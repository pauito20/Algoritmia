from typing import *
from random import random, seed


def mientras_quepa(W: List[int], C: int) -> List[int]:
    contenedores = []
    libres, contenedor = C, 0
    for w in W:
        if w > libres:  # si no, se incrementa el contenedor y se añade en el nuevo decrementando libres
            contenedor += 1
            libres = C
        libres -= w
        contenedores.append(contenedor)
    return contenedores


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    contenedores = []
    espacio_Contenedor = [C] * len(W)
    for w in W:
        for i in range(len(espacio_Contenedor)):
            if w <= espacio_Contenedor[i]:
                espacio_Contenedor[i] -= w
                contenedores.append(i)
                break
    return contenedores



def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    W_ordenado = sorted(range(len(W)), key= lambda i : -W[i])
    contenedores = [0] * len(W)
    espacio_Contenedor = [C] * len(W)
    for i in W_ordenado:
        w = W[i]
        for pos in range(len(espacio_Contenedor)):
            if w <= espacio_Contenedor[pos]:
                espacio_Contenedor[pos] -= w
                contenedores[i] = pos
                break
    return contenedores


def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    # seed(42)
    # W, C = [int(random()*1000)+1 for i in range(1000)], 1000

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        print("-" * 40)
        print("Método:", solve.__name__)
        try:
            sol = solve(W, C)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()
