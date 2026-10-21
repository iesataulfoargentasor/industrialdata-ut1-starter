"""Comprueba conexión SQL y almacenamiento. No ejecuta la práctica."""
import json
import psycopg
from industrialdata.config import data_root

folder = data_root()
for name in ['raw', 'silver', 'gold', 'quarantine', 'reports']:
    (folder/name).mkdir(parents=True, exist_ok=True)
with psycopg.connect(connect_timeout=10) as connection:
    assert connection.execute('SELECT 1').fetchone()[0] == 1
    version = connection.execute('SHOW server_version').fetchone()[0]
print(json.dumps({'infrastructure': 'OK', 'postgres': version, 'data_root': str(folder),
                  'project': 'Pendiente: generador, modelo, pipeline, panel y aceptación'}, ensure_ascii=False))
