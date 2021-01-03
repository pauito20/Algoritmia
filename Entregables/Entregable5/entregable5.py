import os
import sys
from typing import List


def minaDiamantes(tablero) -> int:
    def _minaDiamantes(fila, columna, diamantesAcomulados):
        if tablero[fila][columna] != 0:
            diamantesAcomulados += tablero[fila][columna]
        max = 0
        down = 0
        right = 0
        if fila+1 < len(tablero) and columna < len(tablero[0]):
            #print("posicion abajo=", tablero[fila + 1][columna])
            down = _minaDiamantes(fila+1, columna, diamantesAcomulados)

        if columna+1 < len(tablero[0]) and fila < len(tablero):
            #print("posicion arriba=", tablero[fila][columna + 1])
            right = _minaDiamantes(fila, columna+1, diamantesAcomulados)

        if down > diamantesAcomulados:
            diamantesAcomulados = down
        if right > diamantesAcomulados:
            diamantesAcomulados = right


        return diamantesAcomulados



    diamantesAcomulados = 0

    return _minaDiamantes(0, 0, diamantesAcomulados)

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

    print(filas, columnas)
    print(numDiamantes)
    print("Tablero: ")
    for r in tablero:
        print("\t", r)

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









