const state = {
  files: [],
  meta: null,
  health: null,
  jobs: [],
  sockets: new Map(),
  activePreview: null,
  previewText: "",
  editorMode: null, // "view" | "edit" | "study" | null
  editorTab: "segments",
  segments: [],
  dirty: false,
  study: null,
};

const $ = (id) => document.getElementById(id);

let _dialogResolver = null;

function _closeDialog(result) {
  const root = $("cyntaDialog");
  if (!root || root.hidden) return;
  root.hidden = true;
  const resolve = _dialogResolver;
  _dialogResolver = null;
  if (resolve) resolve(result);
}

function showDialog({ message, confirm = false, okLabel = "Aceptar", cancelLabel = "Cancelar" }) {
  return new Promise((resolve) => {
    if (_dialogResolver) _closeDialog(false);
    _dialogResolver = resolve;
    const root = $("cyntaDialog");
    const msg = $("cyntaDialogMsg");
    const ok = $("cyntaDialogOk");
    const cancel = $("cyntaDialogCancel");
    msg.textContent = message;
    ok.textContent = okLabel;
    cancel.textContent = cancelLabel;
    cancel.hidden = !confirm;
    root.hidden = false;
    ok.focus();
  });
}

function cyntaAlert(message) {
  return showDialog({ message, confirm: false, okLabel: "Entendido" });
}

function cyntaConfirm(message, { okLabel = "Aceptar", cancelLabel = "Cancelar" } = {}) {
  return showDialog({ message, confirm: true, okLabel, cancelLabel });
}

function wireDialog() {
  const root = $("cyntaDialog");
  if (!root) return;
  $("cyntaDialogOk").addEventListener("click", () => _closeDialog(true));
  $("cyntaDialogCancel").addEventListener("click", () => _closeDialog(false));
  root.querySelector("[data-dialog-dismiss]")?.addEventListener("click", () => {
    const cancel = $("cyntaDialogCancel");
    _closeDialog(!cancel.hidden ? false : true);
  });
  document.addEventListener("keydown", (e) => {
    if (root.hidden) return;
    if (e.key === "Escape") {
      e.preventDefault();
      const cancel = $("cyntaDialogCancel");
      _closeDialog(!cancel.hidden ? false : true);
    } else if (e.key === "Enter") {
      e.preventDefault();
      _closeDialog(true);
    }
  });
}

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

  const partCount = p.part_count || job.parts?.length || job.result?.parts;
  const partIndex =
    typeof p.part_index === "number" ? p.part_index : null;
  if (partCount && partIndex != null && job.status === "running") {
    const base = (partIndex / partCount) * 100;
    const within = p.audio_sec ? Math.min(20, p.audio_sec / 30) : 5;
    return Math.min(95, Math.max(10, base + within));
  }

  if (p.audio_sec && job.result?.duration_sec) {
    return Math.min(95, Math.max(10, (p.audio_sec / job.result.duration_sec) * 100));
  }
  if (p.audio_sec) return Math.min(90, 10 + p.audio_sec / 60);
  if (job.status === "running") return 15;
  return 0;
}

