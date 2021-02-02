from typing import List


def numero_repeticiones(v: List[int], x: int):
    def R(b, e):
        tam = e - b
        if tam <= 1:
            if v[b] == x:
               return b
            else:
                return -1

        else:
            medio = (b+e) // 2
            if v[medio] != x:
                return R(medio, e)
            if v[medio] == x:
                return medio
            return R(b, medio)

    cant_x = 0
    esta = True

    while esta:
        i = R(0, len(v))

        if v[i] == x:
            v.__delitem__(i)
            cant_x += 1
        else:
            esta = False

    return cant_x


if __name__ == "__main__":
    vec = [-5, -5, 1, 1, 2, 2, 2, 2, 4, 4, 4, 7]
    num = 4

    print("Dado el vector {} el número {} se repite {} veces".format(vec, num, numero_repeticiones(vec, num)))


