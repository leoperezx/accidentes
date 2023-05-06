import streamlit as st
import streamlit.components.v1 as components
import pandas as pd 
import add.functions as fn
from PIL import Image

# streamlit run https://github.com/leoperezx/accidentes/streamlit_app.py
IMAGE = Image.open('add/img-map.jpg')
APP_TITLE = "Reporte de accidentes vehículares de Palmira - 2020."
APP_SUBTITLE = "Fuente: Datos abiertos, Alcaldía de Palmira."
APP_SUBTITLE_MAP ="Mapa de todos los accidentes registrados de Palmira - 2020."
APP_INTRO = "El actual reporte es realizado con la información suministrada por la secretaría de transito y transporte de la ciudad de Palmira, Valle, Colombia. Los datos sin procesar los puede encontrar [aquí](https://www.datos.gov.co/Transporte/Accidentes-de-transito-Palmira-2020/mg8y-amuh). Página oficial de 'Datos abiertos' del gobierno de Colombia. <br><br>El siguiente trabajo es un proyecto en proceso. Lo que quiere decir que es autónomo, no esta terminado, no es oficilal y es realizado a modo de práctica para el análisis de datos de forma autodidacta. Además, se estudia la programación de diferentes lenguajes, incluyendo varios framewokrs de forma autonoma utilizando solo el uso de Internet. <br><br>El primer paso fue tomar todo el dataset, leerlo y revisarlo. A continuación, se presenta el enlace que lleva a un archivo compartido de [Google Sheets](https://docs.google.com/spreadsheets/d/1Sjc3ELm89rNrAvtS5oZVNVF0ATXw8bG5O06IX_P2kGE/edit?usp=sharing) donde se realiza un resumen y algunas operaciones a los datos de la secretaría con algunas tablas dinámicas para hacer algúnos análisis."
APP_FINAL = "Quedo atento a comentarios, preguntas, dudas, críticas constructivas, felicitaciones, ayuda y apoyo tanto en ideas para análisis como laboral<br><br>Todavía exisite mucha información sin analizar, muchas operaciones a realizar y funciones por aprender. Programo mientras aprendo. Veras muchos cambios. **Esto es de prueba y error**."

df = pd.read_csv("add/dataset.csv")



def main():
    
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    st.markdown(APP_INTRO,unsafe_allow_html=True)
    st.title("Presentación de los Datos")
    st.write("Dimenciones del dataset (filas, columnas): ",df.shape)
    st.write(df.head(10))
    st.subheader("Mapa interactivo de los accidentes - Palmira 2020")
    if st.button("Crear mapa"):
        fn.generarMapa(df)
    else: 
        st.image(IMAGE, width=600, caption="Imagen provicional")
    st.markdown(APP_FINAL, True)


if __name__=="__main__":
    main()
