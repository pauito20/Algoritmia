from typing import List


def numeroFalta(v: List[int]) -> int:
    def N(b, e) -> int:
        tam = e-b
        if tam <= 1:
            if v[b] == b:
                return b+1
            else:
                return b
        else:
            medio = (b+e) // 2

            if medio == v[medio]:
                return N(medio, e)

            if medio - 1 == v[medio-1]:
                return medio

            else:
                return N(b, medio)
    return N(0, len(v))

if __name__ == "__main__":

    vec1 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
    print("El número que falta en el vector {} es {} ".format(vec1, numeroFalta(vec1)))

    vec2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
    print("El número que falta en el vector {} es {} ".format(vec2, numeroFalta(vec2)))



