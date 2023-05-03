import streamlit as st
import streamlit.components.v1 as components
import pandas as pd 
import functions as fn




# streamlit run https://github.com/leoperezx/accidentes/streamlit_app.py

APP_TITLE = "Reporte de accidentes vehículares de Palmira - 2020."
APP_SUBTITLE = "Fuente: Datos abiertos, Alcaldía de Palmira."
APP_SUBTITLE_MAP ="Mapa de todos los accidentes registrados de Palmira - 2020."

# LOAD DATA

df = pd.read_csv("data/Accidentes_de_transito_Palmira_2020.csv")

# Clear Data
# Los datos de latitud y longitud están sin formato y escritos como 
# números enteros con puntos de cifras de mil.
df_geo = df[["LAT","LONG"]]
# Cambio de la dfrmación - Correcciones
df_geo = fn.darFormatoGeo( fn.limpiarPunto( df_geo ).astype(int) ) 

# Cambio de nombre a las columnas para un mejor manejo en con Folium.
# print(df.columns) # Columnas antes de renombrarlas
df.rename(columns={'BARRIOS-COREGIMIENTO- VIA':'BARRIOS_CORREGIMIENTO_VIA',
                   'CONDICION DE LA VICTIMA':'CONDICION_DE_LA_VICTIMA',
                   'CLASE DE SINIESTRO':'CLASE_DE_SINIESTRO',
                   'CLASE VEHICULO':'CLASE_DE_VEHICULO',
                   'TIPO DE SERVICIO':'TIPO_DE_SERVICIO'}, inplace = True)
# print(df[["LAT","LONG"]])
# print(df.columns) # columnas después de renombrarlas

# LOAD DATA CLEAR
df[["LAT","LONG"]] = df_geo # reemplazamos las columnas después de "limpiarlas"

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    
    # bootstrap 4 collapse example
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <h5>
        El actual reporte es realizado con la información suministrada por la secretaría de transito y transporte de la ciudad de Palmira, 
        Valle, Colombia. Los datos sin procesar los puede encontrar <a href="https://www.datos.gov.co/Transporte/Accidentes-de-transito-Palmira-2020/mg8y-amuh">aquí</a>.
        Página oficial de "Datos abiertos" del gobierno de Colombia. 
        </h5>
        <br>
        <h5>
        El siguiente trabajo es un proyecto en proceso. Lo que quiere decir que es autónomo, no esta terminado, no es oficilal 
        y es realizado a modo de práctica para el análisis de datos de forma autodidacta. Además, se estudia la programación 
        de diferentes lenguajes, incluyendo varios framewokrs de forma autonoma utilizando solo el uso de Internet. 
        </h5>
        <br>
        <h5>
        El primer paso fue tomar todo el dataset, leerlo y revisarlo. A continuación, se presenta el enlace que lleva a un archivo 
        compartido de <a href="https://docs.google.com/spreadsheets/d/1Sjc3ELm89rNrAvtS5oZVNVF0ATXw8bG5O06IX_P2kGE/edit?usp=sharing">Google Sheets</a>
        donde se realiza un resumen y algunas operaciones a los datos de la secretaría con algunas tablas dinámicas para hacer algúnos análisis. 
        </h5>
        """,
        height=400,
    )
    st.title("Presentación de los Datos")

    st.write("Dimenciones del dataset: ",df.shape)

    st.write(df.head(10))
    

    # DISPLAY METRICS No module named 'streamlit_folium'

if __name__=="__main__":
    main()
    
    st.text('Código del mapa interactivo')
    # components.html(
    #     """
    #     <iframe src="./map.html" height="600" width="600" title="Iframe Example"></iframe>

    #     """,width=600,height=600)

    # https://www.google.com/maps/d/edit?mid=1llROdOHQaUo4zKZyqCeKF9jey08hdss&usp=sharing

    with st.echo():
        
        from streamlit_folium import folium_static
        import folium
        
        # tiles: propiedad para cambiar el estilo del mapa.
        some_map = folium.Map(location=(3.535513,-76.297656),tiles="cartodbpositron", zoom_start=10)

        
        for row in df.itertuples():
            iframe = folium.IFrame("<body style=font-family:'sans-serif'>Choque de vehículo tipo: " + 
                                    row.CLASE_DE_VEHICULO +"<br>" +
                                    row.GRAVEDAD)
            
            pop_up = folium.Popup(iframe, min_width=200, max_width=200)

            some_map.add_child(folium.Marker(location=[row.LAT,row.LONG], popup=pop_up, icon=folium.Icon(color="red")))

        folium_static(some_map)
    
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <h6>
        * Si das <strong>click</strong> sobre uno de los puntos, se muetra más información. 
        </h6>
        <br>
        <h5> 
        Quedo atento a comentarios, preguntas, dudas, críticas "constructivas", felicitaciones, ayuda y apoyo tanto en 
        ideas para análisis como laboral. 
        </h5>
        <h5>
        Todavía exisite mucha información sin analizar, muchas operaciones a realizar y funciones por aprender. 
        Programo mientras aprendo, así que ... <strong>ten paciencia</strong>. 
        </h5>      
        <br>
        <p>&copy; 2023 | Github: <a href="https://github.com/leoperezx">leoperezx</a>  | Twitter: <a href="https://twitter.com/leoperezx">@leoperezx</a></p> 
        """,height=300,
    )

  

