import os
import sys

def read_file(f):

    list_Points = []

    n_graphPoints = int(f.readline())

    i = 0
    while i < n_graphPoints:

        linea = f.readline().rstrip('\n').split(" ")
        tupla = (round(float(linea[0]), 1), round(float(linea[1]), 1))
        list_Points.append(tupla)
        i += 1
    return n_graphPoints, list_Points

if __name__ == '__main__':


    name_fich = input("Introduce el nombre(ruta) del fichero: ")

    if not os.path.isfile(name_fich):
        print("El parametro introducido(", name_fich, ") no es un fichero.")
        exit(0)

    file = open(name_fich, "r")
    info = read_file(file)
    n_graphPoint = info[0]
    list_Ponits = info[1]


    print(f"El num de puntos es:{n_graphPoint}")
    print(f"Los puntos son: \n {list_Ponits}")

    '''

    #Creamos una lista donde guardaremos las coordenadas de los puntos
    list_Points = []
    #Convertimos el fichero en una lista de líneas
    lineas = sys.stdin.readlines()
    #Obtenemos el número de puntos del grafo
    n_graphPoints = int(lineas[0])
    #Obtenemos las coordenadas de los puntos
    i = 0
    while i < n_graphPoints:
        linea = lineas[1 + i].rstrip('\n').split(" ")
        tupla = (round(float(linea[0]), 1), round(float(linea[1]), 1))
        list_Points.append(tupla)
        i += 1

 '''
