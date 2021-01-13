from typing import *


# Versión recursiva directa
def mochila_rec(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0:
            return 0
        if n > 0 and w[n - 1] <= c:
            return max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
        if n > 0 and w[n - 1] > c: #Puede ponerse como un else ya que n nunca pude ser menor que 0 y ya esta comprobado antes
            return B(n - 1, c)
    N = len(v)
    return B(N, C)


# Versión recursiva con memoización
def mochila_rec_mem(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        print(mem)
        if n == 0:
            return 0
        if (n, c) not in mem:
            if n > 0 and w[n - 1] <= c:
                mem[n, c] = max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
            else:
                mem[n, c] = B(n - 1, c)
        return mem[n, c]
    N = len(v)
    mem = {}
    return B(N, C)


# Versión recursiva con memoización y recuperación de camino
#Vamos a guardarno
#mem[3, 5] = (100, (2, 5, 1))
#el 100 es el beneficio, el 2 es n -1, el 5 es w de n -1, y el 1 es x de n PARA EL CASO DE HABERLO METIDO
#mem[3, 5] = (100, (2, 10, 0))
#el 100 es el beneficio, el 2 es n -1, el 10 es w de n -1, y el 0 es x de n PARA EL CASO DE NO HABERLO METIDO
def mochila_rec_mem_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    def B(n: int, c: int) -> int:
        if n == 0:
            return 0
        if (n, c) not in mem:
            if n > 0 and w[n - 1] <= c:
                mem[n, c] = max((B(n - 1, c), (n -1, c, 0)),
                                (B(n - 1, c - w[n - 1]) + v[n - 1], (n - 1, c - w[n - 1], 1)))
            else:
                mem[n, c] = ( B(n - 1, c), (n -1, c, 0) )
        return mem[n, c][0]
    N = len(v)
    mem = {}
    score = B(N, C)
    sol = []
    n, c = N, C
    while n != 0:
        _, (n, c, x) = mem[n, c]
        sol.append(x)
    sol.reverse()
    return score, sol


# Versión iterativa con recuperación de camino
def mochila_iter_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(v)  # número de objetos
    for c in range(C + 1):
        mem[0, c] = 0, None
    for n in range(1, N + 1):
        for c in range(C + 1):
            if w[n - 1] <= c:
                mem[n, c] = max((mem[n - 1, c][0], (n - 1, c, 0)),
                                (mem[n - 1, c - w[n - 1]][0] + v[n - 1], (n - 1, c - w[n - 1], 1)))
            else:
                mem[n, c] = mem[n - 1, c][0], (n - 1, c, 0)

    score = mem[N, C][0]  # TODO: Cambiar por mem[N, C][0]
    sol =[]
    n, c = N, C
    while n != 0:
        _, (n, c, x) = mem[n, c]
        sol.append(x)
    sol.reverse()

    return score, sol


# Versión iterativa con reduccion del coste espacial

def mochila_iter_reduccion_coste(v: List[int], w: List[int], C: int) -> int:
    N = len(v)  # número de objetos
    current = [0] * (C + 1)
    previous = [None] * (C + 1)
    for n in range(1, N + 1):
        current, previous = previous, current
        for c in range(C + 1):
            if w[n - 1] <= c:
                current[c] = max(previous[c],
                                previous[c - w[n - 1]] + v[n - 1])
            else:
                current[c] = previous[c]

    return current[C]


# PROGRAMA PRINCIPAL -------------------------------------------------------------------------
if __name__ == "__main__":
    values = [90, 75, 60, 20, 10]
    weights = [4, 3, 3, 2, 2]
    capacity = 6

    print("Versión recursiva:")
    print(mochila_rec(values, weights, capacity))
    print()
    print("Versión recursiva con memoización:")
    print(mochila_rec_mem(values, weights, capacity))
    print()
    print("Versión recursiva con memoización y recuperación de camino:")
    print(mochila_rec_mem_camino(values, weights, capacity))
    print()
    print("Versión iterativa con recuperación de camino:")
    print(mochila_iter_camino(values, weights, capacity))
    print()
    print("Versión iterativa con reduccion del coste espacial:")
    print(mochila_iter_reduccion_coste(values, weights, capacity))
