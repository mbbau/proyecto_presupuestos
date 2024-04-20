import streamlit as st
import pandas as pd


st.set_page_config(
    page_title= "Quotations_project",
    layout= "wide"
)

columna_logo = st.columns((0.8,0.1))
with columna_logo[1]:
    st.image('logo clinica.png')

st.header(body = "", divider='blue')

df = pd.DataFrame(columns="medico")

# Ahora genero las variables que serán ingresadas por el usuario al momento de generar el presupuesto.

presupuesto_estimado = st.text_input(
    "Presupuesto Estimado",
    value = None, 
    label_visibility= "hidden"
    )

fecha_de_presupuesto = st.date_input(
    "Fecha de Presupuesto", 
    value = "today", 
    label_visibility= "hiden"
    )

nombre_de_paciente = st.text_input(
    "Nombre de Paciente",
    value = None, 
    label_visibility= "hidden"
    )

indentificacion_de_paciente = st.number_input(
    "Identificación de Paciente",
    placeholder = 999999999, 
    label_visibility= "hidden"
    )

#medico = st.selectbox(
#    label = "Medico",
#    options = df.medico.unique(),
#    label_visibility = "hidden"
#)
