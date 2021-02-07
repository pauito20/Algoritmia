from typing import List


def minimo_local(v :List[int]):
    def R(b, e):
        tam = e - b
        if tam == 3:
            if v[b] > v[b+1] and v[b] < v[b+1]:
                return b+1
        else:
            medio = (b+e) // 2
            if v[medio-1] < v[medio]:
                return R(b, medio)
            if v[medio] < v[medio+1]:
                return medio
            return R(medio, e)

    return R(0, len(v))

if __name__ == "__main__":
    v = [9, 5, 1, 4, 8]

    print("Pos: ", minimo_local(v), "Elem: ", v[minimo_local(v)])