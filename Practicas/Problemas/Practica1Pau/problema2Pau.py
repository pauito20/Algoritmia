from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo

from Practicas.Problemas.Practica1Pau.labyrinthviewerPau import LabyrinthViewer
import random

from typing import *

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

'''RECORREMOS EL LABERINTO EN PROFUNCICDAD DE FORMA RECURSIVA'''


def path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    def recorrido_profundidad(u: Vertex, v: Vertex):
        # Añadimos el primer vértice visitado  al conjunto de vistos "seen"
        seen.add(v)
        aristas.append((u, v))
        # recorremos los hijos del primero pasado y vemos los que estan o no vistos
        for suc in g.succs(v):
            if suc not in seen:
                res = recorrido_profundidad(v, suc)

    aristas = []
    seen = set()
    recorrido_profundidad(source, source)
    return recover_path(aristas, target)


''' MÉTODO PARA RECUPERAR EL CAMINO TRAZADO'''


def recover_path(edges: List[Edge], target: Vertex):
    # Diccionario back pointer para cada (u ,v) de edges
    bp = {}
    for u,v in edges:
        bp[v] = u
    v = target
    path = [v]

    while bp[v] != v:
        #Todavía no se ha llegado al origen (arista fantasma)
        v = bp[v]
        path.append(v)
    #Hemos ido hacia atrás por ello giramos el camino
    path.reverse()
    return path

'''RECORREMOS EL LABERINTO EN ANCHURA, ENCONTRANDO CAMINO MÁS CORTO POSIBLE'''


def shortest_path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((source, source))
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))

    return recover_path(aristas, target)



'''CREAMOS UN LABERINTO'''


def create_labyrinth(rows, cols, n=0):
    # Creamos una lista de vértices (celdas del laberinto)
    vertices = []
    for i in range(rows):
        for j in range(cols):
            vertices.append((i, j))
    '''
    Opción pro: vertices = [(r, c) for r in range(rows) for c in range(cols)]
    '''

    # Creamos un MFSet y le añadimos uno a uno los vertices de la lista "vertices"
    mfs = MergeFindSet()

    for v in vertices:
        mfs.add(v)

    # Creamos una lista "edge" con los pares de vértices vecinos y la barajamos
    edges = []

    for i in range(rows):
        for j in range(cols):
            if j > 0:
                edges.append(((i, j), (i, j - 1)))
            if i > 0:
                edges.append(((i, j), (i - 1, j)))
    # Otra forma
    '''
    for cx, cy in vertices:
        if cy +1 < rows:
            edges.append((cx, cy), (cx, cy + 1))
        if cx + 1 < cols:
            edges.append((cx, cy), (cx + 1, cy))
    '''
    # Otra forma
    '''
    edges = [((r, c), (r, c+1)) for r in range(rows) for c in range(cols)]
    edges.extend 
        [((r + 1, c), (r, c)) for r in range(rows -1) for c in range(cols)]
    '''

    random.shuffle(edges)

    # Creamos una lista vacía "corridors" que será la que contenga las aristas finales del grafo
    corridors = []

    # Recorremos edges y para cada arista mediante find, si son diferentes usamos merge para fusionarlas y añadimos esta a corridors
    for u, v in edges:
        cu = mfs.find(u)
        cv = mfs.find(v)

        if cu != cv:
            corridors.append((u, v))
            mfs.merge(u, v)
        elif n > 0:
            #Utilizamos para que haya más caminos en el laberinto
            corridors.append((u, v))
            n -= 1

    # Devolvemos el grafo resultante
    return UndirectedGraph(E=corridors)


''' ############ ---------- Programa Principal ---------- ############ '''
if __name__ == '__main__':
    # Creamos el grafo con la función utilizada anteriormente
    graph = create_labyrinth(100, 100, 1000)


    # Creamos un camino mediante el recorrido en profundidad y lo pintamos en azul
    ini = (0, 0)
    fin = (99, 99)
    camino = path(graph, ini, fin)
    shortest_camino = shortest_path(graph, ini, fin)

    # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
    lv = LabyrinthViewer(graph, canvas_width=1100, canvas_height=800, margin=20)
    lv.add_path(camino, 'blue')
    lv.add_path(shortest_camino, 'red', offset = 3)

    # Obligatorio: Muestra el laberinto
    lv.run()
