# 

def limpiarPunto(df):
    '''
    Transforma los números en texto y elimia los puntos 
    que denotan las cifras de mil. 
    '''
    rango = len(df.index)
    columnas = df.columns
    
    for j in range(len(columnas)):
        for i in range(rango):
            df[columnas[j]][i] = str(df[columnas[j]][i]).replace('.','')
    
    return df


def cantidadDeDigitos(num):
    '''
    Devuelve la cantidad de cifras de un número. 
    
    ej. >>> cantidadDeDigitos(9876) = 4
    '''
       
    count=0
    num=abs(num)
    while(num>0):
        count=count+1
        num=num//10
    return count


def darFormatoGeo(df):
    '''
    Da formato a los números en las columnas LAT y LONG.

    - Combierte los números de 4, 5 y 6 cifras de la columna de LAT
    a formato de georeferencia de la librería Folium LAT ( #.##### ).

    - Combierte los números de 5, 6 y 7 cifras de la columna de LONG
    a formato de georeferencia de la librería Folium LONG ( -##.##### ).
    '''
    rango = len(df.index)
    for i in range(rango):   
        # es de cuatro cifras pero debe ser de 6 (#.###00)
        if cantidadDeDigitos(df.LAT[i]) == 4:
            df.LAT[i] = (df.LAT[i]*100)/100000
           
        # es de cinco cifras pero debe ser de 6 (#.####0)
        if cantidadDeDigitos(df.LAT[i]) == 5:
            df.LAT[i] = (df.LAT[i]*10)/100000
           
        else:
            df.LAT[i] = df.LAT[i]/100000
        
    for j in range(rango):  
        # es de cinco cifras pero debe ser de 7 (-##.###00)
        if cantidadDeDigitos(df.LONG[j]) == 5:
            df.LONG[j] = (df.LONG[j]*100)/100000
            
        # es de seis cifras pero debe ser de 7 (-##.####0)
        if cantidadDeDigitos(df.LONG[j]) == 6:
            df.LONG[j] = (df.LONG[j]*10)/100000
           

        else:
            df.LONG[j] = df.LONG[j]/100000

    return df

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
        
        folium.Marker([row.LAT,row.LONG], popup=pop_up, tooltip=tool_tip, icon=folium.Icon(color='black',icon_color='#FFFF00')).add_to(some_map)

    return folium_static(some_map)
