import os
import sys
import random
from math import sqrt

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo


def read_file(f):

    list_Points = []

    n_graphPoints = int(f.readline())

    i = 0
    while i < n_graphPoints:

        linea = f.readline().rstrip('\n').split(" ")
        tupla = (round(float(linea[0]), 2), round(float(linea[1]), 2))
        list_Points.append(tupla)
        i += 1
    return n_graphPoints, list_Points



def kruskal(graph :UndirectedGraph, edgeList ):
    res = []
    indicesPesosOrdenados = sorted(range(len(listaAristasPeso)), key=lambda i: listaAristasPeso[i])

    print(indicesPesosOrdenados)
    vertices = graph.V

    mfs = MergeFindSet()
    for i in  vertices:
        mfs.add(i)

    w = 0
    #Comprobacion de que no hay ciclos
    for i in indicesPesosOrdenados:
        u, v = edgeList[i]
        cu = mfs.find(u)
        cv = mfs.find(v)
        print(listaAristasPeso[i])
        if cu != cv:
            mfs.merge(u, v)
            res.append((u, v))
            w = w + listaAristasPeso[i]


    return res, w



def caulculoDistancia( listPoint, i, j ):

    v1x = listPoint[i][0]
    v1y = listPoint[i][1]
    v2x = listPoint[j][0]
    v2y = listPoint[j][1]

    distancia = sqrt( pow( (abs(v1x-v2x)) , 2) + pow( (abs(v1y-v2y)) , 2) )

    return distancia


if __name__ == '__main__':


    name_fich = input("Introduce el nombre(ruta) del fichero: ")

    if not os.path.isfile(name_fich):
        print("El parametro introducido(", name_fich, ") no es un fichero.")
        exit(0)

    file = open(name_fich, "r")
    info = read_file(file)
    n_graphPoint = info[0]
    list_Points = info[1]


    print(f"El num de puntos es:{n_graphPoint}")
    print(f"Los puntos son: \n {list_Points}")


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
        tupla = (round(float(linea[0]), 2), round(float(linea[1]), 2))
        list_Points.append(tupla)
        i += 1

 '''

    listaIndices = [i for i in range(len(list_Points))]

    edges = []

    listaAristasPeso = []

    for i in listaIndices:
        for j in listaIndices:
            if i != j:
                if not edges.__contains__( (i,j) ) or not edges.__contains__( (j,i) ):
                    edges.append( (i,j) )
                    peso = caulculoDistancia(list_Points,i,j)
                    if not listaAristasPeso.__contains__(peso):
                        listaAristasPeso.append(peso)

    graph = UndirectedGraph(E=edges)
    print(graph)
    print(len(graph.E))
    print(len(listaAristasPeso))
    print(listaAristasPeso)





    print(f"Este es Kruskal \n {kruskal(graph,edges)}")

