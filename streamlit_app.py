import streamlit as st
import pandas as pd 
# streamlit run https://github.com/leoperezx/accidentes/streamlit_app.py

APP_TITLE = "Reporte de accidentes vehículares de Palmira - 2020."
APP_SUBTITLE = "Fuente: Datos abiertos, Alcaldía de Palmira."

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)

# LOAD DATA
df = pd.read_excel("https://github.com/leoperezx/accidentes/data/Accidentes_de_transito_Palmira_2020.xlsx")

st.write(df.shape)
st.write(df.head())
st.write(df.columns)
# DISPLAY FILTERS AND MAPS

# DISPLAY METRICS

if __name__=="__main__":
    main()