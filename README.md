# Transcriptor Local

Producto **local-first** para transcribir audio/video (clases, Zoom grabado, lo que sea) en tu PC con [faster-whisper](https://github.com/SYSTRAN/faster-whisper).

- UI en `http://127.0.0.1:8765` (drag & drop)
- CLI batch para carpetas de clases (`transcribe_batch.py`)
- GPU NVIDIA si está disponible (probado con RTX 4060)

Repo privado Cursor: `matias-b/transcripciones`  
(copia online no pública; en Windows el `git push` puede pedir `origin auth login`)

## Requisitos

- Windows 10/11 (también sirve en otras plataformas con ajustes)
- Python 3.11+
- [ffmpeg](https://ffmpeg.org/) en el PATH (`winget install Gyan.FFmpeg`)
- GPU NVIDIA recomendada (sin GPU: `--device cpu --model medium`, más lento)

## Arranque rápido (producto)

```powershell
cd C:\Programacion\Transcripciones
.\run.ps1
```

Se abre el navegador. Arrastrá `.m4a` / `.mp3` / `.wav` o `.mp4` / `.mkv` / `.webm`.

Salidas por job en `data/jobs/<id>/out/`:

- `transcripcion.md`
- `segmentos.json`
- `subtitulos.srt`

## CLI de clases (curso)

```powershell
py -3.11 -m pip install -r requirements.txt
py -3.11 transcribe_batch.py --clase 1
py -3.11 transcribe_batch.py          # todas; salta las ya hechas
```

Entrada: `Clases/Clase N/audio*.m4a`  
Salida: `Transcripciones/Clase N/`

## API local (extensible)

| Método | Ruta | Uso |
|--------|------|-----|
| GET | `/api/meta` | modelos, idiomas, prompts |
| GET | `/api/jobs` | historial |
| POST | `/api/jobs` | multipart upload |
| WS | `/ws/jobs/{id}` | progreso |
| GET | `/api/jobs/{id}/files/{md\|json\|srt}` | descargas |

Estos contratos están pensados para mañana poder apuntar la misma UI a un worker remoto / multi-usuario.

## Arquitectura

```
UI (static) → FastAPI → cola (thread) → ffmpeg (si video) → faster-whisper → SQLite + files
```

Código clave:

- [`app/main.py`](app/main.py) — API + WebSocket
- [`app/worker.py`](app/worker.py) — cola
- [`transcribe/engine.py`](transcribe/engine.py) — ASR
- [`transcribe/media.py`](transcribe/media.py) — audio/video

## Roadmap

### Hecho (v1)

- Drag & drop audio/video
- Cola + progreso + historial
- Export MD/JSON/SRT
- Plantillas de prompt (curso / mates / general)
- Abrir carpeta del job + búsqueda en preview

### v1.1

- Editor de transcript en UI
- Resumen / outline / flashcards (LLM aparte del ASR)
- Merge de varios archivos en una “clase”

### v1.5 — realtime

- Micrófono **o** loopback WASAPI (audio del sistema) mientras Zoom/Meet suena
- **No** requiere permiso del host de Zoom; es “transcribí lo que oigo”
- Calidad/latencia peores que batch; GPU ayuda

### v2

- Detección de diapositivas + OCR alineado a timestamps
- Empaquetado `.exe` (Tauri + sidecar Python)
- Modo LAN para compañeros en la misma WiFi

### Multi-usuario (después)

Misma API; agregar auth, object storage y cola server. La UI puede seguir igual.

## Notas

- Los medios en `Clases/` **no** van al git (muy pesados).
- `data/` es runtime local (también ignorado).
- Primera corrida descarga el modelo Whisper (~3 GB para `large-v3`).
