from typing import List, Tuple


def suma_max(a: List[int]) -> Tuple[int, int, int]:
    def rec(b: int, e: int) -> Tuple[int, int, int]:
        num_elem = e-b
        if num_elem == 0:
            return 0, 0, 0
        if num_elem == 1:               # is_simple, caso para vector vacio
            return a[b], b, b+1         # trivial_solution
        else:                           # decrease
            h = (b + e)//2
            print("centro = ", h)
            mejor_izq = rec(b, h)
            mejor_der = rec(h, e)

            # para calcular el mejor del centro

            # dos bucles while, uno hacia cada lado desde el centro, sumando
            # cada bucle para cuando encuentra uno negativo
            indice_izq = h-1
            suma_mejor_izq = a[indice_izq]
            while indice_izq > 0:
                if suma_mejor_izq + a[indice_izq-1] >= suma_mejor_izq:
                    indice_izq -= 1
                    suma_mejor_izq += a[indice_izq]
                else:
                    break

            indice_der = h
            suma_mejor_der = a[indice_der]
            while indice_der < e-1:
                if suma_mejor_der + a[indice_der + 1] >= suma_mejor_der:
                    indice_der += 1
                    suma_mejor_der += a[indice_der]
                else:
                    break

            mejor_centro = suma_mejor_izq + suma_mejor_der, indice_izq, indice_der+1
            print("-"*10)
            print("Mejor derecha: ", mejor_der)
            print("Mejor izquierda: ", mejor_izq)
            print("Mejor centro: ", mejor_centro)
            print("_"*10)
            return max(mejor_izq, mejor_der, mejor_centro)

    return rec(0, len(a))

if __name__ == "__main__":
    print("######################### Sol 1 ##############################")
    print(suma_max([1, 1, 1, 1]))
    print("######################### Sol 2 ##############################")
    print(suma_max([1, -1, 1, -1, 1, 2, 3]))
    print("######################### Sol 3 ##############################")
    print(suma_max([1, 1, -1, -1, 1, 1, 1, 1]))
