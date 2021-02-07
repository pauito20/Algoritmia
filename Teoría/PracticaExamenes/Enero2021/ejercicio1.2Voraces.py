from typing import List


def voraz_tienda(C: int, b: List[int], p: List[int], m: List[int]) -> List[int]:
        indices_ordenados = sorted(range(len(b)), key=lambda i: -(b[i]))
        sol = [0] * len(b)
        for i in indices_ordenados:
            print(i, m[i])
            if m[i] > 0:
                for u in range(m[i], -1, -1):
                    if u * p[i] <= C:
                        sol[i] += u
                        C -= u * p[i]
                        break
        return sol

if __name__ == "__main__":
    P, B, M, C, = [1, 2, 3, 4], [1, 2, 3, 4], [4, 3, 2, 1], 10

    print(voraz_tienda(C, B, P, M))