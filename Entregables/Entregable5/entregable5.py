import os
import sys
from typing import List


def minaDiamantes(tablero) -> int:
    def _minaDiamantes(f, c, diamantesAcomulados) -> int:
        '''

        if tablero[f][c] != 0:
            diamantesAcomulados += tablero[f][c]

        if (f, c) not in mem:
            print(mem)
            if f + 1 < len(tablero) and c + 1 < len(tablero[0]):
                mem[f, c] = max(_minaDiamantes(f + 1, c, diamantesAcomulados),
                                _minaDiamantes(f, c + 1, diamantesAcomulados))
            elif f + 1 < len(tablero):
                mem[f, c] = _minaDiamantes(f + 1, c, diamantesAcomulados)
            elif c + 1 < len(tablero[0]):
                mem[f, c] = _minaDiamantes(f, c + 1, diamantesAcomulados)

        return mem[f, c]

        '''

        if tablero[f][c] != 0:
            diamantesAcomulados += tablero[f][c]

        if f + 1 < len(tablero) and c + 1 < len(tablero[0]):
            return max(_minaDiamantes(f + 1, c, diamantesAcomulados),
                        _minaDiamantes(f, c + 1, diamantesAcomulados))
        elif f + 1 < len(tablero):
            return _minaDiamantes(f + 1, c, diamantesAcomulados)
        elif c + 1 < len(tablero[0]):
            return _minaDiamantes(f, c + 1, diamantesAcomulados)

        return diamantesAcomulados

    mem = {}
    diamantesAcomulados = 0
    return  _minaDiamantes(0, 0, diamantesAcomulados)


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
    '''
    print(filas, columnas)
    print(numDiamantes)
    print("Tablero: ")
    for r in tablero:
        print("\t", r)
    '''
    print("\n PICO PALA PICO PALA: ")
    print(minaDiamantes(tablero))

    '''
    # Convertimos el fichero en una lista de líneas
    lineas_fich = sys.stdin.readlines()
    filas = lineas_fich[0].split(" ")[0]
    columnas = lineas_fich[0].split(" ")[1]
    numDiamantes = int(lineas_fich[1])

    tablero = creaMatriz(filas, columnas)

    for i in range(2, numDiamantes + 2):
        f, c, d = int(lineas_fich[i])
        tablero[f][c] = d  
    '''
