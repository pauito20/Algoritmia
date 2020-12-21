import os
import sys
from typing import List, Optional




def funambulista(edificios: List[int]):
    def funambilistaRecursive(i_ed_1: int, i_ed_2: int, i_ed_valle: int, res: List[int]):
        # Caso base: Hay 2 o menos edificios
        if i_ed_1 == i_ed_2 or i_ed_1 == i_ed_2 - 1:
            return res
        if len(edificios) < 3:
            return None
        if len(edificios) == 3:
            if edificios[i_ed_1] > edificios[i_ed_1+1] and edificios[i_ed_1+1] < edificios[i_ed_2]:
                return [i_ed_1, i_ed_2, i_ed_2-1, min(edificios[i_ed_1], edificios[i_ed_2])-edificios[i_ed_1+1]]

        # Recursividad miramos derecha, izquierda y centro y nos quedamos la mejor opcion (mayor valle)
        centro = (i_ed_1 + i_ed_2) // 2

        #Miramos el máximo de la izquierda
        ind_izq = i_ed_1
        h_max_izq = 0
        ind_max_izq = -1

        while ind_izq < centro:
            if h_max_izq < edificios[ind_izq]:
                h_max_izq = edificios[ind_izq]
                ind_max_izq = ind_izq
            ind_izq += 1

        #Vamos hacia la derecha, si cogemos un edificio mayor al de la izquierda paramos
        #ind_der = ind_max_izq+1
        ind_der = centro
        h_max_der = edificios[ind_der]
        ind_max_der = -1

        while ind_der < i_ed_2:
            if h_max_der < edificios[ind_der]:
                h_max_der = edificios[ind_der]
                ind_max_der = ind_der
                if edificios[ind_max_der] > edificios[ind_max_izq]:
                    #Paramos, ya que max_izq es más pequeño max_der (pasamos cable)
                    break
            ind_der += 1

        else:
            ind_izq = centro-1
            i = centro -2
            while i >= i_ed_1:
                if edificios[i] > edificios[ind_izq]:
                    ind_izq = i
                    if edificios[ind_izq] >= edificios[ind_max_der]:
                        break
                i -= 1
            ind_max_izq = ind_izq

        if edificios[i_ed_2] > edificios[ind_max_der]:
            ind_max_der = i_ed_2

        i = ind_max_izq + 1
        valle = i
        h_valle = edificios[i]

        while i < ind_max_der:
            if edificios[i] <= h_valle:
                h_valle = edificios[i]
                valle = i
            i += 1

        res_centro = [ind_max_izq, ind_max_der, valle, min(edificios[ind_max_izq], edificios[ind_max_der])-edificios[valle]]
        res_izq = funambilistaRecursive(i_ed_1, centro, i_ed_valle, res)
        if res_izq is not None and res_izq[3] > res_centro[3]:
            res_centro = res_izq
            print("Izquierda: ", res_centro)
        res_der = funambilistaRecursive(centro, i_ed_2, centro + 1, res)
        if res_der is not None and res_der[3] > res_centro[3]:
            print("Derecha: " , res_centro)
            res_centro = res_der

        return res_centro

    # Caso base: Lista de edificios vacia
    if len(edificios) <= 2:
        return None
        # Llamada de la función recursiva inicial
    return funambilistaRecursive(0, len(edificios) - 1, 1, [-1, -1, -1, -1])


if __name__ == '__main__':
    '''
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



    res = funambulista(alturas)



    if res == None or res[0] == res[1] or res[0]+ 1 == res[1] or res[3] == 0:
        print("NO HAY SOLUCIÓN")
    else:
        print(res[0], res[1], res[2], res[3])


