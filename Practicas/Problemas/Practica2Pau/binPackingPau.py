from typing import *
from random import random, seed

def mientras_quepa(W: List[int], C: int) -> List[int]:
    #Contenedor actual
    actual = 0
    #Peso maximo que admite el contenedor
    libre = C
    #Lista con el resultado del tamaño de la lista inicial
    res = [0]*len(W)

    #Recorremos la lista pasada con los pesos
    for i in range(len(W)):
        #Si el peso es menor o igual que libre
        if W[i] <= libre:
            #modificamos libre, y le quitamos el peso añadido
            libre -= W[i]
            #Añadimos el contenedor al resultado
            res[i] = actual
    #En caso de que libre sea mayor que el peso maximo
        else:
            #Libre será el peso inicial
            libre = C
            #Aumentamos actual, que es el contenedor en el que guardamos
            actual += 1
            #A la lista resultado, le ponemos el contenedor
            res[i] = actual

        #Actualizamos el valor de libre
        libre -= W[i]
    return res




def primero_que_quepa(W: List[int], C: int) -> List[int]:
    # Peso maximo que admite el contenedor
    libres = [C]
    # Lista con el resultado del tamaño de la lista inicial
    contenedores = []
    #Recorremos la lista de objetos pasada
    for w in W:
        pos = -1
        for i in range(len(libres)):
            if libres[i] >= w:
                pos = i
                break
        #Una vez recorrido podemos, o tener la posición correcta o no tenerla
        if pos == -1:
            # Posición no correcta
            libres.append(C)
            pos = len(libres) - 1

        #Posición correcta
        contenedores.append(pos)
        libres[pos] -= w

    return contenedores


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    ''' Al ordenar de mayor a menor peso, mejoramos el resultado, acercandose al óptimo '''
    indices_ordenados = sorted(range(len(W)), key = lambda i: -W[i])
    # Peso maximo que admite el contenedor
    libres = [C]
    # Lista con el resultado del tamaño de la lista inicial
    contenedores = [0] * len(W)
    # Recorremos la lista de objetos pasada
    for i in indices_ordenados:
        w = W[i]
        pos = -1
        for j in range(len(libres)):
            if libres[j] >= w:
                pos = j
                break
        # Una vez recorrido podemos, o tener la posición correcta o no tenerla
        if pos == -1:
            # Posición no correcta
            libres.append(C)
            pos = len(libres) - 1

        # Posición correcta
        contenedores[i] = pos
        libres[pos] -= w

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
