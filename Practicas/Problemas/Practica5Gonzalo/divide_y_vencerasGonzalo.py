from typing import List, Optional


def punto_fijo(v : List[int]) -> Optional[int]:
    def puntoFijoFun(i: int, j: int) -> Optional[int]:

        if i == j:
            return None

        punto_medio = (i + j) // 2

        if v[punto_medio] == punto_medio:
            return punto_medio

        if v[punto_medio] > punto_medio:
            return puntoFijoFun(i, punto_medio)

        return puntoFijoFun(punto_medio + 1, j)

    return puntoFijoFun(0, len(v))



if __name__ == '__main__':

    v1 = [2, 3, 4, 5, 6, 7]
    v2 = [0, 3, 6, 5, 8, 7]
    v3 = [2, 3, 4, 5, 6, 7]
    v4 = [-12, 1, 4, 5, 8, 11]

    print(punto_fijo(v1))
    print(punto_fijo(v2))
    print(punto_fijo(v3))
    print(punto_fijo(v4))
