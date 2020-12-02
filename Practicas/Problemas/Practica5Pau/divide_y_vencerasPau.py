from typing import *


def punto_fijo(v: List[int]) -> Optional[int]:
    def punto_fijo_(i: int, j: int) -> Optional[int]:
        #Buscará el punto fijo desde la posición "i" hasta la "j" donde "i" esta incluido y "j" no
        m = (i+j) // 2
        if i == j:
            return None
        if v[m] == m:
            return m
        elif v[m] > m:
            return punto_fijo_(i, m)
        return punto_fijo_(m+1, j)



    #Busco en tot el vector, pero al tener dos parametros "i" i "j" no hay coste
    #En caso de usar listas, el coste aumentaria en memoria ya que se debería almacenar espacio para ello
    return punto_fijo_(0, len(v))


if __name__ == "__main__":
    print(punto_fijo([-10, -5, 1, 3, 6]))
    print(punto_fijo([-10, -5, 1, 2, 6]))
