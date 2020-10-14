#Problema1 Crear un laberinto aleatorio
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
import random


def create_labyring(rows,cols):

#Crea una lista, vertices, con los vértices del grafo (nuestras celdas del laberinto).
    vertices = []
    for i in range(rows):
        for j in range(cols):
          vertices.append((i,j))

    #Esto es lo mismo vertices = [(r,c) for r in range(rows) for c in range(cols)]

#Crea un MFSet vacío, mfs, y añádele uno a uno los vértices de la lista vertices usando su método add.

    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

#Crea una lista, edges, con todos los pares de vértices vecinos y barájala. Usa la función shuffle del módulo random.

    edges = []
    for i in range(rows):
        for j in range(cols):
            if j > 0:
                edges.append((i,j),(i,j-1))
            if i > 0:
                edges.append((i,j),(i-1,j))


    random.shuffle(edges,random)

#Crea una lista vacía, corridors. Aquí pondremos las aristas (pasillos) que tendrá al final nuestro grafo (laberinto).

    corridors = []

#Recorre la lista edges y, para cada arista (u,v), encuentra la clase a la que pertenece
# cada uno de los dos vértices usando find. Si son diferentes, fusiónalas en la misma clase con
# merge y añade la arista (u,v) a la lista corridors.

    for u,v in edges:
        cu = mfs.find(u)
        cv = mfs.find(v)
        if cu != cv:
            corridors.append((u,v))
            mfs.merge(u,v)  #los une
#El laberinto es el grafo no dirigido que tiene a la lista corridors como conjunto de aristas:

    return UndirectedGraph(E = corridors)