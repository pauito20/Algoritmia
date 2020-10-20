#Vamos a recorrer el grafo en profundiad
import random
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo

from Practicas.Problemas.Practica1Gonzalo.labyrinthviewerGonzalo import LabyrinthViewer
from Practicas.Problemas.Practica1Gonzalo.problema1Gonzalo import create_labyring
from typing import *

Vertex = Tuple[int,int]
Edge = Tuple[Vertex,Vertex]

def path(g:UndirectedGraph, source : Vertex, target: Vertex) -> List[Vertex]:
    def recorrido_Desde_a(u:Vertex, v: Vertex):   # v es el sucessor de u
        seen.add(v)
        aristas.append((u, v))
        for suc in g.succs(v):
            if suc not in seen:
                recorrido_Desde_a(v, suc)

    seen = set()
    aristas = []
    recorrido_Desde_a(source,source)
    return recuperar_camino(aristas,target)



def recuperar_camino(lista_aristas : List[Edge], target :Vertex) -> List[Vertex]:
    bp = {}
    for u,v in lista_aristas:   # u es el origen desde el cual llegamos a v
        bp[v] = u
    v = target
    camino = [v]
    while v != bp[v]:
        v = bp[v]
        camino.append(v)
    camino.reverse()
    return camino

#Modificacion para el problema3

def create_labyring_Problema3(rows, cols,n=0):

    vertices = []
    for i in range(rows):
        for j in range(cols):
            vertices.append((i, j))

    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    edges = []
    for i in range(rows):
        for j in range(cols):
            if j > 0:
                edges.append(((i, j), (i, j - 1)))
            if i > 0:
                edges.append(((i, j), (i - 1, j)))

    random.shuffle(edges)
    corridors = []

    for u, v in edges:
        cu = mfs.find(u)
        cv = mfs.find(v)
        if cu != cv :
            corridors.append((u, v))
            mfs.merge(u, v)  # los une
        elif n>0:
            n -=1
            corridors.append((u, v))
            mfs.merge(u, v)  # los une

    return UndirectedGraph(E=corridors)


def shortest_path(g: UndirectedGraph,source: Vertex,target: Vertex) -> List[Vertex]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((source,source))
    seen.add(source)
    while len(queue)>0:
        u, v = queue.pop()   # a V se llega desde U
        aristas.append((u,v))
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v,suc))

    return recuperar_camino(aristas,target)





if __name__ == '__main__':

    graph = create_labyring_Problema3(50,50,500)

    inicial = (0,0)
    final = (49,49)
    resultado = path(graph,inicial,final)
    lol = shortest_path(graph,inicial,final)


    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)
    lv.set_input_point((0, 0))
    lv.set_output_point((4, 9))
    lv.add_path(lol,'blue',offset=2)
    lv.add_path(resultado)

    lv.run()
