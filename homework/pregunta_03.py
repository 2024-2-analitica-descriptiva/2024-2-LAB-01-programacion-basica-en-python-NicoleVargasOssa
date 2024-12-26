"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

x = open("files/input/data.csv", "r").readlines()
x = [linea.strip().split("\t") for linea in x]
def pregunta_03():
    diccionario = {}

    for linea in x:
        clave = linea[0]
        valor = int(linea[1])

        if clave in diccionario:
            diccionario[clave] += valor
        else:
            diccionario[clave] = valor

    orden = sorted(diccionario.items())
    return orden
print(pregunta_03())
   
    
