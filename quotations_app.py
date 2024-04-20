import streamlit as st
import pandas as pd

st.set_page_config(
    page_title= "Quotations_project",
    layout= 'wide'
)

from streamlit.components.v1 import html

# Insertar CSS para mejorar la impresión
css_to_inject = """
<style>
@media print {
    html, body {
        width: 210mm;
        height: 297mm;
    }
    .reportview-container .main .block-container {
        max-width: 210mm;
        padding: 20mm;
    }
    .reportview-container .main {
        color: black; /* Cambia el color de la fuente para la impresión si es necesario */
    }
    /* Aquí puedes añadir estilos específicos para la impresión */
}
</style>
"""

# Inyectar el CSS en la app
html(css_to_inject)


columna_logo = st.columns((0.7,0.3))
with columna_logo[1]:
    st.image('logo clinica.png')

st.header(body = "", divider='blue')

df = pd.DataFrame()

# Ahora genero las variables que serán ingresadas por el usuario al momento de generar el presupuesto.

columnas_para_datos_iniciales = st.columns((0.5,0.5))

with columnas_para_datos_iniciales[0]:
    presupuesto_estimado = st.text_input(
        "**Presupuesto Estimado NO.**",
        value = None
        )
    
with columnas_para_datos_iniciales[1]:
    fecha_de_presupuesto = st.date_input(
        "**Fecha de Presupuesto**", 
        value = "today"
        )

with columnas_para_datos_iniciales[0]:
    nombre_de_paciente = st.text_input(
        "**Nombre de Paciente**",
        value = None
        )
    
with columnas_para_datos_iniciales[1]:
    indentificacion_de_paciente = st.text_input(
        "**Identificación de Paciente**",
        value = None
        )

#medico = st.selectbox(
#    label = "Medico",
#    options = df.medico.unique(),
#    label_visibility = "hidden"
#)
#procedimiento = st.selectbox(
#    label = "Medico",
#    options = df2.procedimiento.unique(),
#    label_visibility = "hidden"
#)


# Botón para imprimir la página (ejecuta un script de JavaScript para imprimir la página)
st.button("Imprimir Reporte", on_click=lambda: html("<script>window.print()</script>", height=0))