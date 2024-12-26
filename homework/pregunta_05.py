"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

x = open("files/input/data.csv", "r").readlines()
x = [linea.strip().split("\t") for linea in x]

def pregunta_05():
    tupla=list(set(linea[0] for linea in x))
    tupla= [(linea,max([int(n[1]) for n in x  if n[0] == linea]),min([int(n[1]) for n in x if n[0] == linea])) for linea in tupla]
    return(sorted(tupla))
print(pregunta_05())
