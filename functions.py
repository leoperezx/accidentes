# VARIABLES

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
