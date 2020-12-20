import os
import sys
from typing import List, Optional

from bt_scheme import infinity


def funambulista(edificios: List[int]):
    def funambilistaRecursive(i_ed_1: int, i_ed_2: int, i_ed_valle: int, res: List[int]):
        '''
               #Caso base
               print(i_ed_1, i_ed_2, i_ed_valle)
               if i_ed_valle == i_ed_2:
                  return res
               #Recursividad
               if edificios[i_ed_1] > edificios[i_ed_2]:
                   print(f"Recurividad 1")
                   return funambilistaRecursive(i_ed_1, i_ed_2 - 1, i_ed_valle, res)
               if edificios[i_ed_1] < edificios[i_ed_valle]:
                   print(f"Recurividad 2")
                   return funambilistaRecursive(i_ed_1 + 1, i_ed_2, i_ed_valle + 1, res)


               if (abs(res[0]) - abs(res[2])) < (edificios[i_ed_1] - edificios[i_ed_valle]):
                   res = [i_ed_1, i_ed_2, i_ed_valle]
               print(f"Recurividad 3")
               return funambilistaRecursive(i_ed_1 + 1, i_ed_2, i_ed_valle +1, res)
           '''

        #Caso base: Hay 2 o menos edificios
        if i_ed_1 == i_ed_2 or i_ed_1 == i_ed_2 - 1:
            return res

        #Recursividad miramos derecha, izquierda y centro y nos quedamos la mejor opcion (mayor valle)
        centro = (i_ed_1 + i_ed_2) // 2

        res_izq = funambilistaRecursive(i_ed_1, centro, i_ed_valle, res)
        res_der = funambilistaRecursive(centro + 1, i_ed_2, centro + 2, res)
        #Recorremos por el centro (por si hemos partido la solución)

        #POR LA IZQUIERDA Y DISMINUIMOS
        ind_izq = centro
        ind_grande_izq = ind_izq
        ind_peq_izq = i_ed_1
        ind_valle = -1
        valle = infinity
        while ind_izq > 0:
            if edificios[ind_izq - 1] < edificios[ind_izq]:
                if ind_izq - 1 < ind_grande_izq and (edificios[ind_grande_izq] - edificios[ind_izq - 1]) < valle:
                    valle = edificios[ind_grande_izq] - edificios[ind_izq - 1]
                    ind_valle = ind_izq - 1
            else:
                if ind_valle > ind_izq - 1:
                    if edificios[ind_izq - 1] < edificios[ind_grande_izq]:
                        ind_peq_izq = ind_izq - 1
                    else:
                        ind_peq_izq = ind_grande_izq
                        ind_grande_izq = ind_izq - 1
            ind_izq -= 1

        res_centro_izq = [ind_peq_izq, ind_grande_izq, ind_valle, valle]#

        #POR LA DERECHA Y AUMENTAMOS

        ind_der = centro + 1
        ind_grande_der = i_ed_2
        ind_peq_der = centro + 1
        ind_valle = -1
        valle = infinity
        while ind_der < i_ed_2:
            if edificios[ind_der + 1] < edificios[ind_der]:
                if ind_der + 1 > ind_peq_der and (edificios[ind_peq_der] - edificios[ind_der + 1]) < valle:
                    valle = edificios[ind_peq_der] - edificios[ind_der + 1]
                    ind_valle = ind_der + 1
            else:
                if ind_valle < ind_der + 1:
                    if edificios[ind_der + 1] > edificios[ind_grande_der]:
                        if edificios[ind_der + 1] < edificios[ind_peq_der]:
                            ind_grande_der = ind_peq_der
                            ind_peq_der = ind_der + 1
                        else:
                            ind_peq_der = ind_grande_der
                            ind_grande_der = ind_der + 1

                    elif edificios[ind_der + 1] > edificios[ind_peq_der]:
                        ind_peq_der = ind_der + 1
            ind_der += 1

        res_centro_der = [ind_peq_der, ind_grande_der, ind_valle, valle]

        if res_centro_izq[1] > res_centro_der[0]:
            res_centro = [res_centro_izq[1], res_centro_der[1], res_centro_der[2], min(edificios[res_centro_izq[1]], edificios[res_centro_der[1]]) - edificios[res_centro_der[2]]]
        else:
            if res_centro_izq[3] > res_centro_der[3]:
                res_centro = res_centro_izq
            else:
                res_centro = res_centro_der

        if res_izq[3] > res_der[3] and res_izq[3] > res_centro[3]:
            return res_izq
        elif res_der[3] > res_izq[3] and res_der[3] > res_centro[3]:
            return res_der
        else:
            return res_centro

    #Caso base: Lista de edificios vacia
    if len(edificios) <= 2:
        return [-1]
    #Llamada de la función recursiva inicial
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




