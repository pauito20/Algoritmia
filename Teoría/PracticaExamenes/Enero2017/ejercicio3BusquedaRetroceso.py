from bt_scheme import *

def particionesSolver(C: List[int], S:int):
    class ParticionesConjuntoPS(PartialSolution):

        def __init__(self, decisions, pendiente):
            self.decisions = decisions
            self.pendiente = pendiente
            self.n = len(decisions)

            print("decisions: ", decisions)


        def is_solution(self) -> bool:
            return self.n == len(C) and sum(self.pendiente) == 0

        def get_solution(self) -> Solution:
            return self.decisions

        def successors(self) -> Iterable["ParticionesConjuntoPS"]:
            if self.n < len(C):
                for subc in range(S):
                    if C[self.n] <= self.pendiente[subc]:
                        self.pendiente[subc] -= C[self.n]
                        yield ParticionesConjuntoPS(self.decisions + (subc, ), self.pendiente)
                        self.pendiente[subc] += C[self.n]

    initialPS = ParticionesConjuntoPS((), [sum(C)//S]*S)
    return BacktrackingSolver.solve(initialPS)


if __name__ == "__main__":

    C = [2, 4, 5, 9, 6, 7, 0, 3]
    S = 4

    for sol in particionesSolver(C, S):
        print("Para el conjunto {} hay {} subconjuntos cuya suma es {}. Son {} \n"
              .format(C, S, sum(C)//S, sol))

