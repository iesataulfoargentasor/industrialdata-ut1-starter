"""Interfaz del simulador. H2: implementar el generador y sus contratos."""
import argparse
import sys
from pathlib import Path
from .config import data_root


def generate(*, output, seed, scenario, machines, minutes):
    """Crear las cuatro fuentes y el manifiesto según el enunciado.

    TODO: reproducibilidad, escenarios, identidad de eventos y conservación de raw.
    Cada alumno debe decidir el modelo, los parámetros y las muestras de referencia.
    """
    raise NotImplementedError('H2 pendiente: implementar generate() y sus pruebas.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--scenario', default='demo')
    parser.add_argument('--machines', type=int, default=6)
    parser.add_argument('--minutes', type=int, default=1440)
    parser.add_argument('--output', type=Path, default=data_root()/'raw')
    args = parser.parse_args()
    try:
        generate(**vars(args))
    except NotImplementedError as error:
        print(str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
