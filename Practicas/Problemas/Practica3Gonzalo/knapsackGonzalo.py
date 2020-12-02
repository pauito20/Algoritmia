from Practicas.Problemas.Practica3Gonzalo.bt_schemeGonzalo import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed

def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, pendiente: int, usados : Tuple[int, ...], valor : int): # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.pendiente = pendiente    #lo que falta para completar la machila
            self.usados = usados    #decisiones tomadas
            self.n = len(usados)    #longitud de las decisiones tomadas
            self.valor = valor      #valor de la mochila

            print(" ------------ ")
            print("Pendiente: ",self.pendiente)
            print("Usados: ", self.usados)
            print("Longitud: ", self.n)
            print("Valor mochila: ",self.valor)
            print(" ------------ ")

        def is_solution(self) -> bool:      # IMPLEMENTAR
            return self.n == len(values)

        def get_solution(self) -> Solution: # IMPLEMENTAR
            return self.usados

        def successors(self) -> Iterable["KnapsackPS"]:# IMPLEMENTAR
            if self.n < len(weights):
                yield KnapsackPS(self.pendiente, self.usados + (0,), self.valor)
                if weights[self.n] <= self.pendiente:
                    newPendiente = self.pendiente - weights[self.n]
                    newValor =  self.valor + values[self.n]
                    yield KnapsackPS(newPendiente, self.usados + (1,), newValor)

        def state(self) -> State:           # IMPLEMENTAR
            return (self.pendiente, self.n)

        def f(self) -> Union[int, float]:   #Es la funcion que queremos optimizar
            return -self.valor
            #return -sum(self.usados[i] * values[i] for i in range(len(self.usados)))     #obtenemos elm valor de la mochila ( el - para maximizar )

    initialPS = KnapsackPS(capacity, (), 0)                # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)

def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int,...], Tuple[int,...], int]:
    seed(42)
    weights = [int(random()*1000+1) for _ in range(num_objects)]
    values = [int(random()*1000+1) for _ in range(num_objects)]
    capacity = sum(weights)//2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7     # SOLUCIÓN: Weight=7,    Value=9
    # W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        w = sum(W[i] * m for i, m in enumerate(sol))
        v = sum(V[i] * m for i, m in enumerate(sol))
        print(f"Weight = {w} Values ={v}")
        print (sol)
    print("\n<TERMINADO>")
    tupla1 = (0, 0)

    print((tupla1[0]-1, tupla1[1]))