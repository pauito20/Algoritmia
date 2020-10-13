from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from Practicas.Problemas.Practica1Pau.labyrinthviewerPau import LabyrinthViewer
import random

def create_labyrinth(rows,cols):
    # Creamos una lista de vértices (celdas del laberinto)
    vertices = []
    for i in range(rows):
        for j in range(cols):
            vertices.append((i, j))
    #Opción pro: vertices = [(r, c) for i in range(rows) for c in range(cols]


    #Creamos un MFSet y le añadimos uno a uno los vertices de la lista "vertices"
    mfs = MergeFindSet()

    for v in vertices:
        mfs.add(v)

    #Creamos una lista "edge" con los pares de vértices vecinos y la barajamos
    edges = []

    for i in range(rows):
        for j in range(cols):
            if j > 0:
                edges.append(((i, j),(i, j-1)))
            if i > 0:
                edges.append(((i, j), (i -1, j)))
    #Otra forma
    '''
    for cx, cy in vertices:
        if cy +1 < rows:
            edges.append((cx, cy), (cx, cy + 1))
        if cx + 1 < cols:
            edges.append((cx, cy), (cx + 1, cy))
    '''
    #Otra forma
    '''
    edges = [((r, c), (r, c+1)) for r in range(rows) for c in range(cols)]
    edges.extend 
        [((r + 1, c), (r, c)) for r in range(rows -1) for c in range(cols)]
    '''


    random.shuffle(edges)


    #Creamos una lista vacía "corridors" que será la que contenga las aristas finales del grafo
    corridors=[]

    #Recorremos edges y para cada arista mediante find, si son diferentes usamos merge para fusionarlas y añadimos esta a corridors
    for u, v in edges:
        cu = mfs.find(u)
        cv = mfs.find(v)

        if cu != cv:
            corridors.append((u, v))
            mfs.merge(u, v)

    #Devolvemos el grafo resultante
    return UndirectedGraph(E = corridors)