import streamlit as st
import pandas as pd

columna_logo = st.columns(3)
with columna_logo[2]:
    st.image('logo clinica.png')

st.header(divider='blue')