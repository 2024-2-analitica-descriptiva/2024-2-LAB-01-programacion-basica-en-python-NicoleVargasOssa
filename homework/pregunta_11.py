"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


x = open("files/input/data.csv", "r").readlines()

def pregunta_11():
    diccionario = {}
    for linea in x:
        sublistas = linea.strip().split("\t")
        columna2 = int(sublistas[1]) 
        
        columna4 = sublistas[3].split(",")  
        for i in columna4:
            if i in diccionario:
                diccionario[i] += columna2
            else:
                diccionario[i] = columna2

    dicc = dict(sorted(diccionario.items()))
    return dicc

print(pregunta_11())

"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
