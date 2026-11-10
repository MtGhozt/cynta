const state = {
  file: null,
  meta: null,
  jobs: [],
  sockets: new Map(),
  activePreview: null,
  previewText: "",
};

const $ = (id) => document.getElementById(id);

function fmtBytes(n) {
  if (!n && n !== 0) return "";
  const u = ["B", "KB", "MB", "GB"];
  let i = 0;
  let x = n;
  while (x >= 1024 && i < u.length - 1) {
    x /= 1024;
    i += 1;
  }
  return `${x.toFixed(i === 0 ? 0 : 1)} ${u[i]}`;
}

function progressPct(job) {
  const p = job.progress || {};
  if (job.status === "done") return 100;
  if (job.status === "queued") return 2;
  if (job.status === "preparing") return 8;
  if (p.audio_sec && job.result?.duration_sec) {
    return Math.min(95, Math.max(10, (p.audio_sec / job.result.duration_sec) * 100));
  }
  if (p.audio_sec) return Math.min(90, 10 + p.audio_sec / 60);
  if (job.status === "running") return 15;
  return 0;
}

function setFile(file) {
  state.file = file;
  const chip = $("fileChip");
  if (!file) {
    chip.classList.remove("show");
    chip.textContent = "";
    $("submitBtn").disabled = true;
    return;
  }
  chip.classList.add("show");
  chip.textContent = `${file.name} · ${fmtBytes(file.size)}`;
  $("submitBtn").disabled = false;
  if (!$("title").value) {
    $("title").value = file.name.replace(/\.[^.]+$/, "");
  }
}

async function loadMeta() {
  const res = await fetch("/api/meta");
  state.meta = await res.json();
  fillSelect($("language"), state.meta.languages, state.meta.defaults.language);
  fillSelect($("model"), state.meta.models, state.meta.defaults.model);
  fillSelect($("device"), state.meta.devices, state.meta.defaults.device);
  const prompts = Object.entries(state.meta.prompt_templates).map(([k, v]) => [k, v.label]);
  prompts.push(["custom", "Custom…"]);
  fillSelectPairs($("prompt_template"), prompts, state.meta.defaults.prompt_template);
}

function fillSelect(el, values, selected) {
  el.innerHTML = values
    .map((v) => `<option value="${v}" ${v === selected ? "selected" : ""}>${v}</option>`)
    .join("");
}

function fillSelectPairs(el, pairs, selected) {
  el.innerHTML = pairs
    .map(([k, label]) => `<option value="${k}" ${k === selected ? "selected" : ""}>${label}</option>`)
    .join("");
}

async function refreshJobs() {
  const res = await fetch("/api/jobs");
  state.jobs = await res.json();
  renderJobs();
  state.jobs.forEach((j) => {
    if (["queued", "preparing", "running"].includes(j.status)) watchJob(j.id);
  });
}

function renderJobs() {
  const root = $("jobs");
  if (!state.jobs.length) {
    root.innerHTML = `<div class="empty">Todavía no hay jobs. Arrastrá un archivo para empezar.</div>`;
    return;
  }
  root.innerHTML = state.jobs
    .map((job) => {
      const pct = progressPct(job);
      const segs = job.progress?.segments ?? job.result?.segments;
      const audioMin = job.progress?.audio_sec
        ? (job.progress.audio_sec / 60).toFixed(1)
        : job.result?.duration_sec
          ? (job.result.duration_sec / 60).toFixed(1)
          : null;
      const metaBits = [
        job.source_name,
        job.model,
        job.device,
        segs != null ? `${segs} segs` : null,
        audioMin ? `${audioMin} min audio` : null,
        job.error ? job.error : null,
      ]
        .filter(Boolean)
        .join(" · ");
      return `
        <article class="job" data-id="${job.id}">
          <div class="job-top">
            <div>
              <h3 class="job-title">${escapeHtml(job.title)}</h3>
              <p class="job-meta">${escapeHtml(metaBits)}</p>
            </div>
            <span class="status ${job.status}">${job.status}</span>
          </div>
          <div class="progress"><i style="width:${pct}%"></i></div>
          <div class="job-actions">
            ${
              job.status === "done"
                ? `
              <button data-act="preview" data-id="${job.id}">Ver</button>
              <button data-act="md" data-id="${job.id}">MD</button>
              <button data-act="json" data-id="${job.id}">JSON</button>
              <button data-act="srt" data-id="${job.id}">SRT</button>
              <button data-act="folder" data-id="${job.id}">Carpeta</button>
              <button data-act="retry" data-id="${job.id}">Rehacer</button>
            `
                : ""
            }
            ${
              ["queued", "preparing", "running"].includes(job.status)
                ? `<button data-act="cancel" data-id="${job.id}">Cancelar</button>`
                : ""
            }
            ${
              ["error", "cancelled"].includes(job.status)
                ? `<button data-act="retry" data-id="${job.id}">Reintentar</button>`
                : ""
            }
          </div>
        </article>
      `;
    })
    .join("");
}

