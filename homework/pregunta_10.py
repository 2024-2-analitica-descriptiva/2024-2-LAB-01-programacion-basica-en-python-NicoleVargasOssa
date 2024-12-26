"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


x = open("files/input/data.csv", "r").readlines()
def pregunta_10():
    tupla = []  # Inicializar la lista vacía
    for linea in x:
        sublistas = linea.strip().split("\t")
        columna1 = sublistas[0]
        columna4 = len(sublistas[3].split(","))
        columna5 = len(sublistas[4].split(","))

        tupla.append((columna1, columna4, columna5))
    return tupla

print(pregunta_10())

"""
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
