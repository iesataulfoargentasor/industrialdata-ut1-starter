"""Interfaz del proceso ordinario. H3–H4: implementar sin depender de notebooks."""
import argparse
import sys
from pathlib import Path
from .config import data_root


def execute(input_folder, output_root):
    """TODO: coordinar ingesta, calidad, análisis, registro y publicación.

    Una ejecución incompleta no debe sustituir resultados válidos. Definid cómo
    resolver repetición, lotes tardíos, conflictos y fallos antes de programarlo.
    """
    raise NotImplementedError('H3–H4 pendientes: implementar execute() y las pruebas P01–P11.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=data_root()/'raw')
    parser.add_argument('--output', type=Path, default=data_root())
    args = parser.parse_args()
    try:
        execute(args.input, args.output)
    except NotImplementedError as error:
        print(str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
