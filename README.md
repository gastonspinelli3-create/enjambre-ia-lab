# Enjambre IA Lab — v0.1

Prototipo experimental de tres roles: explorador, verificador y evaluador.

**Importante:** en esta versión los roles son funciones deterministas de Python, no modelos de inteligencia artificial. No navegan internet ni se conectan a Claude o ChatGPT. Su objetivo es validar la estructura de ejecución y la memoria antes de añadir APIs.

## Ejecutar

Requiere Python 3.9 o superior, sin dependencias externas.

```bash
python enjambre.py
```

Ingresá una hipótesis. El programa mostrará el resultado de los tres roles y agregará una línea JSON al archivo `memoria.jsonl`.

## Próximo experimento

Conectar un modelo autorizado al explorador, exigir evidencia verificable y comparar resultados contra una prueba de referencia. No guardar claves API en el repositorio.
