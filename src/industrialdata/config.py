"""Configuración de infraestructura, sin reglas de negocio."""
import os
from pathlib import Path


def data_root():
    return Path(os.environ.get('DATA_ROOT', '/data'))
