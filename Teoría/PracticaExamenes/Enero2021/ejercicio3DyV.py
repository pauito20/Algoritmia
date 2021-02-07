from typing import List


def num_falta(v: List[int]):
    def R(b, e):
        tam = e - b

        if tam <= 1:
            if v[b] == b:
                return b+1
            else:
                return b
        else:
            medio = (b+e)//2

            if v[medio] == medio:
                return R(medio, e)

            if v[medio-1] == medio-1:
                return medio

            return R(b, medio)

    return R(0, len(v))

if __name__ == "__main__":
    V = [0, 1, 2, 3, 4, 5, 7, 8, 9]
    print(num_falta(V))