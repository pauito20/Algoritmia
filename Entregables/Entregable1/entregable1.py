from typing import *
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Practicas.Problemas.Practica1Pau.labyrinthviewerPau import LabyrinthViewer
import random

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

def read_file(f):
    tuplas_prohibidas = set()

    rows = int(f.readline().split(" ")[0])
    f.seek(0)
    cols = int(f.readline().split(" ")[1])

    t_forb = int(f.readline())

    i = 0
    while i < t_forb:
        linea = f.readline().rstrip('\n').split(" ")
        tupla = ((int(linea[0]), int(linea[1])), (int((linea[2])), int(linea[3])))
        tuplas_prohibidas.add(tupla)
        i += 1
    return rows, cols, tuplas_prohibidas


def create_labyring(rows, cols, forbiden:set):
    # Creamos una lista de vértices (celdas del laberinto)
    vertices = [(r, c) for r in range(rows) for c in range(cols)]

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

    #Mezclamos de forma aleatoria las aristas
    random.shuffle(edges)

    # Creamos una lista vacía "corridors" que será la que contenga las aristas finales del grafo
    corridors = []

    # Recorremos edges y para cada arista mediante find, si son diferentes usamos merge para fusionarlas y añadimos esta a corridors
    for u, v in edges:
        cu = mfs.find(u)
        cv = mfs.find(v)
        entra = True

        # Aqui comprobamos si esta esa arista, si no hay que meterla
        if cu != cv:
            for f_ed in forbiden:
                if f_ed == (u, v) or f_ed == (v, u):
                    entra = False

            if entra:
                corridors.append((u, v))
                mfs.merge(u, v)



    # Devolvemos el grafo resultante
    return UndirectedGraph(E=corridors)



if __name__ == '__main__':
    name_fich = input("Introduce el nombre(ruta) del fichero: ")
    file = open(name_fich, "r")
    info = read_file(file)
    rows = info[0]
    cols = info[1]
    tuplas_prohibidas = info[2]

    random.seed(50)


    graph = create_labyring(rows, cols, tuplas_prohibidas)




    # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
    lv = LabyrinthViewer(graph, canvas_width=800, canvas_height=600, margin=10)




    # Obligatorio: Muestra el laberinto
    lv.run()

