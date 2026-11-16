# Cynta

Transcriptor **local-first** para audio/video (clases, Zoom grabado, lo que sea) en tu PC con [faster-whisper](https://github.com/SYSTRAN/faster-whisper).

- UI en `http://127.0.0.1:8765` (drag & drop)
- Cola de jobs, progreso, export MD / JSON / SRT
- GPU NVIDIA si está disponible (probado con RTX 4060); si no, CPU

Repo público: [MtGhozt/cynta](https://github.com/MtGhozt/cynta)

## Requisitos

| Pieza | Notas |
|-------|--------|
| Windows 10/11 | También corre en otras plataformas con ajustes |
| Python **3.11** | [python.org](https://www.python.org/downloads/) — marcá *Add to PATH* |
| ffmpeg | `winget install Gyan.FFmpeg` y **reabrí** la terminal |
| GPU NVIDIA (opc.) | Drivers recientes; sin GPU usá `device=cpu` |

## Arranque (recomendado)

Doble clic en `run.bat`, o en PowerShell:

```powershell
cd C:\ruta\a\cynta   # o Transcripciones
.\run.ps1
```

El script:

1. Chequea Python 3.11, ffmpeg y GPU
2. Instala deps solo si faltan (`-Install` para forzar)
3. Levanta el server y abre el browser cuando `/api/health` responde

Opciones:

```powershell
.\run.ps1 -SkipInstall   # no toca pip
.\run.ps1 -Install       # reinstala requirements.txt
.\run.ps1 -Port 8765
```

En la UI, el badge arriba a la derecha dice **cuda** o **cpu**. Si falta ffmpeg/CUDA, aparece un aviso.

## Instalación manual

```powershell
py -3.11 -m pip install -r requirements.txt
py -3.11 -m uvicorn app.main:app --host 127.0.0.1 --port 8765
```

Abrí `http://127.0.0.1:8765`.

## CUDA — si la GPU no aparece

1. `nvidia-smi` en una terminal → tiene que listar la placa.
2. Reinstalá wheels CUDA de pip:

   ```powershell
   py -3.11 -m pip install -r requirements.txt
   ```

   Incluye `nvidia-cublas-cu12`, `nvidia-cudnn-cu12`, `nvidia-cuda-runtime-cu12`.
3. En Cynta, Device = `cuda` (o `auto`). Si sigue fallando, usá `cpu` + modelo `medium`/`small`.
4. Primera corrida con `large-v3` descarga ~3 GB del modelo.

El health endpoint reporta el diagnóstico:

```text
GET /api/health → ffmpeg, cuda.gpu, cublas_wheels, recommended_device, warnings
```

## Uso rápido

1. Soltá uno o varios `.m4a` / `.mp3` / `.wav` o `.mp4` / `.mkv` / `.webm`  
   (varios archivos bajo el mismo nombre = una **clase** con timeline continuo)
2. Elegí idioma / modelo / device / dominio
3. **Transcribir** → mirá la cola a la derecha (en clases: progreso Parte k/n)
4. **Guardar en** → carpeta de salida (picker nativo en Windows)

### Cola: Ver / Editar / descargas

| Acción | Qué hace |
|--------|----------|
| **Ver** | Preview markdown solo lectura (cerrá con otra vez Ver o **Cerrar**) |
| **Editar** | Segmentos editables → **Guardar** regenera MD / JSON / SRT |
| **MD / JSON / SRT** | Descarga el archivo |
| **Carpeta** | Abre la carpeta del job |
| **Rehacer** | Vuelve a encolar el mismo audio |

Fuente de verdad al editar: `segmentos.json`. El markdown se regenera al guardar (no se edita a mano en la UI).

Salidas por job (también en la carpeta del job):

- `transcripcion.md`
- `segmentos.json`
- `subtitulos.srt`

## CLI de clases (curso)

```powershell
py -3.11 transcribe_batch.py --clase 1
py -3.11 transcribe_batch.py          # todas; salta las ya hechas
```

Entrada: `Clases/Clase N/audio*.m4a` (varios audios se unen con offsets)  
Salida: `Transcripciones/Clase N/`

## API local

| Método | Ruta | Uso |
|--------|------|-----|
| GET | `/api/health` | entorno: ffmpeg, CUDA, warnings |
| GET | `/api/meta` | modelos, idiomas, prompts |
| GET | `/api/jobs` | historial |
| POST | `/api/jobs` | multipart upload (`file` o `files` × N) |
| GET/PUT | `/api/jobs/{id}/segments` | leer / editar segmentos (regenera MD+SRT) |
| WS | `/ws/jobs/{id}` | progreso |
| GET | `/api/jobs/{id}/files/{md\|json\|srt}` | descargas |

## Arquitectura

```
UI (static) → FastAPI → cola (thread) → ffmpeg (si video) → faster-whisper → SQLite + files
```

- [`app/main.py`](app/main.py) — API + WebSocket
- [`app/envcheck.py`](app/envcheck.py) — health / preflight
- [`app/worker.py`](app/worker.py) — cola
- [`transcribe/engine.py`](transcribe/engine.py) — ASR
- [`transcribe/export.py`](transcribe/export.py) — MD/JSON/SRT + rewrite al editar
- [`run.ps1`](run.ps1) / [`run.bat`](run.bat) — launcher Windows

## Roadmap

Versiones, criterios de “listo” y orden sugerido: **[`ROADMAP.md`](ROADMAP.md)**.

Resumen:

| Versión | Foco |
|---------|------|
| **Hecho (≤0.3)** | Batch + UI Cynta + editor + merge multi-archivo (clase) |
| **v0.4** | Outline / flashcards **locales** (Ollama; sin API paga) |
| **v0.5** | Realtime (mic / loopback WASAPI) |
| **v1.0** | `.exe` + modo LAN |
| **Después** | Slides/OCR, multi-usuario, LLM cloud opt-in |

## Notas

- `Clases/` y `data/` no van al git (medios / runtime local).
- Cancelar el picker de carpeta no es error; el diálogo usa Explorer moderno en Windows.
