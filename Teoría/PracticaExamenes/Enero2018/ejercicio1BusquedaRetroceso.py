from typing import List, Tuple, Iterable, Union
from Utils import bt_scheme
from bt_scheme import PartialSolutionWithOptimization, Solution, State, BacktrackingOptSolver


def valladoSolver(M:int, L:List[int], C:List[int], P:List[int]):
    class ValladoPS(PartialSolutionWithOptimization):

            def __init__(self, decisions, pendiente, coste):
                self.decisions = decisions
                self.pendiente = pendiente
                self.coste = coste
                self.n = len(decisions)

            def is_solution(self) -> bool:
                return self.pendiente == 0 and self.n == len(L)

            def get_solution(self) -> Solution:
                return self.decisions

            def successors(self) -> Iterable["ValladoPS"]:
                if self.n < len(L):
                    for i in range(C[self.n]):
                        if L[self.n]*i <= self.pendiente:
                            yield ValladoPS(self.decisions+(i,), self.pendiente-L[self.n]*i, self.coste+P[self.n]*i)

            def state(self) -> State:
                return self.n, self.pendiente

            def f(self) -> Union[int, float]:
                return self.coste

    initialPS = ValladoPS((), M, 0)

    return BacktrackingOptSolver.solve(initialPS)


if __name__ == "__main__":
    M, L, C, P, = 10, [2, 4, 6, 7], [1, 2, 3, 4], [1, 2, 3, 4]
    for sol in valladoSolver(M, L, C, P):
        print(sol)