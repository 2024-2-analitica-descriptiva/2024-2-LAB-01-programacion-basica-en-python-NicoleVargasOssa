"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


x = open("files/input/data.csv", "r").readlines()
def pregunta_01():
    return sum(int(linea.strip().split("\t")[1]) for linea in x)
    
print(pregunta_01())
 
    
   