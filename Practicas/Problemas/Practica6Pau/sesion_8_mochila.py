from typing import *


# Versión recursiva directa
def mochila_rec(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0: #Caso base, no hay elementos
            return 0
        if w[n-1] <= c: #Objeto cabe en la mochila, vemos el máximo beneficio
            return max(B(n-1, c), B(n-1, c-w[n-1])+v[n-1])
        else: # Objeto no cabe en la mochila
            return B(n-1, c)

    N = len(v)
    return B(N, C)


# Versión recursiva con memoización
def mochila_rec_mem(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0:  # Caso base, no hay elementos
            return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:  # Objeto cabe en la mochila, vemos el máximo beneficio
                mem[n, c] = max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
            else:  # Objeto no cabe en la mochila
                mem[n, c] = B(n - 1, c)
        return mem[n, c]

    N = len(v)
    #Mem nos servirá para no calcular más veces algo que ya hemos calculado
    mem = {}
    return B(N, C)


# Versión recursiva con memoización y recuperación de camino
def mochila_rec_mem_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    def B(n: int, c: int) -> int:
        if n == 0:  # Caso base, no hay elementos
            return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:  # Objeto cabe en la mochila, vemos el máximo beneficio
                mem[n, c] = max((B(n - 1, c), (n-1, c, 0)),
                                    (B(n - 1, c - w[n - 1]) + v[n - 1], (n-1, c-w[n-1], 1)))
            else:  # Objeto no cabe en la mochila
                mem[n, c] = B(n - 1, c), (n-1, c, 0)
        return mem[n, c][0]

    N = len(v)
    mem = {}
    score = B(N, C)
    sol = []
    n, c = N, C
    while n != 0:
        _, (n_prev, c_prev, x) = mem[n, c] #Nos interesa la x que e sla decisión tomada para ponerla en "sol"
        n, c = n_prev, c_prev
        sol.append(x)
    sol.reverse()
    return score, sol


# Versión iterativa con recuperación de camino
def mochila_iter_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(v)  # número de objetos
    # --------------------
    # TODO: IMPLEMENTAR rellenar tabla mem
    for c in range(C + 1):
        mem[0, c] = 0, None
    for n in range(1, N+1):
        for c in range(C + 1):
            if w[n - 1] <= c:  # Objeto cabe en la mochila, vemos el máximo beneficio
                mem[n, c] = max((mem[n - 1, c][0], (n-1, c, 0)),
                                    (mem[n - 1, c - w[n - 1]][0] + v[n - 1], (n-1, c-w[n-1], 1)))
            else:  # Objeto no cabe en la mochila
                mem[n, c] = mem[n - 1, c][0], (n-1, c, 0)


    # --------------------
    score = mem[N, C][0] # TODO: Cambiar por mem[N, C][0]
    sol = []
    n, c = N, C
    # --------------------
    # TODO: IMPLEMENTAR recuperación de camino en sol
    while n != 0:
        _, (n, c, x) = mem[n, c] #Nos interesa la x que e sla decisión tomada para ponerla en "sol"
        sol.append(x)
    sol.reverse()
    # --------------------
    return score, sol


# Versión iterativa con reduccion del coste espacial
'''
Para esto no debe interesarnos el camino y que además cada fila dependa de la anterior unicamente no de
varias anteriormente. Es un tipo de optimización que ahorra mucho espacio, sin embargo, no siempre es posible.
'''

def mochila_iter_reduccion_coste(v: List[int], w: List[int], C: int) -> int:
    N = len(v)  # número de objetos
    current = [0] * (C + 1)
    previous = [None] * (C + 1)
    # --------------------
    # TODO: IMPLEMENTAR usar dos columnas para rellenar la última de la tabla
    for n in range(1, N + 1):
        current, previous = previous, current
        for c in range(C + 1):
            if w[n - 1] <= c:  # Objeto cabe en la mochila, vemos el máximo beneficio
                current[c] = max( previous[c],
                                  previous[c - w[n-1]] + v[n-1])
            else:  # Objeto no cabe en la mochila
                current[c] = previous[c]
    # --------------------
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
