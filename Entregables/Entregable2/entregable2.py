import os
import sys
from math import sqrt
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet



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


'''
def prim(graph: UndirectedGraph, indicesPesosOrdenados):
    visitados = [0]
    res = []

    lista_TodasAristas = []
    for edge in graph.E:
        lista_TodasAristas.append(edge)

    lista_Vertices = []
    for v in graph.V:
        lista_Vertices.append(v)

    lista_Adyacentes = []
    listaAristaAD = []
    lista_indices = []
    lista_AdyacentesPeso = []

    V = 0
    weight = 0

    seen = set()

    while len(visitados) < len(lista_Vertices):
        res.append(V)
        for ady in graph.succs(V):
            if ady != V:
                if ady > V:
                    arista = (V, ady)
                    peso = caulculoDistancia(list_Points, V, ady)
                else:
                    arista = (ady, V)
                    peso = caulculoDistancia(list_Points, ady, V)

                if not listaAristaAD.__contains__(arista):
                    lista_Adyacentes.append(ady)
                    listaAristaAD.append(arista)
                    lista_indices.append(int(lista_TodasAristas.index(arista)))
                    lista_AdyacentesPeso.append(peso)
                    ordenadas = sorted(range(len(lista_AdyacentesPeso)), key=lambda i: lista_AdyacentesPeso[i])

        for i in ordenadas:
            if not seen.__contains__(i):
                seen.add(i)
                pos = lista_indices.index(i)
                print(i,pos)
                V = lista_Adyacentes[pos]
                visitados.append(V)
                weight = weight + listaAristasPeso[pos]
                break

    return visitados, weight
'''

def prim(graph: UndirectedGraph):
    visitados = [0]
    res = []

    aristas = []
    for edge in graph.E:
        aristas.append(edge)

    vertices = []
    for v in graph.V:
        vertices.append(v)

    mfs = MergeFindSet()
    for i in vertices:
        mfs.add(i)

    weight, V = 0, 0
    seen = set()
    adyacentesAcomulados = { }


    while len(visitados) < len(vertices):
        res.append(V)
        visitados.append(V)
        verticesAdyacentes = []
        aristasAdyacentes = []
        pesoAristasAdyacentes = []
        indices = []

        for ady in graph.succs(V):
            if ady != V:
                if ady > V:
                    arista = (V, ady)
                    peso = caulculoDistancia(list_Points, V, ady)
                else:
                    arista = (ady, V)
                    peso = caulculoDistancia(list_Points, ady, V)

                if not adyacentesAcomulados.__contains__(arista):
                    adyacentesAcomulados.setdefault(arista,peso)
                    verticesAdyacentes.append(ady)


        j = 0
        for i in adyacentesAcomulados.keys():
            aristasAdyacentes.append(i)
            indices.append(j)
            pesoAristasAdyacentes.append(adyacentesAcomulados.get(i))
            j += 1

        ordenadas = sorted(range(len(pesoAristasAdyacentes)), key=lambda i: pesoAristasAdyacentes[i])




    return res, weight



def caulculoDistancia(listPoint, i, j):
    v1x = listPoint[i][0]
    v1y = listPoint[i][1]
    v2x = listPoint[j][0]
    v2y = listPoint[j][1]

    distancia = sqrt(pow((abs(v1x - v2x)), 2) + pow((abs(v1y - v2y)), 2))

    return distancia


if __name__ == '__main__':

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
    res_kruskal = kruskal(graph, indicesPesosOrdenados, list_Points)
    g = UndirectedGraph(E=res_kruskal[0])


    print(res_kruskal[1])
    print(recorrido_profundidad_vertices(g, 0))

    print(prim(graph))







