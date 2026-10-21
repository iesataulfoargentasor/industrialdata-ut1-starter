"""Pruebas del andamiaje; NO son pruebas de aceptación del proyecto."""
import tempfile
from pathlib import Path
import psycopg
import pytest
from streamlit.testing.v1 import AppTest
from industrialdata.config import data_root

pytestmark = pytest.mark.infra


def test_database_connection():
    with psycopg.connect(connect_timeout=10) as connection:
        assert connection.execute('SELECT current_database()').fetchone()[0]


def test_persistent_folder_writable():
    folder = data_root(); folder.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='infra_', dir=folder) as temporary:
        file = Path(temporary)/'probe.txt'
        file.write_text('infraestructura', encoding='utf-8')
        assert file.read_text(encoding='utf-8') == 'infraestructura'


def test_empty_dashboard():
    app = AppTest.from_file('/app/dashboard/app.py').run(timeout=20)
    assert not app.exception
    assert len(app.tabs) == 3
    assert 'todavía no hay resultados' in app.info[0].value
