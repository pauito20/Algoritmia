import os
import sys
from typing import List, Optional

from bt_scheme import infinity


def funambulista(edificios: List[int]):
    def funambilistaRecursive(i_ed_1: int, i_ed_2: int, i_ed_valle: int, res: List[int]):
        # Caso base: Hay 2 o menos edificios
        if i_ed_1 == i_ed_2 or i_ed_1 == i_ed_2 - 1:
            return res
        # Recursividad miramos derecha, izquierda y centro y nos quedamos la mejor opcion (mayor valle)
        centro = (i_ed_1 + i_ed_2) // 2
        res_izq = funambilistaRecursive(i_ed_1, centro, i_ed_valle, res)
        res_der = funambilistaRecursive(centro + 1, i_ed_2, centro + 2, res)

        #Miramos el máximo de la izquierda
        ind_izq = centro
        h_max_izq = 0
        ind_max_izq = -1
        while ind_izq >= 0:
            if h_max_izq < edificios[ind_izq]:
                h_max_izq = edificios[ind_izq]
                ind_max_izq = ind_izq
            ind_izq -= 1

        #Vamos hacia la derecha, si cogemos un edificio mayor al de la izquierda paramos
        ind_der = ind_max_izq+1
        h_max_der = 0
        ind_max_der = -1
        while ind_der < len(edificios):
            if h_max_der < edificios[ind_der]:
                h_max_der = edificios[ind_der]
                ind_max_der = ind_der
            if edificios[ind_max_der] > edificios[ind_max_izq]:
                #Paramos, ya que max_izq es más pequeño max_der (pasamos cable)
                break
            ind_der += 1

        i = ind_max_izq +1
        valle = -1
        h_valle = infinity
        while i < ind_max_der:
            if edificios[i] < h_valle:
                h_valle = edificios[i]
                valle = i
            i += 1

        res_centro = [ind_max_izq, ind_max_der, valle, min(edificios[ind_max_izq], edificios[ind_max_der])-edificios[valle]]

        if res_izq[3] > res_der[3] and res_izq[3] >= res_centro[3]:
            return res_izq
        elif res_der[3] > res_izq[3] and res_der[3] >= res_centro[3]:
            return res_der
        else:
            return res_centro

    # Caso base: Lista de edificios vacia
    if len(edificios) <= 2:
        return [-1]
        # Llamada de la función recursiva inicial
    return funambilistaRecursive(0, len(edificios) - 1, 1, [-1, -1, -1, -1])


if __name__ == '__main__':

    name_fich = input("Introduce el nombre(ruta) del fichero: ")

    if not os.path.isfile(name_fich):
        print("El parametro introducido(", name_fich, ") no es un fichero.")
        exit(0)

    file = open(name_fich, "r")
    linea = str(file.readline())
    numEdificios = int(linea)

    alturas = []
    for i in range(numEdificios):
        linea = (str(file.readline().rstrip('\n')))
        alturas.append(int(linea))

    '''

    # Convertimos el fichero en una lista de líneas
    lineas_fich = sys.stdin.readlines()
    numEdificios = int(lineas_fich[0])

    alturas = []
    for i in range(1, len(lineas_fich)):
        alturas.append(int(lineas_fich[i]))
    '''

    print("\n----- Parámetros de entrada -----")
    print("Nº de edificios: ", numEdificios)
    print("Alturas de los edificios: ", alturas)

    res = funambulista(alturas)

    print("\n----- RESULTADO -----")

    if res[0] == -1:
        print("NO HAY SOLUCIÓN")
    else:

        print("Resultado FINAL OBTENIDO: ", res)

