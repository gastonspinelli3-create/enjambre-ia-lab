"""ENJAMBRE IA LAB v0.1: experimento local reproducible, sin APIs externas."""
import json
from datetime import datetime, timezone
from pathlib import Path

MEMORIA = Path('memoria.jsonl')


def explorador(hipotesis):
    return {'agente': 'explorador', 'hipotesis': hipotesis,
            'propuesta': 'Buscar una fuente primaria y definir una prueba observable.',
            'estado': 'PENDIENTE'}


def verificador(resultado):
    return {'agente': 'verificador', 'observacion': 'No se aportaron fuentes ni pruebas externas.',
            'evidencia_confirmada': False, 'estado': 'PENDIENTE'}


def evaluador(exploracion, verificacion):
    return {'agente': 'evaluador', 'estado': 'PENDIENTE',
            'proximo_paso': 'Agregar una fuente verificable y repetir el experimento.',
            'mejora_validada': False}


def ejecutar(hipotesis):
    if not hipotesis.strip():
        raise ValueError('La hipótesis no puede estar vacía')
    a = explorador(hipotesis)
    b = verificador(a)
    c = evaluador(a, b)
    registro = {'fecha_utc': datetime.now(timezone.utc).isoformat(),
                'version': '0.1', 'explorador': a, 'verificador': b, 'evaluador': c}
    with MEMORIA.open('a', encoding='utf-8') as archivo:
        archivo.write(json.dumps(registro, ensure_ascii=False) + '\n')
    return registro


if __name__ == '__main__':
    print('ENJAMBRE IA LAB v0.1 — simulación sin modelos conectados')
    hipotesis = input('Escribí una hipótesis para investigar: ')
    print(json.dumps(ejecutar(hipotesis), ensure_ascii=False, indent=2))
    print(f'Registro guardado en {MEMORIA}')
