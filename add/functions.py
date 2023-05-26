

def generarMapa(data,options):
    '''
    Organiza la información de la base de datos para dibujar en un mapa 
    cada uno de los puntos georeferenciados para ubicar cada uno de los 
    accidentes registrados en el año 2020 en Palmira. 

    lista disponible de atributos de la base de datos son:
    GRAVEDAD,
    FECHA,
    AÑO,
    HORA,
    JORNADA,
    DIA_SEMANA,
    BARRIOS_CORREGIMIENTO_VIA,
    DIRECCION,
    ZONA,
    AUTORIDAD,
    LAT,
    LONG,
    HIPOTESIS,
    CONDICION_DE_LA_VICTIMA,
    CLASE_DE_SINIESTRO,
    LESIONADO,
    HOMICIDIOS,
    CLINICA,
    SITIO,
    CLASE_DE_VEHICULO,
    MARCA,
    MATRICULA,
    TIPO_DE_SERVICIO,
    EMPRESA,,

    '''
           
    from streamlit_folium import folium_static
    import folium

    data_filter = data.loc[data['CLASE_DE_VEHICULO'].isin(options)] 

    some_map = folium.Map(location=(3.535513,-76.297656),tiles="cartodbpositron", zoom_start=10)

    tool_tip="Click me!"    


    for row in data_filter.itertuples():
        pop_up=("<p>Choque de vehículo tipo: " + row.CLASE_DE_VEHICULO +"</p>" +
                    "<p>Nivel de gravedad:" + row.GRAVEDAD + "</p>" + 
                    "<p>Hipótesis del accidente:" + row.HIPOTESIS + "</p>")
        
        folium.Marker([row.LAT,row.LONG], popup=pop_up, tooltip=tool_tip, icon=folium.Icon(color='#F1F2F6',icon_color='#FFABAB')).add_to(some_map)

    return folium_static(some_map)
