import streamlit as st

# streamlit run https://github.com/leoperezx/accidentes/streamlit_app.py

APP_TITLE = "Reporte de accidentes vehículares de Palmira - 2020."
APP_SUBTITLE = "Fuente: Datos abiertos, Alcaldía de Palmira."

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)

# LOAD DATA

# DISPLAY FILTERS AND MAPS

# DISPLAY METRICS

if __name__=="__main__":
    main()