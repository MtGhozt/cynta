from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLASSES_DIR = ROOT / "Clases"
OUTPUT_DIR = ROOT / "Transcripciones"

COURSE_NAME = "Lenguajes de programación"
COURSE_TOPICS = ["paradigma lógico", "orientado a objetos"]

# Helps Whisper spell course-specific terms more consistently.
INITIAL_PROMPT = (
    "Clase universitaria de Lenguajes de programación en español. "
    "Temas: paradigma lógico y paradigma orientado a objetos. "
    "Términos frecuentes: Prolog, predicados, hechos, reglas, unificación, "
    "backtracking, resolución, cláusulas de Horn, consulta, variables, "
    "objetos, clases, herencia, polimorfismo, encapsulamiento, métodos, "
    "instancias, tipado, semántica, sintaxis."
)

DEFAULT_MODEL = "large-v3"
DEFAULT_LANGUAGE = "es"
DEFAULT_DEVICE = "cuda"
DEFAULT_COMPUTE_TYPE = "float16"
FALLBACK_MODEL = "medium"
FALLBACK_DEVICE = "cpu"
FALLBACK_COMPUTE_TYPE = "int8"

BEAM_SIZE = 5
VAD_FILTER = True
# Avoid Whisper getting stuck repeating filler ("Pero...", etc.).
CONDITION_ON_PREVIOUS_TEXT = False
COMPRESSION_RATIO_THRESHOLD = 2.0
LOG_PROB_THRESHOLD = -0.8
NO_SPEECH_THRESHOLD = 0.6