function escapeHtml(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function watchJob(jobId) {
  if (state.sockets.has(jobId)) return;
  const proto = location.protocol === "https:" ? "wss" : "ws";
  const ws = new WebSocket(`${proto}://${location.host}/ws/jobs/${jobId}`);
  state.sockets.set(jobId, ws);
  ws.onmessage = (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.event === "snapshot" || msg.event === "ping") {
      upsertJob(msg.job);
      return;
    }
    const job = state.jobs.find((j) => j.id === jobId);
    if (!job) return;
    if (msg.event === "progress" || msg.event === "model_ready" || msg.event === "audio_ready") {
      job.progress = msg;
      if (msg.event !== "progress") job.status = job.status === "queued" ? "running" : job.status;
      renderJobs();
    }
    if (msg.event === "done") {
      job.status = "done";
      job.result = msg.result || msg;
      job.progress = { event: "done" };
      renderJobs();
      ws.close();
      state.sockets.delete(jobId);
    }
    if (msg.event === "error" || msg.event === "cancelled") {
      job.status = msg.event === "error" ? "error" : "cancelled";
      job.error = msg.error || job.error;
      renderJobs();
      ws.close();
      state.sockets.delete(jobId);
    }
  };
  ws.onclose = () => state.sockets.delete(jobId);
}

function upsertJob(job) {
  if (!job) return;
  const i = state.jobs.findIndex((j) => j.id === job.id);
  if (i >= 0) state.jobs[i] = job;
  else state.jobs.unshift(job);
  renderJobs();
}

async function submitJob(e) {
  e.preventDefault();
  if (!state.file) return;
  $("submitBtn").disabled = true;
  const fd = new FormData();
  fd.append("file", state.file);
  fd.append("title", $("title").value || state.file.name);
  fd.append("language", $("language").value);
  fd.append("model", $("model").value);
  fd.append("device", $("device").value);
  fd.append("prompt_template", $("prompt_template").value);
  if ($("prompt_template").value === "custom") {
    fd.append("custom_prompt", $("custom_prompt").value);
  }
  try {
    const res = await fetch("/api/jobs", { method: "POST", body: fd });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: res.statusText }));
      alert(err.detail || "Error al crear job");
      return;
    }
    const job = await res.json();
    state.jobs.unshift(job);
    renderJobs();
    watchJob(job.id);
    setFile(null);
    $("title").value = "";
  } finally {
    $("submitBtn").disabled = !state.file;
  }
}

async function onJobAction(e) {
  const btn = e.target.closest("button[data-act]");
  if (!btn) return;
  const id = btn.dataset.id;
  const act = btn.dataset.act;
  if (act === "cancel") {
    await fetch(`/api/jobs/${id}/cancel`, { method: "POST" });
    await refreshJobs();
  } else if (act === "retry") {
    await fetch(`/api/jobs/${id}/retry`, { method: "POST" });
    await refreshJobs();
    watchJob(id);
  } else if (act === "folder") {
    await fetch(`/api/jobs/${id}/open-folder`, { method: "POST" });
  } else if (["md", "json", "srt"].includes(act)) {
    window.open(`/api/jobs/${id}/files/${act}`, "_blank");
  } else if (act === "preview") {
    const res = await fetch(`/api/jobs/${id}/transcript`);
    const data = await res.json();
    state.activePreview = id;
    state.previewText = data.markdown || "";
    $("previewWrap").hidden = false;
    applySearch();
  }
}

function applySearch() {
  const q = ($("searchBox").value || "").trim();
  let text = state.previewText;
  if (q) {
    const re = new RegExp(q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi");
    text = text.replace(re, (m) => `⟦${m}⟧`);
  }
  $("preview").textContent = text;
}

function wireDrop() {
  const drop = $("dropzone");
  const input = $("fileInput");
  drop.addEventListener("click", () => input.click());
  drop.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") input.click();
  });
  input.addEventListener("change", () => setFile(input.files?.[0] || null));
  ["dragenter", "dragover"].forEach((ev) => {
    drop.addEventListener(ev, (e) => {
      e.preventDefault();
      drop.classList.add("dragover");
    });
  });
  ["dragleave", "drop"].forEach((ev) => {
    drop.addEventListener(ev, (e) => {
      e.preventDefault();
      drop.classList.remove("dragover");
    });
  });
  drop.addEventListener("drop", (e) => {
    const f = e.dataTransfer?.files?.[0];
    if (f) setFile(f);
  });
}

async function boot() {
  wireDrop();
  $("jobForm").addEventListener("submit", submitJob);
  $("refreshBtn").addEventListener("click", refreshJobs);
  $("jobs").addEventListener("click", onJobAction);
  $("searchBox").addEventListener("input", applySearch);
  $("prompt_template").addEventListener("change", () => {
    $("customPromptWrap").style.display =
      $("prompt_template").value === "custom" ? "grid" : "none";
  });

  try {
    await fetch("/api/health");
    $("healthBadge").textContent = "local · ok";
  } catch {
    $("healthBadge").textContent = "sin conexión";
  }
  await loadMeta();
  await refreshJobs();
}

boot();
