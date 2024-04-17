import streamlit as st
import pandas as pd

st.set_page_config(
    page_title= "Quotations_project",
    layout= "wide"
)

columna_logo = st.columns(3)
with columna_logo[2]:
    st.image('logo clinica.png')

st.header(body = "", divider='blue')