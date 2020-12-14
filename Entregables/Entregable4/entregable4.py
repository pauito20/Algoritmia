import os
import sys
from typing import List, Optional


def funambulista(edificios: List[int]):
    def funambilistaRecursive(i_ed_1: int, i_ed_2: int, i_ed_valle: int, res : List[int]):
        #Caso base
        print(i_ed_1,i_ed_2,i_ed_valle)
        if i_ed_valle == i_ed_2:
           return res
        #Recursividad
        if edificios[i_ed_1] > edificios[i_ed_2]:
            print(f"Recurividad 1")
            return funambilistaRecursive(i_ed_1, i_ed_2 - 1 , i_ed_valle, res)
        if edificios[i_ed_1] < edificios[i_ed_valle]:
            print(f"Recurividad 2")
            return funambilistaRecursive(i_ed_1 + 1, i_ed_2, i_ed_valle + 1, res)


        if (abs(res[0]) - abs(res[2])) < (edificios[i_ed_1] - edificios[i_ed_valle]):
            res = [i_ed_1, i_ed_2, i_ed_valle]
        print(f"Recurividad 3")
        return funambilistaRecursive(i_ed_1 + 1, i_ed_2, i_ed_valle +1, res)

    if len(edificios) <= 2:
        return [-1]
    #Llamada de la función recursiva inicial
    return funambilistaRecursive(0, len(edificios) - 1, 1, [-1,-1,-1])

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

    print(f"el resl: {res}")
    if res[0] == -1:
        print("NO HAY SOLUCIÓN")
    else:
        print()
        res.append(alturas[res[0]] - alturas[res[2]])
        print(res)



