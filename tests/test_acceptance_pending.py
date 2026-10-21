"""Agenda visible de P01–P11. Sustituir cada caso por pruebas reales independientes."""
import pytest

CASES = [
    'P01_arranque_completo', 'P02_repeticion', 'P03_reconciliacion',
    'P04_integracion', 'P05_escenarios', 'P06_datos_tardios',
    'P07_energia', 'P08_denominadores', 'P09_persistencia',
    'P10_formatos_y_motores', 'P11_fallo_controlado',
]


@pytest.mark.aceptacion
@pytest.mark.parametrize('case', CASES)
def test_acceptance_to_implement(case):
    pytest.skip(f'{case}: el equipo debe implementar el caso y su resultado esperado independiente')
