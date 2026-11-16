# Cynta — Roadmap

Documento vivo de qué ya está, qué entra en cada versión y qué queda fuera a propósito.
Actualizalo al cerrar una versión (mover ítems a **Hecho** y ajustar la siguiente).

**Principios**

- Local-first: la app tiene que servir sin nube.
- IA externa (OpenAI/Anthropic/etc.) **al final**, no en el núcleo ASR.
- Preferir slices chicos que se puedan usar solos (editor antes que LLM; batch antes que realtime).

---

## Hecho

### v0.1 — Motor batch (CLI)

- Whisper (faster-whisper) para clases en `Clases/`
- Export MD / JSON / SRT
- GPU NVIDIA + fallback CPU

### v0.2 — Producto local “Cynta”

- UI drag & drop (audio/video via ffmpeg)
- Cola de jobs + progreso WebSocket + SQLite
- Plantillas de prompt (dominio), dark mode
- Carpeta de salida configurable (picker Windows moderno)
- Launcher `run.bat` / `run.ps1` + health CUDA/ffmpeg
- Viewer + editor de segmentos (`Ver` / `Editar` → Guardar regenera MD/JSON/SRT)

---

## Próximo

### v0.3 — Clase = varios archivos

**Objetivo:** juntar varios audios/videos en una sola “clase” con timeline continuo.

- Upload / cola de **varios** archivos bajo un mismo título/clase
- Merge de `segmentos.json` con offsets de tiempo
- Un MD/SRT unificado + jobs parciales visibles en la cola
- (Opcional) reordenar clips antes de merge

**Listo cuando:** podés soltar 2+ archivos, obtener una sola transcripción ordenada y editarla como hoy.

### v0.4 — Estudio local (sin API paga)

**Objetivo:** sacar valor de estudio **después** del ASR, sin obligar nube.

- Outline / capítulos a partir de timestamps (heurística o LLM **local** tipo Ollama)
- Flashcards / preguntas desde segmentos (mismo motor local)
- Export de outline + cards junto al job
- Si no hay Ollama: degradar a outline heurístico (por gaps / headings), no romper la UI

**Listo cuando:** un job done puede generar outline + cards en la máquina, con aviso claro si falta el modelo local.

> APIs externas (OpenAI, etc.) quedan para un add-on opcional **después de v0.4**, no bloquean esta versión.

### v0.5 — Realtime

**Objetivo:** transcribir lo que oís (Zoom/Meet/clase en vivo).

- Captura micrófono **o** loopback WASAPI (Windows)
- Streaming a Whisper (ventanas / VAD)
- UI de sesión en vivo → al parar, materializa un job normal (editable)

**Listo cuando:** una sesión de ~10 min produce segmentos guardables sin permiso del host de Zoom.

### v1.0 — Empaquetado + LAN

**Objetivo:** que un compañero lo use sin pelearse con Python.

- Empaquetado `.exe` (Tauri o similar + sidecar Python)
- Onboarding CUDA/CPU en primer arranque (ya hay health; pulir UX del instalador)
- Modo LAN: mismos endpoints, bind a `0.0.0.0` + aviso de firewall
- README “para compañeros” de una página

**Listo cuando:** doble clic instala/abre Cynta en una PC limpia con GPU o CPU.

---

## Después de v1.0

### Slides + OCR

- Detectar cambios de diapositiva / frames clave
- OCR alineado a timestamps del transcript
- Vista combinada “qué se dijo / qué se vio”

### Multi-usuario / cloud opcional

- Auth, object storage, cola server
- Misma API que hoy; la UI local puede apuntar a un worker remoto
- **No** reemplaza el modo 100% local

### Add-on LLM cloud (opt-in)

- Resumen / flashcards vía API externa con key en `.env`
- Claramente opcional; el default sigue siendo local

---

## Fuera de alcance (por ahora)

- Editar timestamps a mano en el editor (solo texto de segmento)
- Historial/undo de ediciones en disco
- App móvil nativa
- Integración directa con Zoom SDK (preferimos loopback)

---

## Cómo elegir el próximo slice

1. ¿Se puede usar sin la feature siguiente? → sí, priorizar.
2. ¿Rompe local-first o mete vendor lock? → diferir.
3. ¿Desbloquea estudio (merge clase / outline) o distribución (exe)? → subir prioridad.

**Orden sugerido actual:** `v0.3 merge clase` → `v0.4 estudio local` → `v0.5 realtime` → `v1.0 exe/LAN`.
