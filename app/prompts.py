from __future__ import annotations

PROMPT_TEMPLATES: dict[str, dict[str, str]] = {
    "general": {
        "label": "General (español)",
        "prompt": "Transcripción en español de audio hablado, con puntuación clara.",
    },
    "lenguajes": {
        "label": "Lenguajes de programación",
        "prompt": (
            "Clase universitaria de Lenguajes de programación en español. "
            "Temas: paradigma lógico y paradigma orientado a objetos. "
            "Términos frecuentes: Prolog, CLIPS, predicados, hechos, reglas, unificación, "
            "backtracking, resolución, cláusulas de Horn, consulta, variables, "
            "objetos, clases, herencia, polimorfismo, encapsulamiento, métodos, "
            "instancias, tipado, semántica, sintaxis, Smalltalk, Simula."
        ),
    },
    "mates": {
        "label": "Matemáticas",
        "prompt": (
            "Clase de matemáticas en español. Cuidar notación: teorema, lema, "
            "demostración, integral, derivada, matriz, vector, límite, serie."
        ),
    },
    "none": {
        "label": "Sin prompt",
        "prompt": "",
    },
}
