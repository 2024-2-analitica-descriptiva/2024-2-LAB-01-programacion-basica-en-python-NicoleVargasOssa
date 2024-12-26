"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    x = open("files/input/data.csv", "r").readlines()
    x = [linea.strip().split("\t")[4] for linea in x]

    diccionario = {}

    for linea in x:
        lista = linea.split(",")

        for dupla in lista:
            clave, valor = dupla.split(":")
            if clave in diccionario:
                diccionario[clave] += 1
            else:
                diccionario[clave] = 1

    dicc = dict(sorted(diccionario.items()))

    return dicc

print(pregunta_09())

"""
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
