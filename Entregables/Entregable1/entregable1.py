from typing import *

Vertex = Tuple[int,int]
Edge = Tuple[Vertex,Vertex]

def read_file(f):
    tuplas_prohibidas = set()
    rows = int(f.readline().split(" ")[0])
    f.seek(0)
    cols = int(f.readline().split(" ")[1])
    n_f_edges = int(f.readline().split(" ")[0])
    i = 0
    while i < n_f_edges:
        linea = f.readline().rstrip('\n').split(" ")
        tupla = ((int(linea[0]), int(linea[1])), (int((linea[2])), int(linea[3])))
        tuplas_prohibidas.add(tupla)
        i += 1
    return rows,cols,tuplas_prohibidas


def create_labyring():
    return


if __name__ == '__main__':
    name_fich = input("Introduce el nombre(ruta) del fichero: ")
    file = open(name_fich, "r")
    info = read_file(file)
    rows = info[0]
    cols = info[1]
    tuplas_prohibidas = info[2]


    print(rows,cols,tuplas_prohibidas)

