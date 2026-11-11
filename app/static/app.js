const state = {
  file: null,
  meta: null,
  health: null,
  jobs: [],
  sockets: new Map(),
  activePreview: null,
  previewText: "",
  editorMode: null, // "view" | "edit" | null
  editorTab: "segments",
  segments: [],
  dirty: false,
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

function setHealth(kind, text, title) {
  const el = $("healthBadge");
  el.classList.remove("ok", "bad", "busy", "warn");
  el.classList.add(kind);
  el.querySelector(".live-text").textContent = text;
  if (title) el.title = title;
  const busy = state.jobs.some((j) =>
    ["queued", "preparing", "running"].includes(j.status)
  );
  if (busy && (kind === "ok" || kind === "warn")) {
    el.classList.remove("ok", "warn");
    el.classList.add("busy");
  }
}

function applyHealth(info) {
  const cudaOk = Boolean(info?.cuda?.ok);
  const ffmpegOk = Boolean(info?.ffmpeg?.ok);
  const gpuName = info?.cuda?.gpu?.name || "";
  const warnings = Array.isArray(info?.warnings) ? info.warnings : [];

  if (!info?.ok) {
    setHealth("bad", "offline", "Servidor no responde");
    return;
  }

  if (cudaOk) {
    setHealth("ok", "cuda", gpuName ? `GPU: ${gpuName}` : "CUDA listo");
  } else {
    setHealth(
      "warn",
      "cpu",
      warnings[0] || "Sin CUDA usable — se recomienda device=cpu"
    );
  }

  const banner = $("envBanner");
  if (!ffmpegOk || !cudaOk) {
    banner.hidden = false;
    banner.textContent = warnings.join(" · ") || "Revisá el entorno local.";
  } else {
    banner.hidden = true;
    banner.textContent = "";
  }

  const device = $("device");
  if (device && info.recommended_device && !device.dataset.userPicked) {
    const want = info.recommended_device;
    if ([...device.options].some((o) => o.value === want)) {
      device.value = want;
    }
  }
}

function setFile(file) {
  state.file = file;
  const chip = $("fileChip");
  if (!file) {
    chip.hidden = true;
    chip.textContent = "";
    $("submitBtn").disabled = true;
    return;
  }
  chip.hidden = false;
  chip.textContent = `${file.name}  ${fmtBytes(file.size)}`;
  $("submitBtn").disabled = false;
  if (!$("title").value) {
    $("title").value = file.name.replace(/\.[^.]+$/, "");
  }
}

async function loadMeta() {
  const res = await fetch("/api/meta");
  state.meta = await res.json();
  const languages = (state.meta.languages || ["es", "en", "auto"]).map((code) => {
    const labels = { es: "Español", en: "English", auto: "Auto" };
    return [code, labels[code] || code];
  });
  fillSelectPairs($("language"), languages, state.meta.defaults.language);
  fillSelect($("model"), state.meta.models, state.meta.defaults.model);
  const recommended =
    state.health?.recommended_device || state.meta.defaults.device;
  fillSelect($("device"), state.meta.devices, recommended);
  $("device").addEventListener(
    "change",
    () => {
      $("device").dataset.userPicked = "1";
    },
    { once: true }
  );
  const prompts = Object.entries(state.meta.prompt_templates).map(([k, v]) => [k, v.label]);
  prompts.push(["custom", "Custom"]);
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
  setHealth("ok", "local");
  state.jobs.forEach((j) => {
    if (["queued", "preparing", "running"].includes(j.status)) watchJob(j.id);
  });
}

function renderJobs() {
  const root = $("jobs");
  if (!state.jobs.length) {
    root.innerHTML = `<p class="empty">Nada en cola. Soltá un archivo a la izquierda.</p>`;
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
        audioMin ? `${audioMin} min` : null,
        job.error || null,
      ]
        .filter(Boolean)
        .join(" / ");
      const barClass = ["running", "preparing"].includes(job.status)
        ? "running"
        : job.status === "done"
          ? "done"
          : "";
      return `
        <article class="job" data-id="${job.id}">
          <div class="job-top">
            <div>
              <h3 class="job-title">${escapeHtml(job.title)}</h3>
              <p class="job-meta">${escapeHtml(metaBits)}</p>
            </div>
            <span class="status ${job.status}">${job.status}</span>
          </div>
          <div class="progress ${barClass}"><i style="width:${pct}%"></i></div>
          <div class="job-actions">
            ${
              job.status === "done"
                ? `
              <button type="button" data-act="view" data-id="${job.id}">${
                  state.activePreview === job.id &&
                  !$("previewWrap")?.hidden &&
                  state.editorMode === "view"
                    ? "Cerrar"
                    : "Ver"
                }</button>
              <button type="button" data-act="edit" data-id="${job.id}">${
                  state.activePreview === job.id &&
                  !$("previewWrap")?.hidden &&
                  state.editorMode === "edit"
                    ? "Cerrar"
                    : "Editar"
                }</button>
              <button type="button" data-act="md" data-id="${job.id}">MD</button>
              <button type="button" data-act="json" data-id="${job.id}">JSON</button>
              <button type="button" data-act="srt" data-id="${job.id}">SRT</button>
              <button type="button" data-act="folder" data-id="${job.id}">Carpeta</button>
              <button type="button" data-act="retry" data-id="${job.id}">Rehacer</button>
            `
                : ""
            }
            ${
              ["queued", "preparing", "running"].includes(job.status)
                ? `<button type="button" data-act="cancel" data-id="${job.id}">Cancelar</button>`
                : ""
            }
            ${
              ["error", "cancelled"].includes(job.status)
                ? `<button type="button" data-act="retry" data-id="${job.id}">Reintentar</button>`
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
      setHealth("ok", "local");
    }
    if (msg.event === "done") {
      job.status = "done";
      job.result = msg.result || msg;
      job.progress = { event: "done" };
      renderJobs();
      setHealth("ok", "local");
      ws.close();
      state.sockets.delete(jobId);
    }
    if (msg.event === "error" || msg.event === "cancelled") {
      job.status = msg.event === "error" ? "error" : "cancelled";
      job.error = msg.error || job.error;
      renderJobs();
      setHealth("ok", "local");
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
  setHealth("ok", "local");
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
      alert(typeof err.detail === "string" ? err.detail : "No se pudo crear el job");
      return;
    }
    const job = await res.json();
    state.jobs.unshift(job);
    renderJobs();
    watchJob(job.id);
    setFile(null);
    $("title").value = "";
    setHealth("ok", "local");
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
  } else if (act === "view") {
    if (
      state.activePreview === id &&
      !$("previewWrap").hidden &&
      state.editorMode === "view"
    ) {
      closeEditor();
      return;
    }
    await openViewer(id);
  } else if (act === "edit") {
    if (
      state.activePreview === id &&
      !$("previewWrap").hidden &&
      state.editorMode === "edit"
    ) {
      closeEditor();
      return;
    }
    await openEditor(id);
  }
}

function closeEditor() {
  if (state.dirty) {
    if (!confirm("Hay cambios sin guardar. ¿Cerrar igual?")) {
      return;
    }
  }
  state.activePreview = null;
  state.editorMode = null;
  state.segments = [];
  state.previewText = "";
  setDirty(false);
  $("previewWrap").hidden = true;
  $("editorHint").hidden = true;
  $("saveSegmentsBtn").hidden = false;
  $("segmentsEditor").innerHTML = "";
  $("preview").textContent = "";
  document.querySelectorAll(".reader-tabs .tab").forEach((btn) => {
    btn.hidden = false;
  });
  renderJobs();
}

function fmtSegTime(sec) {
  const t = Math.max(0, Math.floor(Number(sec) || 0));
  const h = Math.floor(t / 3600);
  const m = Math.floor((t % 3600) / 60);
  const s = t % 60;
  if (h > 0) {
    return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  }
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

function setDirty(on) {
  state.dirty = Boolean(on);
  $("dirtyFlag").hidden = !state.dirty;
  $("saveSegmentsBtn").disabled = !state.dirty || !state.activePreview;
}

function setEditorTab(tab) {
  state.editorTab = tab;
  document.querySelectorAll(".reader-tabs .tab").forEach((btn) => {
    const active = btn.dataset.tab === tab;
    btn.classList.toggle("is-active", active);
    btn.setAttribute("aria-selected", active ? "true" : "false");
  });
  const segs = $("segmentsEditor");
  const md = $("preview");
  if (tab === "segments") {
    segs.hidden = false;
    md.hidden = true;
  } else {
    segs.hidden = true;
    md.hidden = false;
    applyMarkdownPreview();
  }
}

function applyMarkdownPreview() {
  const q = ($("searchBox").value || "").trim();
  let text = state.previewText || "";
  if (q) {
    const re = new RegExp(q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi");
    text = text.replace(re, (m) => `⟦${m}⟧`);
  }
  $("preview").textContent = text;
}

function renderSegments() {
  const root = $("segmentsEditor");
  const q = ($("searchBox").value || "").trim().toLowerCase();
  root.innerHTML = state.segments
    .map((seg, i) => {
      const text = seg.text || "";
      const hit = !q || text.toLowerCase().includes(q);
      return `
        <div class="seg-row${hit ? (q ? " is-hit" : "") : " is-hidden"}" data-idx="${i}">
          <div class="seg-time">${escapeHtml(fmtSegTime(seg.start))}</div>
          <textarea data-idx="${i}" rows="2" spellcheck="true">${escapeHtml(text)}</textarea>
        </div>`;
    })
    .join("");
}

function applySearch() {
  if (state.editorTab === "markdown") {
    applyMarkdownPreview();
    return;
  }
  const q = ($("searchBox").value || "").trim().toLowerCase();
  $("segmentsEditor").querySelectorAll(".seg-row").forEach((row) => {
    const idx = Number(row.dataset.idx);
    const text = (state.segments[idx]?.text || "").toLowerCase();
    const hit = !q || text.includes(q);
    row.classList.toggle("is-hidden", !hit);
    row.classList.toggle("is-hit", Boolean(q && hit));
  });
}

function setReaderChrome(mode) {
  const editTab = document.querySelector('.reader-tabs .tab[data-tab="segments"]');
  const mdTab = document.querySelector('.reader-tabs .tab[data-tab="markdown"]');
  const hint = $("editorHint");
  const saveBtn = $("saveSegmentsBtn");
  if (mode === "view") {
    if (editTab) editTab.hidden = true;
    if (mdTab) mdTab.hidden = true;
    hint.hidden = true;
    saveBtn.hidden = true;
    $("dirtyFlag").hidden = true;
  } else {
    if (editTab) editTab.hidden = false;
    if (mdTab) mdTab.hidden = false;
    hint.hidden = false;
    saveBtn.hidden = false;
  }
}

async function openViewer(id) {
  if (state.dirty && state.activePreview && state.activePreview !== id) {
    if (!confirm("Hay cambios sin guardar. ¿Descartarlos y abrir otro job?")) {
      return;
    }
  }
  if (state.dirty && state.activePreview === id && state.editorMode === "edit") {
    if (!confirm("Hay cambios sin guardar. ¿Descartarlos y solo ver?")) {
      return;
    }
  }
  const res = await fetch(`/api/jobs/${id}/transcript`);
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    alert(errDetail(data) || "No se pudo cargar la transcripción");
    return;
  }
  state.activePreview = id;
  state.editorMode = "view";
  state.segments = [];
  state.previewText = data.markdown || "";
  setDirty(false);
  $("previewWrap").hidden = false;
  setReaderChrome("view");
  setEditorTab("markdown");
  applyMarkdownPreview();
  renderJobs();
  $("previewWrap").scrollIntoView({ behavior: "smooth", block: "nearest" });
}

async function openEditor(id) {
  if (state.dirty && state.activePreview && state.activePreview !== id) {
    if (!confirm("Hay cambios sin guardar. ¿Descartarlos y abrir otro job?")) {
      return;
    }
  }
  const res = await fetch(`/api/jobs/${id}/segments`);
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    alert(errDetail(data) || "No se pudieron cargar los segmentos");
    return;
  }
  state.activePreview = id;
  state.editorMode = "edit";
  state.segments = (data.segments || []).map((s) => ({
    start: Number(s.start),
    end: Number(s.end),
    text: String(s.text || ""),
  }));
  setDirty(false);
  $("previewWrap").hidden = false;
  setReaderChrome("edit");
  setEditorTab("segments");
  renderSegments();
  renderJobs();
  $("previewWrap").scrollIntoView({ behavior: "smooth", block: "nearest" });

  fetch(`/api/jobs/${id}/transcript`)
    .then((r) => r.json())
    .then((d) => {
      if (state.activePreview === id) {
        state.previewText = d.markdown || "";
        if (state.editorTab === "markdown") applyMarkdownPreview();
      }
    })
    .catch(() => {
      if (state.activePreview === id) state.previewText = "";
    });
}

async function saveSegments() {
  const id = state.activePreview;
  if (!id || !state.dirty) return;
  const btn = $("saveSegmentsBtn");
  btn.disabled = true;
  btn.textContent = "Guardando…";
  try {
    const res = await fetch(`/api/jobs/${id}/segments`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ segments: state.segments }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      alert(errDetail(data) || `No se pudo guardar (${res.status})`);
      return;
    }
    setDirty(false);
    const mdRes = await fetch(`/api/jobs/${id}/transcript`);
    if (mdRes.ok) {
      const md = await mdRes.json();
      state.previewText = md.markdown || "";
      if (state.editorTab === "markdown") applyMarkdownPreview();
    }
  } catch (e) {
    alert(`No se pudo guardar: ${e}`);
  } finally {
    btn.textContent = "Guardar";
    btn.disabled = !state.dirty;
  }
}

function wireEditor() {
  $("searchBox").addEventListener("input", applySearch);
  $("saveSegmentsBtn").addEventListener("click", saveSegments);
  $("closeEditorBtn").addEventListener("click", closeEditor);
  document.querySelectorAll(".reader-tabs .tab").forEach((btn) => {
    btn.addEventListener("click", () => setEditorTab(btn.dataset.tab));
  });
  $("segmentsEditor").addEventListener("input", (e) => {
    const ta = e.target.closest("textarea[data-idx]");
    if (!ta) return;
    const idx = Number(ta.dataset.idx);
    if (!state.segments[idx]) return;
    state.segments[idx].text = ta.value;
    setDirty(true);
  });
  window.addEventListener("beforeunload", (e) => {
    if (!state.dirty) return;
    e.preventDefault();
    e.returnValue = "";
  });
}

function wireDrop() {
  const drop = $("dropzone");
  const input = $("fileInput");
  drop.addEventListener("click", () => input.click());
  drop.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      input.click();
    }
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

function applyTheme(theme) {
  const next = theme === "dark" ? "dark" : "light";
  document.documentElement.setAttribute("data-theme", next);
  document.documentElement.style.colorScheme = next;
  localStorage.setItem("cynta-theme", next);
  localStorage.removeItem("cinta-theme");
  const btn = $("themeToggle");
  if (btn) {
    const dark = next === "dark";
    btn.setAttribute("aria-pressed", dark ? "true" : "false");
    btn.textContent = dark ? "Claro" : "Oscuro";
  }
  document.querySelectorAll("select").forEach((el) => {
    el.style.colorScheme = next;
  });
}

function wireTheme() {
  const saved = localStorage.getItem("cynta-theme") || localStorage.getItem("cinta-theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  applyTheme(saved || (prefersDark ? "dark" : "light"));
  $("themeToggle").addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme");
    applyTheme(cur === "dark" ? "light" : "dark");
  });
}

async function loadSettings() {
  const res = await fetch("/api/settings");
  const data = await res.json();
  $("outputDir").value = data.output_dir || "";
  $("outPath").textContent = data.jobs_dir || data.output_dir || "";
}

function errDetail(err) {
  if (!err) return null;
  if (typeof err.detail === "string") return err.detail;
  if (Array.isArray(err.detail)) {
    return err.detail.map((d) => d.msg || JSON.stringify(d)).join("; ");
  }
  return err.message || null;
}

async function pickOutputDir() {
  const btn = $("pickPathBtn");
  if (btn.disabled) return;
  btn.disabled = true;
  const prev = btn.textContent;
  btn.textContent = "Eligiendo…";
  const ac = new AbortController();
  const timer = setTimeout(() => ac.abort(), 180000);
  try {
    const res = await fetch("/api/settings/pick-output-dir", {
      method: "POST",
      signal: ac.signal,
      cache: "no-store",
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      alert(errDetail(data) || `No se pudo elegir la carpeta (${res.status})`);
      return;
    }
    if (data.output_dir) $("outputDir").value = data.output_dir;
    if (data.jobs_dir) $("outPath").textContent = data.jobs_dir;
  } catch (e) {
    if (e && e.name === "AbortError") {
      alert("El selector de carpeta tardó demasiado. Probá de nuevo.");
    } else {
      alert(`No se pudo elegir la carpeta: ${e}`);
    }
  } finally {
    clearTimeout(timer);
    btn.disabled = false;
    btn.textContent = prev || "Elegir carpeta";
  }
}

async function clearQueue() {
  if (!confirm("¿Limpiar jobs terminados (done/error/cancelados) de la lista y del disco?")) {
    return;
  }
  const res = await fetch("/api/jobs/clear", { method: "POST" });
  const data = await res.json();
  await refreshJobs();
  if (data.removed === 0) {
    alert("No había jobs terminados para limpiar.");
  }
}

async function boot() {
  wireTheme();
  wireDrop();
  $("jobForm").addEventListener("submit", submitJob);
  $("refreshBtn").addEventListener("click", refreshJobs);
  $("clearBtn").addEventListener("click", clearQueue);
  $("pickPathBtn").addEventListener("click", pickOutputDir);
  $("jobs").addEventListener("click", onJobAction);
  wireEditor();
  $("prompt_template").addEventListener("change", () => {
    $("customPromptWrap").hidden = $("prompt_template").value !== "custom";
  });

  try {
    const health = await fetch("/api/health").then((r) => r.json());
    state.health = health;
    applyHealth(health);
    await loadSettings();
  } catch {
    state.health = null;
    setHealth("bad", "offline", "Servidor no responde");
  }
  await loadMeta();
  if (state.health) applyHealth(state.health);
  await refreshJobs();
}

boot();