function partProgressLabel(job) {
  const p = job.progress || {};
  const parts = job.parts;
  const count = p.part_count || parts?.length || job.result?.parts;
  if (!count || count < 2) return null;
  let index = typeof p.part_index === "number" ? p.part_index : null;
  if (index == null && Array.isArray(parts)) {
    const running = parts.findIndex((x) => x.status === "running");
    const done = parts.filter((x) => x.status === "done").length;
    index = running >= 0 ? running : Math.min(done, count - 1);
  }
  if (index == null) return `${count} partes`;
  const name = p.part_name || parts?.[index]?.source_name || "";
  const label = `Parte ${index + 1}/${count}`;
  return name ? `${label} — ${name}` : label;
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
  const ollamaOk = Boolean(info?.ollama?.ok);
  if (!ffmpegOk || !cudaOk || !ollamaOk) {
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

function setFiles(fileList) {
  const files = fileList ? [...fileList].filter(Boolean) : [];
  state.files = files;
  const chip = $("fileChip");
  if (!files.length) {
    chip.hidden = true;
    chip.textContent = "";
    $("submitBtn").disabled = true;
    return;
  }
  chip.hidden = false;
  if (files.length === 1) {
    chip.textContent = `${files[0].name}  ${fmtBytes(files[0].size)}`;
  } else {
    const total = files.reduce((sum, f) => sum + (f.size || 0), 0);
    const names = files.map((f) => f.name).join(", ");
    chip.textContent = `${files.length} archivos (${fmtBytes(total)}): ${names}`;
  }
  $("submitBtn").disabled = false;
  if (!$("title").value) {
    $("title").value = files[0].name.replace(/\.[^.]+$/, "");
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
    root.innerHTML = `<p class="empty">Nada en cola. Soltá uno o varios archivos a la izquierda.</p>`;
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
      const partLabel = partProgressLabel(job);
      const metaBits = [
        partLabel,
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
              <button type="button" data-act="study" data-id="${job.id}">${
                  state.activePreview === job.id &&
                  !$("previewWrap")?.hidden &&
                  state.editorMode === "study"
                    ? "Cerrar"
                    : "Estudio"
                }</button>
              <button type="button" data-act="md" data-id="${job.id}">MD</button>
              <button type="button" data-act="json" data-id="${job.id}">JSON</button>
              <button type="button" data-act="srt" data-id="${job.id}">SRT</button>
              <button type="button" data-act="opencards" data-id="${job.id}">OpenCards</button>
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
    if (
      msg.event === "progress" ||
      msg.event === "model_ready" ||
      msg.event === "audio_ready" ||
      msg.event === "part_start" ||
      msg.event === "part_done" ||
      msg.event === "part_skip" ||
      msg.event === "preparing"
    ) {
      job.progress = msg;
      if (msg.event !== "progress") {
        job.status =
          job.status === "queued"
            ? msg.event === "preparing"
              ? "preparing"
              : "running"
            : job.status === "preparing" && msg.event !== "preparing"
              ? "running"
              : job.status;
      }
      if (Array.isArray(job.parts) && typeof msg.part_index === "number") {
        const part = job.parts[msg.part_index];
        if (part) {
          if (msg.event === "part_start") part.status = "running";
          if (msg.event === "part_done" || msg.event === "part_skip") {
            part.status = "done";
            if (msg.duration_sec != null) part.duration_sec = msg.duration_sec;
          }
        }
      }
      renderJobs();
      setHealth("ok", "local");
    }
    if (msg.event === "done") {
      job.status = "done";
      job.result = msg.result || msg;
      job.progress = { event: "done", part_count: msg.result?.parts || job.parts?.length };
      renderJobs();
      setHealth("ok", "local");
      ws.close();
      state.sockets.delete(jobId);
    }
    if (msg.event === "error" || msg.event === "cancelled") {
      job.status = msg.event === "error" ? "error" : "cancelled";
      job.error = msg.error || job.error;
      if (Array.isArray(job.parts) && typeof msg.part_index === "number") {
        const part = job.parts[msg.part_index];
        if (part && msg.event === "error") {
          part.status = "error";
          part.error = msg.error;
        }
      }
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
  if (!state.files.length) return;
  $("submitBtn").disabled = true;
  const fd = new FormData();
  for (const f of state.files) {
    fd.append("files", f);
  }
  fd.append("title", $("title").value || state.files[0].name);
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
      await cyntaAlert(typeof err.detail === "string" ? err.detail : "No se pudo crear el job");
      return;
    }
    const job = await res.json();
    state.jobs.unshift(job);
    renderJobs();
    watchJob(job.id);
    setFiles([]);
    $("fileInput").value = "";
    $("title").value = "";
    setHealth("ok", "local");
  } finally {
    $("submitBtn").disabled = !state.files.length;
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
  } else if (["md", "json", "srt", "opencards", "outline", "outline_md"].includes(act)) {
    window.open(`/api/jobs/${id}/files/${act}`, "_blank");
  } else if (act === "study") {
    if (
      state.activePreview === id &&
      !$("previewWrap").hidden &&
      state.editorMode === "study"
    ) {
      await closeEditor();
      return;
    }
    await openStudy(id);
  } else if (act === "view") {
    if (
      state.activePreview === id &&
      !$("previewWrap").hidden &&
      state.editorMode === "view"
    ) {
      await closeEditor();
      return;
    }
    await openViewer(id);
  } else if (act === "edit") {
    if (
      state.activePreview === id &&
      !$("previewWrap").hidden &&
      state.editorMode === "edit"
    ) {
      await closeEditor();
      return;
    }
    await openEditor(id);
  }
}

async function closeEditor() {
  if (state.dirty) {
    const ok = await cyntaConfirm("Hay cambios sin guardar. ¿Cerrar igual?");
    if (!ok) return;
  }
  state.activePreview = null;
  state.editorMode = null;
  state.segments = [];
  state.previewText = "";
  state.study = null;
  setDirty(false);
  $("previewWrap").hidden = true;
  $("editorHint").hidden = true;
  $("studyMeta").hidden = true;
  $("studyMeta").textContent = "";
  $("saveSegmentsBtn").hidden = false;
  $("segmentsEditor").innerHTML = "";
  $("preview").textContent = "";
  $("studyOutline").innerHTML = "";
  $("studyCards").innerHTML = "";
  $("studyOutline").hidden = true;
  $("studyCards").hidden = true;
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
  const outline = $("studyOutline");
  const cards = $("studyCards");
  segs.hidden = tab !== "segments";
  md.hidden = tab !== "markdown";
  outline.hidden = tab !== "outline";
  cards.hidden = tab !== "cards";
  if (tab === "markdown") applyMarkdownPreview();
  if (tab === "outline") renderStudyOutline();
  if (tab === "cards") renderStudyCards();
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
  if (state.editorTab === "outline" || state.editorTab === "cards") {
    const q = ($("searchBox").value || "").trim().toLowerCase();
    const root = state.editorTab === "outline" ? $("studyOutline") : $("studyCards");
    root.querySelectorAll(".study-item, .study-card").forEach((el) => {
      const text = (el.textContent || "").toLowerCase();
      el.hidden = Boolean(q && !text.includes(q));
    });
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
  const outlineTab = document.querySelector('.reader-tabs .tab[data-tab="outline"]');
  const cardsTab = document.querySelector('.reader-tabs .tab[data-tab="cards"]');
  const hint = $("editorHint");
  const saveBtn = $("saveSegmentsBtn");
  const studyMeta = $("studyMeta");
  if (mode === "view") {
    if (editTab) editTab.hidden = true;
    if (mdTab) mdTab.hidden = true;
    if (outlineTab) outlineTab.hidden = true;
    if (cardsTab) cardsTab.hidden = true;
    hint.hidden = true;
    studyMeta.hidden = true;
    saveBtn.hidden = true;
    $("dirtyFlag").hidden = true;
  } else if (mode === "study") {
    if (editTab) editTab.hidden = true;
    if (mdTab) mdTab.hidden = true;
    if (outlineTab) outlineTab.hidden = false;
    if (cardsTab) cardsTab.hidden = false;
    hint.hidden = true;
    studyMeta.hidden = false;
    saveBtn.hidden = true;
    $("dirtyFlag").hidden = true;
  } else {
    if (editTab) editTab.hidden = false;
    if (mdTab) mdTab.hidden = false;
    if (outlineTab) outlineTab.hidden = true;
    if (cardsTab) cardsTab.hidden = true;
    hint.hidden = false;
    studyMeta.hidden = true;
    saveBtn.hidden = false;
  }
}

function fmtStudyTime(sec) {
  return fmtSegTime(sec);
}

function renderStudyOutline() {
  const root = $("studyOutline");
  const chapters = state.study?.outline?.chapters || [];
  if (!chapters.length) {
    root.innerHTML = `<p class="empty">Sin capítulos.</p>`;
    return;
  }
  root.innerHTML = chapters
    .map((ch, i) => {
      const stamp = fmtStudyTime(ch.start_sec);
      const summary = ch.summary
        ? `<p class="study-summary">${escapeHtml(ch.summary)}</p>`
        : "";
      return `
        <article class="study-item">
          <p class="study-stamp">${i + 1}. [${escapeHtml(stamp)}]</p>
          <h4 class="study-title">${escapeHtml(ch.title || "Sin título")}</h4>
          ${summary}
        </article>`;
    })
    .join("");
}

function renderStudyCards() {
  const root = $("studyCards");
  const cards = state.study?.deck?.cards || [];
  if (!cards.length) {
    root.innerHTML = `<p class="empty">Sin cards. Generá estudio de nuevo.</p>`;
    return;
  }
  root.innerHTML = cards
    .map((card, i) => {
      return `
        <article class="study-card">
          <p class="study-stamp">Card ${i + 1}</p>
          <p class="study-front"><strong>Q:</strong> ${escapeHtml(card.front || "")}</p>
          <p class="study-back"><strong>A:</strong> ${escapeHtml(card.back || "")}</p>
        </article>`;
    })
    .join("");
}

async function openStudy(id) {
  if (state.dirty && state.activePreview && state.activePreview !== id) {
    if (!(await cyntaConfirm("Hay cambios sin guardar. ¿Descartarlos y abrir estudio?"))) {
      return;
    }
  }
  const btnBusy = document.querySelector(`button[data-act="study"][data-id="${id}"]`);
  if (btnBusy) {
    btnBusy.disabled = true;
    btnBusy.textContent = "Generando…";
  }
  try {
    let data = null;
    const existing = await fetch(`/api/jobs/${id}/study`);
    if (existing.ok) {
      data = await existing.json();
    } else {
      const res = await fetch(`/api/jobs/${id}/study`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ force: true, use_ollama: true }),
      });
      data = await res.json().catch(() => ({}));
      if (!res.ok) {
        await cyntaAlert(errDetail(data) || "No se pudo generar el estudio");
        return;
      }
    }

    state.activePreview = id;
    state.editorMode = "study";
    state.study = data;
    state.segments = [];
    setDirty(false);
    $("previewWrap").hidden = false;
    setReaderChrome("study");

    const mode = data.mode || data.outline?.mode || "heuristic";
    const cardsCount = data.deck?.cards_count ?? data.deck?.cards?.length ?? 0;
    const warn = data.ollama?.warning || data.outline?.ollama?.warning;
    const ollamaUsed = Boolean(data.ollama?.used || data.outline?.ollama?.used);
    const bits = [
      `modo: ${mode}`,
      ollamaUsed ? `ollama: ${data.ollama?.model || data.outline?.ollama?.model || "sí"}` : "ollama: no",
      `${cardsCount} cards`,
      "importá OpenCards en Open Cards",
    ];
    if (warn) bits.push(warn);
    $("studyMeta").textContent = bits.join(" · ");
    $("studyMeta").hidden = false;

    setEditorTab("outline");
    renderJobs();
    $("previewWrap").scrollIntoView({ behavior: "smooth", block: "nearest" });
  } finally {
    renderJobs();
  }
}

async function openViewer(id) {
  if (state.dirty && state.activePreview && state.activePreview !== id) {
    if (!(await cyntaConfirm("Hay cambios sin guardar. ¿Descartarlos y abrir otro job?"))) {
      return;
    }
  }
  if (state.dirty && state.activePreview === id && state.editorMode === "edit") {
    if (!(await cyntaConfirm("Hay cambios sin guardar. ¿Descartarlos y solo ver?"))) {
      return;
    }
  }
  const res = await fetch(`/api/jobs/${id}/transcript`);
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    await cyntaAlert(errDetail(data) || "No se pudo cargar la transcripción");
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
    if (!(await cyntaConfirm("Hay cambios sin guardar. ¿Descartarlos y abrir otro job?"))) {
      return;
    }
  }
  const res = await fetch(`/api/jobs/${id}/segments`);
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    await cyntaAlert(errDetail(data) || "No se pudieron cargar los segmentos");
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
      await cyntaAlert(errDetail(data) || `No se pudo guardar (${res.status})`);
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
    await cyntaAlert(`No se pudo guardar: ${e}`);
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
  input.addEventListener("change", () => setFiles(input.files || []));
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
    const list = e.dataTransfer?.files;
    if (list?.length) setFiles(list);
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
      await cyntaAlert(errDetail(data) || `No se pudo elegir la carpeta (${res.status})`);
      return;
    }
    if (data.output_dir) $("outputDir").value = data.output_dir;
    if (data.jobs_dir) $("outPath").textContent = data.jobs_dir;
  } catch (e) {
    if (e && e.name === "AbortError") {
      await cyntaAlert("El selector de carpeta tardó demasiado. Probá de nuevo.");
    } else {
      await cyntaAlert(`No se pudo elegir la carpeta: ${e}`);
    }
  } finally {
    clearTimeout(timer);
    btn.disabled = false;
    btn.textContent = prev || "Elegir carpeta";
  }
}

async function clearQueue() {
  const ok = await cyntaConfirm(
    "¿Limpiar jobs terminados (done/error/cancelados) de la lista y del disco?"
  );
  if (!ok) return;
  const res = await fetch("/api/jobs/clear", { method: "POST" });
  const data = await res.json();
  await refreshJobs();
  if (data.removed === 0) {
    await cyntaAlert("No había jobs terminados para limpiar.");
  }
}

async function boot() {
  wireTheme();
  wireDialog();
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
