"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


x = open("files/input/data.csv", "r").readlines()
x = [linea.strip().split("\t") for linea in x]

def pregunta_12():
    diccionario = {}

    for linea in x:
        columna1 = linea[0]  
        columna5 = linea[4]  
        valores = columna5.split(",")  
        suma = sum(int(v.split(":")[1]) for v in valores)  
    
        if columna1 not in diccionario:
            diccionario[columna1] = 0
        diccionario[columna1] += suma 

    dicc = dict(sorted(diccionario.items()))
    return dicc 

print(pregunta_12())


"""
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
