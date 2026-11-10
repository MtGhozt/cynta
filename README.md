# Transcripciones de clases

Transcribe los audios de `Clases/Clase N/audio*.m4a` a Markdown + JSON listos para estudiar con IA.

Curso: **Lenguajes de programación** (paradigma lógico y orientado a objetos).

## Requisitos

- Python 3.11+
- [ffmpeg](https://ffmpeg.org/) en el PATH
- GPU NVIDIA recomendada (RTX 4060 ok)

```powershell
py -3.11 -m pip install -r requirements.txt
```

En Windows, `requirements.txt` incluye las DLLs CUDA (`cublas`/`cudnn`) que CTranslate2 necesita para GPU. El script las agrega al PATH solo.

## Uso

Probar solo la Clase 1:

```powershell
py -3.11 transcribe_batch.py --clase 1
```

Transcribir todas las clases (omite las que ya tengan `segmentos.json` + `transcripcion.md`):

```powershell
py -3.11 transcribe_batch.py
```

Forzar re-transcripción:

```powershell
py -3.11 transcribe_batch.py --force
```

También generar subtítulos `.srt`:

```powershell
py -3.11 transcribe_batch.py --clase 1 --srt
```

CPU (si CUDA falla):

```powershell
py -3.11 transcribe_batch.py --clase 1 --device cpu --model medium --compute-type int8
```

## Salida

```
Transcripciones/
  Clase 1/
    transcripcion.md   # frontmatter + párrafos con [HH:MM:SS]
    segmentos.json     # segmentos crudos para IA / RAG
    subtitulos.srt     # opcional con --srt
```

## Notas

- Se usa el `.m4a`, no el `.mp4` (mismo audio, más liviano).
- Modelo por defecto: `large-v3` en CUDA `float16`, con fallback automático.
- La primera corrida descarga el modelo (~3 GB).
- **Clase 1 (prueba OK):** ~98 min de audio → ~48 min en RTX 4060 (`large-v3`, RTF ~0.49).
- Para el resto (2–7), sin rehacer la 1:

```powershell
py -3.11 transcribe_batch.py
```

  Eso omite clases que ya tengan `transcripcion.md` + `segmentos.json`. Estimación orientativa: ~40–50 min wall por clase de ~1.5 h de audio.
