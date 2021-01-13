from typing import List


def cuerdasMAxBeneficio(M: int, L: List[int], B: List[int], P: List[int], ):
    indicesBenMax = sorted(range(len(B)), key=lambda i: -B[i])
    res = [0]*len(P)
    while M > 0:
        print(M)
        for i in indicesBenMax:
            if P[i] != 0:
                p = P[i]
                while p > 0:
                    if M - L[i] >= 0:
                        M -= L[i]
                        res[i] += 1
                        p -= 1
                    else:
                        break
        else:
            break
    return res


def ryv (V :List[int], x : int):
    def _ryv(i: int, j: int, veces: int):
        if i == j:
            return veces
        mitad = len(V) // 2
        izq = _ryv(i, mitad, veces)
        der = _ryv(mitad + 1, j, veces)

        for e in V:
            if e == x:
                veces += 1

        return max(izq + der, veces)

    veces = 0
    return _ryv(0, len(V), veces)



if __name__ == '__main__':

    M = 10
    L = [2.0, 9.6, 4.2]
    B = [2, 9, 1]
    V = [2, 4, 3, 2, 3, 4, 2]
    P = [ 5, 2, 1]

    print(ryv(V,2))

    '''
    print(cuerdasMAxBeneficio(M, L, B, P))

    for i in range(len(B)):
        print(i)

    print(len(B))
    '''
