from typing import *
import sys


def busca_edificios(a: List[int]) -> Optional[Tuple[int, int, int, int]]:
    def rec(b: int, e: int) -> Optional[Tuple[int, int, int, int]]:

        '''
        if is simple
            return trivial_solution
        else
            reducir y recursividad
        '''
            
        num_elem = e-b
        if num_elem < 3:
            return None
        elif num_elem == 3:
            if a[b] > a[b+1] and a[b+2] > a[b+1]:
                return b, b+2, b+1, min(a[b] - a[b+1], a[b+2] - a[b+1])
            return None
        else:
            medio = (b+e)//2

            izq = b
            for i in range(b+1, medio):
                if a[i] > a[izq]:
                    izq = i

            der = medio
            for i in range(medio, e):
                if a[i] >= a[der]:
                    der = i
                    if a[der] >= a[izq]:
                        break
            else:
                izq = medio-1
                for i in range(medio-2, b-1, -1):
                    if a[i] > a[izq]:
                        izq = i
                        if a[izq] >= a[der]:
                            break

            valle = izq+1
            for i in range(izq+2, der):
                if a[i] < a[valle]:
                    valle = i

            devolver = izq, der, valle, min(a[izq] - a[valle], a[der] - a[valle])
            aux = rec(b, medio)
            if aux is not None and aux[3] > devolver[3]:
                devolver = aux

            aux = rec(medio, e)
            if aux is not None and aux[3] > devolver[3]:
                devolver = aux

            return devolver

    return rec(0, len(a))


if __name__ == '__main__':
    lineas: List[str] = sys.stdin.readlines()
    numero_edificios: int = int(lineas[0].rstrip("\n"))
    edificios: List[int] = []
    for a in range(numero_edificios):
        edificios.append(int(lineas[a+1].rstrip("\n")))

    solucion = busca_edificios(edificios)
    if solucion is None or solucion[3] <= 0:
        print("NO HAY SOLUCIÓN")
    else:
        print(str(solucion[0]) + " " + str(solucion[1]) + " " + str(solucion[2]) + " " + str(solucion[3]))
