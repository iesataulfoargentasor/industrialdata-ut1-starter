"""Panel inicial: estructura visual sin resultados ni lógica resuelta."""
import streamlit as st

st.set_page_config(page_title='IndustrialData · Inicio', page_icon='🏭', layout='wide')
st.title('IndustrialData')
st.caption('UT1 · Sistemas de Big Data · I.E.S. Ataulfo Argenta')
st.info('Panel inicial: todavía no hay resultados conectados. Cada alumno debe implementar las tres vistas y la lectura de publicaciones válidas.')
tabs = st.tabs(['Estado e incidencias', 'Producción y energía', 'Calidad y trazabilidad'])
prompts = [
    'H4: mostrar episodios y su evidencia; añadir filtros de máquina y periodo.',
    'H4: mostrar indicadores con unidad, periodo, cobertura y estados no evaluables.',
    'H3–H4: mostrar procedencia, ejecuciones, rechazos y cobertura de los datos.',
]
for tab, prompt in zip(tabs, prompts):
    with tab:
        st.write(prompt)
st.caption('Los datos del proyecto serán sintéticos. Esta pantalla no contiene indicadores calculados ni certifica que el pipeline esté implementado.')
