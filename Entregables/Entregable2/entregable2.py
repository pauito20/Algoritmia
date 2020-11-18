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


def kruskal(graph: UndirectedGraph, indicesPesosOrdenados):
    res = []
    edgeList = graph.E
    vertices = graph.V

    print("\nDatos para Kruskal:")
    print("Lista aristas: ", edgeList)
    print("Lista indices peso ordenados: ", indicesPesosOrdenados)
    print("Lista vertices: ", vertices)

    listaAristas = []
    for i in edgeList:
        listaAristas.append(i)

    mfs = MergeFindSet()
    for i in vertices:
        mfs.add(i)

    total_weight = 0
    # Comprobacion de que no hay ciclos
    for i in indicesPesosOrdenados:
        u, v = listaAristas[i]
        cu = mfs.find(u)
        cv = mfs.find(v)
        print(listaAristasPeso[i])
        if cu != cv:
            mfs.merge(u, v)
            res.append((u, v))
            total_weight = total_weight + listaAristasPeso[i]

    print("------ Fin kruskal ------")

    return res, total_weight


def kruskalModificado(graph: UndirectedGraph):
    '''
    1. Empezando des del vertice inicial, buscamos la lista de aristas que menos pese
       en este caso v_inicial = 0

    2. Recorremos la siguiente arista de menor peso

    3. Formamos así el camino más corto des de un índice dado
    '''

    res = []
    edgeList = graph.E
    vertices = graph.V

    print("\nDatos para Kruskal Modificado:")
    print("Lista aristas: ", edgeList)
    print("Lista indices peso ordenados: ", indicesPesosOrdenados)
    print("Lista vertices: ", vertices)

    listaAristas = []
    for i in edgeList:
        listaAristas.append(i)

    mfs = MergeFindSet()
    for i in vertices:
        mfs.add(i)

    total_weight = 0
    # Comprobacion de que no hay ciclos
    for i in indicesPesosOrdenados:
        u, v = listaAristas[i]
        cu = mfs.find(u)
        cv = mfs.find(v)
        print(listaAristasPeso[i])
        if cu != cv:
            mfs.merge(u, v)
            res.append((u, v))
            total_weight = total_weight + listaAristasPeso[i]

    print("------ Fin kruskal Modificado ------")
    return res, total_weight


def caulculoDistancia(listPoint, i, j):
    v1x = listPoint[i][0]
    v1y = listPoint[i][1]
    v2x = listPoint[j][0]
    v2y = listPoint[j][1]

    distancia = sqrt(pow((abs(v1x - v2x)), 2) + pow((abs(v1y - v2y)), 2))

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

    print(f"El num de puntos es: {n_graphPoint}")
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
            edges.append((i, j))

    graph = UndirectedGraph(E=edges)

    aristas = graph.E

    for u, v in aristas:
        peso = caulculoDistancia(list_Points, u, v)
        listaAristasPeso.append(peso)

    indicesPesosOrdenados = sorted(range(len(listaAristasPeso)), key=lambda i: listaAristasPeso[i])



    print("Grafo creado: ", graph)
    print("Lista Pesos Arista: ", listaAristasPeso)
    print("Lista Indices ordenados: ", indicesPesosOrdenados)
    print(f"\n <<<<<<<<<< Este es el resultado de Kruskal >>>>>>>>>>>\n {kruskal(graph, indicesPesosOrdenados)}")
    # print(f"Este es el resultado de KruskalModificado \n {kruskalModificado(graph)}")
