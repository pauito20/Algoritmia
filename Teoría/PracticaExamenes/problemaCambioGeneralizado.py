from typing import List

from bt_scheme import infinity


def problemaCambio(Q:int, v:List[int], w:List[int]):
    def L(n,q):
        if n == 0 and q == 0:
            return 0
        if n == 0 and q > 0:
            return infinity
        else:
            if (n, q) not in mem:
                mem[n, q] = min(((L(n-1, q-d*v[n-1]) + d*w[n-1]), (d, n-1, q-d*v[n-1])) for d in range(0, abs(q//v[n-1])+1))
            return mem[n, q][0]

    mem = {}
    n, q = len(v), Q
    score = L(n,q)
    sol = []

    while n != 0:
        _, (d, n, q) = mem[n, q]
        sol.append(d)
    sol.reverse()
    return score, sol


if __name__ == "__main__":
    Q = 24
    v = [1, 2, 5, 10]
    w = [1, 2, 4, 5]

    print(problemaCambio(Q, v, w))