import sys
from typing import List, Optional


def funambulista(edificios: List[int]) -> Optional[List[int]]:
    def funambilistaRecursive(edificios: List[int],i_ed_peq: int, i_ed_gran: int,i_ed_valle: int  ) -> Optional[List[int]]:
        #Caso base
        if len(edificios) <= 1:
            return []
        #Recursividad
        elif
            pass



    #Llamada de la función recursiva inicial
    return funambilistaRecursive(edificios, -1, -1, -1 )


if __name__ == '__main__':
    # Convertimos el fichero en una lista de líneas
    lineas_fich = sys.stdin.readlines()
    numEdificios = int(lineas_fich[0])

    alturas = []
    for i in range(1, len(lineas_fich)):
        alturas.append(int(lineas_fich[i]))

    print("\n----- Parámetros de entrada -----")
    print("Nº de edificios: ", numEdificios)
    print("Alturas de los edificios: ", alturas)

    res = funambulista(alturas)
    print("\n----- RESULTADO -----")

    if len(res) == 0:
        print("NO HAY SOLUCIÓN")
    else:
        print("El resultado es: ", res)




