from typing import Tuple, List

from bt_scheme import infinity


def desglose_recuperacion_camino(Q: int, v: List[int], m: List[int], w: List[int]) -> Tuple[int, List[int]]:
    def L(q, n):

        if n == 0 and q == 0:
            return 0
        if q > 0 and n == 0:
            return infinity
        else:
            if (q, n) not in mem:
                mem[q, n] = min([L(q-i*v[n-1], n-1)+i * w[n-1], (i, q-i*v[n-1], n-1)]  for i in
                                 range(min(m[n-1], abs(q//v[n - 1]))+1)
                                 )
            return mem[q, n][0]
    mem = {}
    sol = []
    score = L(Q, len(v))
    q, n = Q, len(v)
    while n != 0:
        _, (i, q_prev, n_prev) = mem[q, n]

        sol.append(i)
        q, n = q_prev, n_prev
    sol.reverse()

    return score, sol


if __name__ == "__main__":
    Q = 24
    v = [1, 2, 5, 10]
    m = [3, 1, 4, 1]
    w = [1, 1, 4, 6]

    print(desglose_recuperacion_camino(Q, v, m, w))

