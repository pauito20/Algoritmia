#import os
import sys
from typing import *

from algoritmia.datastructures.queues import Fifo
from easycanvas import EasyCanvas
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
import random


#from Entregables.Entregable1.labyrinthviewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

#---------------------------------------LABYRINTVIEWER-----------------------------------------------------------------------------------#
#---------------------------------------LABYRINTVIEWER-----------------------------------------------------------------------------------#


class LabyrinthViewer(EasyCanvas):
    def __init__(self, lab: UndirectedGraph, canvas_width: int = 400, canvas_height: int = 400, margin: int = 10):
        EasyCanvas.__init__(self)

        # check 'lab' type
        if not isinstance(lab, UndirectedGraph) or \
                any([type(p) != type((1, 1)) or len(p) != 2 or type(p[0]) != type(1) or type(p[1]) != type(1) for p in
                     lab.V]):
            raise TypeError("The labyrinth must be an UnirectedGraph of two integer tuples")

        self.lab = lab
        self.paths = []
        self.marked_cells = []
        self.margin = margin
        self.max_col = max(p[1] for p in self.lab.V)
        self.max_row = max(p[0] for p in self.lab.V)
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.cell_size = min(float((canvas_width - margin) / (self.max_col + 1)),
                             float((canvas_height - margin) / (self.max_row + 1)))
        self.mw = self.canvas_width - self.cell_size * (self.max_col + 1)
        self.mh = self.canvas_height - self.cell_size * (self.max_row + 1)
        self.ip = self.op = None

    def set_input_point(self, pos: Vertex):
        self.ip = pos

    def set_output_point(self, pos: Vertex):
        self.op = pos

    def add_marked_cell(self, cell, color='red', ):
        self.marked_cells.append((cell, color))

    def add_path(self, path: List[Vertex], color: str = 'red', offset: int = 0):
        self.paths.append((path, color, offset))

    def _draw_path(self, path: List[Vertex], color: str, offset: int):
        u = path[0]
        mw2 = self.mw / 2 + self.cell_size / 2 + offset
        mh2 = self.mh / 2 + self.cell_size / 2 + offset
        for v in path[1:]:
            self.create_line(mw2 + u[1] * self.cell_size, mh2 + u[0] * self.cell_size, mw2 + v[1] * self.cell_size,
                             mh2 + v[0] * self.cell_size, color, width=3)
            u = v

    def main(self):
        mw = self.mw
        mh = self.mh

        self.easycanvas_configure(title='Labyrinth',
                                  background='white',
                                  size=(self.canvas_width, self.canvas_height),
                                  coordinates=(0, self.canvas_height, self.canvas_width, 0))

        # Draw borders
        self.create_rectangle(mw / 2, mh / 2, self.canvas_width - mw / 2, self.canvas_height - mh / 2)

        # Draw I and O on input and output cells
        if self.ip is not None:
            self.create_text(mw / 2 + (self.ip[1] + 0.5) * self.cell_size, mh / 2 + (self.ip[0] + 0.5) * self.cell_size,
                             "I", self.cell_size / 1.5, "CENTER", "black")
        if self.op is not None:
            self.create_text(mw / 2 + (self.op[1] + 0.5) * self.cell_size, mh / 2 + (self.op[0] + 0.5) * self.cell_size,
                             "O", self.cell_size / 1.5, "CENTER", "black")

        # Draw marked cells
        for cell, color in self.marked_cells:
            cx = mw / 2 + cell[1] * self.cell_size + self.cell_size / 2
            cy = mh / 2 + cell[0] * self.cell_size + self.cell_size / 2
            self.create_filled_circle(cx, cy, self.cell_size / 2.5 - 1, color, color)
            self.create_filled_rectangle(cx - self.cell_size / 2 + 1, cy - self.cell_size / 2 + 1,
                                         cx + self.cell_size / 2, cy + self.cell_size / 2, color, color)
        # Draw internal walls
        for r in range(self.max_row + 1):
            for c in range(self.max_col + 1):
                u = r, c
                x = c * self.cell_size
                y = r * self.cell_size

                if u not in self.lab.V or (r + 1, c) not in self.lab.succs(u):
                    self.create_line(mw / 2 + x, mh / 2 + y + self.cell_size, mw / 2 + x + self.cell_size,
                                     mh / 2 + y + self.cell_size)

                if u not in self.lab.V or (r, c + 1) not in self.lab.succs(u):
                    self.create_line(mw / 2 + x + self.cell_size, mh / 2 + y, mw / 2 + x + self.cell_size,
                                     mh / 2 + y + self.cell_size)

        for path, color, offset in self.paths:
            self._draw_path(path, color, offset)

        # Wait for a key
        self.readkey(True)

#--------------------------------------------------------------------------------------------------------------------------#

def recorredor_aristas_anchura(grafo: UndirectedGraph, v_inicial) -> List[Vertex]:
    vertices = []
    queue = Fifo()
    seen = set()
    queue.push(v_inicial)
    seen.add(v_inicial)
    while len(queue) > 0:
        v = queue.pop()
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push(suc)
    return vertices


def esConexo(grafo: UndirectedGraph):
    vertices_no_visitados = set(grafo.V)
    resultado = []
    while len(vertices_no_visitados) > 0:
        u = vertices_no_visitados.pop()
        vertices_visitados = recorredor_aristas_anchura(grafo,u)
        vertices_no_visitados -= set(vertices_visitados)
        resultado.append(vertices_visitados)
    return resultado


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
            #for f_ed in forbiden:
                #if f_ed == (u, v) or f_ed == (v, u):
                    #entra = False
            if forbiden.__contains__((u, v)) or forbiden.__contains__((v, u)):
                entra = False

            if entra:
                corridors.append((u, v))
                mfs.merge(u, v)

    # Devolvemos la lista de aristas
    return corridors



if __name__ == '__main__':

    '''
    name_fich = input("Introduce el nombre(ruta) del fichero: ")

    if not os.path.isfile(name_fich):
        print("El parametro introducido(", name_fich, ") no es un fichero.")
        exit(0)
    else:
    '''

    #name_fich = input()

    name_fich = str(sys.stdin)
    file = open(name_fich, "r")
    info = read_file(file)
    rows = info[0]
    cols = info[1]
    tuplas_prohibidas = info[2]

    random.seed(50)


    edge_list = create_labyring(rows, cols, tuplas_prohibidas)

    graph = UndirectedGraph(E=edge_list)

    if (len(esConexo(graph)) != 1):
        print("NO ES POSIBLE CONSTRUIR EL LABERINTO")
        exit(-1)

    #Imprimimos los datos pedidos por pantalla
    print(rows, " ", cols)
    print(len(edge_list))

    for u, v in edge_list:
        print(u[0], u[1], v[0], v[1])

    print("sys.argv[1] es : " , sys.argv[1])

    if (sys.argv[1] == "-g"):

        # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
            lv = LabyrinthViewer(graph, canvas_width=800, canvas_height=600, margin=10)

        # Obligatorio: Muestra el laberinto
            lv.run()


