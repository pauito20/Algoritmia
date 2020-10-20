#Vamos a recorrer el grafo en profundiad

from algoritmia.datastructures.digraphs import UndirectedGraph
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


if __name__ == '__main__':

    graph = create_labyring(50,50)
    inicial = (0,0)
    final = (49,49)

    resultado = path(graph,inicial,final)


    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)
    lv.set_input_point((0, 0))
    lv.set_output_point((4, 9))
    lv.add_path(resultado)
    lv.run()
