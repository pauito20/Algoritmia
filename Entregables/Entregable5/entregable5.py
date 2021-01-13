import os
import sys
from typing import List


def minaDiamantes(tablero) -> int:
    def _minaDiamantes(f, c) -> int:
        diamantesAc = tablero[f][c]

        if (f, c) not in mem:
            if c == 0 and f == 0:
                mem[f, c] = diamantesAc

            elif c == 0:
                mem[f, c] = _minaDiamantes(f - 1, c) + diamantesAc

            elif f == 0:
                mem[f, c] = _minaDiamantes(f, c - 1) + diamantesAc

            else:
                mem[f, c] = max(_minaDiamantes(f - 1, c) + diamantesAc,
                                _minaDiamantes(f, c - 1) + diamantesAc)

        return mem[f, c]

    mem = {}
    return _minaDiamantes(len(tablero)-1, len(tablero[0])-1)


def creaMatriz(filas: int, columnas: int):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz


if __name__ == '__main__':

    sys.setrecursionlimit(5000)
    '''
    name_fich = input("Introduce el nombre(ruta) del fichero: ")

    if not os.path.isfile(name_fich):
        print("El parametro introducido(", name_fich, ") no es un fichero.")
        exit(0)

    file = open(name_fich, "r")
    linea = file.readline().split(" ")
    filas = int(linea[0])
    columnas = int(linea[1])

    numDiamantes = int(file.readline())

    tablero = creaMatriz(filas, columnas)

    i = 0
    while i < numDiamantes:
        linea = file.readline().rstrip('\n').split(" ")
        f = int(linea[0])
        c = int(linea[1])
        d = int(linea[2])
        tablero[f][c] = d
        i += 1
    
    print(filas, columnas)
    print(numDiamantes)
    print("Tablero: ")
    for r in tablero:
        print("\t", r)
    '''

    # Convertimos el fichero en una lista de líneas
    lineas_fich = sys.stdin.readlines()
    filas = int(lineas_fich[0].split(" ")[0])
    columnas = int(lineas_fich[0].split(" ")[1])
    numDiamantes = int(lineas_fich[1])

    tablero = creaMatriz(filas, columnas)
    '''
    for i in range(2, numDiamantes + 2):
        f = int(lineas_fich[i][0])
        c = int(lineas_fich[i][1])
        d = int(lineas_fich[i][2])
        tablero[f][c] = d
    
    '''
    i = 2
    while i < numDiamantes:
        linea = lineas_fich[i].rstrip('\n').split(" ")
        f = int(linea[0])
        c = int(linea[1])
        d = int(linea[2])
        tablero[f][c] = d
        i += 1


    print(minaDiamantes(tablero))