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


def dyv (vieja: List[int], nueva: List[int]):
    def _dyv(i_iniV, i_finV, i_iniN, i_finN):
        centroV = (i_iniV + i_finV) // 2
        centroN = (i_iniN + i_finN) // 2
        resIzq = _dyv(i_iniV, centroV, i_iniN, centroN)
        resDer = _dyv(centroV + 1, i_finV, centroN + 1, i_finN)

        if vieja[centroV] > nueva[centroN]:
            pass


    return _dyv(0, len(vieja) -1, 0, len(nueva) -1)



if __name__ == '__main__':

    M = 10
    L = [2, 9, 4]
    B = [2, 9, 1]

    P = [ 5, 2, 1]

    print(cuerdasMAxBeneficio(M, L, B, P))

    for i in range(len(B)):
        print(i)

    print(len(B))