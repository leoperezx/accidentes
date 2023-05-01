# VARIABLES

def limpiarPunto(df):
    rango = len(df.index)
    columnas = df.columns
    
    for j in range(len(columnas)):
        for i in range(rango):
            df[columnas[j]][i] = str(df[columnas[j]][i]).replace('.','')
    
    return df


def cantidadDeDigitos(num):
    # cantidad de cifras de un número    
    count=0
    num=abs(num)
    while(num>0):
        count=count+1
        num=num//10
    return count


def darFormatoGeo(df):
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
