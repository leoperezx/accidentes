import streamlit as st
import pandas as pd 
import numpy as np
import functions as fn

# streamlit run https://github.com/leoperezx/accidentes/streamlit_app.py

APP_TITLE = "Reporte de accidentes vehículares de Palmira - 2020."
APP_SUBTITLE = "Fuente: Datos abiertos, Alcaldía de Palmira."

# LOAD DATA

df = pd.read_csv("data/Accidentes_de_transito_Palmira_2020.csv")

# Clear Data
df_geo = df[["LAT","LONG"]]

df_geo = fn.darFormatoGeo( fn.limpiarPunto( df_geo ).astype(int) ) 



# print(df[["LAT","LONG"]])

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)

    # LOAD DATA CLEAR
    df[["LAT","LONG"]] = df_geo

    st.write(df.shape)
    st.write(df.head())
    st.write(df.columns)
    # DISPLAY FILTERS AND MAPS

    # DISPLAY METRICS

if __name__=="__main__":
    main()