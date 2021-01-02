from Practicas.Problemas.Practica3Pau.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, \
    Solution
from typing import *
from random import random, seed


def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, res: Tuple[int, ...], peso: float,
                     valor: float):  # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.n = len(res)
            self.peso = peso
            self.res = res
            self.valor = valor
            '''
            print(" ------------ ")
            print("Usados: ", self.res)
            print("Longitud: ", self.n)
            print("Valor mochila: ", self.valor)
            print("Peso: ", self.peso)
            print("Capacity", capacity)
            print("Pesos: ", weights)
            print("Values: ", values)
            print(" ------------ ")
            '''

        def is_solution(self) -> bool:  # IMPLEMENTAR
            return self.n == len(values)

        def get_solution(self) -> Solution:  # IMPLEMENTAR
            return self.res

        def successors(self) -> Iterable["KnapsackPS"]:  # IMPLEMENTAR
            if self.n < len(values) and self.peso < capacity:
                peso_nuevo = self.peso + weights[self.n]
                valor_nuevo = self.valor + values[self.n]
                if peso_nuevo <= capacity:
                    yield KnapsackPS(self.res + (1,), peso_nuevo, valor_nuevo)
                else:
                    yield KnapsackPS(self.res + (0,), self.peso, self.valor)
            yield KnapsackPS(self.res + (0,), self.peso, self.n )

        def state(self) -> State:  # IMPLEMENTAR
            return self.n

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -self.valor

    initialPS = KnapsackPS((), 0, 0)  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    seed(42)
    weights = [int(random() * 1000 + 1) for _ in range(num_objects)]
    values = [int(random() * 1000 + 1) for _ in range(num_objects)]
    capacity = sum(weights) // 2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7  # SOLUCIÓN: Weight=7,    Value=9
    # W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        w = sum(W[i] * m for i, m in enumerate(sol))
        v = sum(V[i] * m for i, m in enumerate(sol))
        print(f"Weight = {w} Values ={v}")
        print(sol)
    print("\n<TERMINADO>")
    tupla1 = (0, 0)

    print((tupla1[0] - 1, tupla1[1]))