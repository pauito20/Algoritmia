import os
import sys
from math import sqrt
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.prioritymaps import MinHeapMap
from algoritmia.datastructures.priorityqueues import MinHeap
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


def recorrido_profundidad_vertices(g: UndirectedGraph, v_inicial):
    def recorrido_desde(v):
        seen.add(v)
        vertices.append(v)
        for suc in g.succs(v):
            if v == 0:
                suc = min(g.succs(v))

            if suc not in seen:
                recorrido_desde(suc)

    vertices = []
    seen = set()
    recorrido_desde(v_inicial)
    return vertices


def kruskal(graph: UndirectedGraph, indicesPesosOrdenados, listaPuntos):
    res = []
    edgeList = graph.E
    vertices = graph.V
    apariciones = [0] * len(vertices)


    listaAristas = []
    for i in edgeList:
        listaAristas.append(i)

    mfs = MergeFindSet()
    for i in vertices:
        mfs.add(i)

    total_weight = 0

    # Comprobacion de que no hay ciclos y que solo aparezcan una vez (habrá que conectarlos)
    for i in indicesPesosOrdenados:
        u, v = listaAristas[i]
        cu = mfs.find(u)
        cv = mfs.find(v)
        if cu != cv and apariciones[v] < 2 and apariciones[u] < 2:
            apariciones[v] += 1
            apariciones[u] += 1
            mfs.merge(u, v)
            res.append((u, v))
            total_weight = total_weight + listaAristasPeso[i]

    ult = -1
    prim = -1
    for v in vertices:
         if apariciones[v] < 2:
            if prim == -1:
                prim = v
            else:
                ult = v

    res.append((prim, ult))
    total_weight = total_weight + caulculoDistancia(listaPuntos, prim, ult)

    return res, total_weight


def prim(graph: UndirectedGraph, list_Points):
    res = []
    seen = set()

    aristas = []
    for edge in graph.E:
        aristas.append(edge)

    vertices = []
    for v in graph.V:
        vertices.append(v)

    apariciones = [0] * len(vertices)

    mfs = MergeFindSet()
    for i in vertices:
        mfs.add(i)

    weight, v_padre = 0, 0
    adyacentesAcumulados = MinHeapMap()
    aristasVisitadas = set()

    while len(seen) != len(vertices):
        seen.add(v_padre)

        for hijo in graph.succs(v_padre):
            if hijo != v_padre:
                if hijo > v_padre:
                    arista = (v_padre, hijo)
                    peso = caulculoDistancia(list_Points, v_padre, hijo)
                else:
                    arista = (hijo, v_padre)
                    peso = caulculoDistancia(list_Points, hijo, v_padre)
                if not aristasVisitadas.__contains__(arista):
                    adyacentesAcumulados.setdefault(arista,peso)

        hayCiclo = True
        minimo, edge_min = None, None



        while hayCiclo and len(adyacentesAcumulados) != 0:
            #minimo = colaPrio.extract_opt()

            #edge_min = list(adyacentesAcumulados.keys())[list(adyacentesAcumulados.values()).index(minimo)]
            edge_min = adyacentesAcumulados.opt()
            minimo = adyacentesAcumulados[edge_min]
            u, v = edge_min
            cu = mfs.find(u)
            cv = mfs.find(v)
            if cu != cv and apariciones[v] < 2 and apariciones[u] < 2:
                apariciones[v] += 1
                apariciones[u] += 1
                mfs.merge(u, v)
                hayCiclo = False
            else:
                adyacentesAcumulados.__delitem__(edge_min)

        if len(adyacentesAcumulados) == 0:
            ult = -1
            prim = -1
            for v in vertices:
                if apariciones[v] < 2:
                    if prim == -1:
                        prim = v
                    else:
                        ult = v

            res.append((prim, ult))
            weight = weight + caulculoDistancia(list_Points, prim, ult)
            break


        adyacentesAcumulados.__delitem__(edge_min)
        aristasVisitadas.add(edge_min)
        res.append(edge_min)
        weight = weight + minimo
        u, v_padre = edge_min
        if seen.__contains__(v_padre):
            v_padre, l = edge_min


    return res, weight

def caulculoDistancia(listPoint, i, j):
    v1x = listPoint[i][0]
    v1y = listPoint[i][1]
    v2x = listPoint[j][0]
    v2y = listPoint[j][1]

    distancia = sqrt(pow((abs(v1x - v2x)), 2) + pow((abs(v1y - v2y)), 2))

    return distancia


if __name__ == '__main__':
    '''
    sys.setrecursionlimit(1010)
    name_fich = input("Introduce el nombre(ruta) del fichero: ")

    if not os.path.isfile(name_fich):
        print("El parametro introducido(", name_fich, ") no es un fichero.")
        exit(0)

    file = open(name_fich, "r")
    info = read_file(file)
    n_graphPoint = info[0]
    list_Points = info[1]
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
    res_kruskal = kruskal(graph, indicesPesosOrdenados, list_Points)
    g = UndirectedGraph(E=res_kruskal[0])


    print(res_kruskal[1])
    print(recorrido_profundidad_vertices(g, 0))



    res_prim = prim(graph,list_Points)
    g_prim = UndirectedGraph(E=res_prim[0])

    print(res_prim[1])
    print(recorrido_profundidad_vertices(g_prim,0))





