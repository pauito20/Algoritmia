import os
import sys
from typing import List, Optional


def funambulista(edificios: List[int]) -> Optional[List[int]]:
    def funambilistaRecursive(i_ed_peq: int, i_ed_gran: int,i_ed_valle: int  ) -> Optional[List[int]]:
        #Caso base
        if len(edificios) <= 1:
            return []
        #Recursividad




    #Llamada de la función recursiva inicial
    return funambilistaRecursive(-1,-1,-1)

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
        alturas.append(linea)

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
    '''
    res = funambulista(alturas)
    print("\n----- RESULTADO -----")
    
    if len(res) == 0:
        print("NO HAY SOLUCIÓN")
    else:
        print("El resultado es: ", res)

    '''


