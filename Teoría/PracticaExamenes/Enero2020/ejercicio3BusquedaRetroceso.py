from bt_scheme import *

def dominoSolver(F:List[Tuple[int,int]]):
    class CadenaDominoPS(PartialSolution):

        def __init__(self, decisions, a):
            self.decisions = decisions
            self.n = len(decisions)
            self.a = a



        def is_solution(self) -> bool:
            return self.n == len(F)

        def get_solution(self) -> Solution:
            return self.decisions

        def successors(self) -> Iterable["CadenaDominoPS"]:
            if self.n < len(F):
                for i in range(len(F)):
                    if self.n == 0:
                        yield CadenaDominoPS(self.decisions+(F[i],), F[i])
                    else:
                        if self.a[1] == F[i][0] and F[i] not in self.decisions:
                            yield CadenaDominoPS(self.decisions+(F[i],), F[i])
                        elif self.a[1] == F[i][1] and F[i] not in self.decisions:
                            yield CadenaDominoPS(self.decisions+((F[i][1], F[i][0]), ), (F[i][1], F[i][0]))

    initialPS = CadenaDominoPS((), ())
    return BacktrackingSolver.solve(initialPS)


if __name__ == "__main__":
    F = [(2, 3), (1, 6), (3, 3), (3, 6), (2, 6)]

    num_sol = 0

    for sol in dominoSolver(F):
        print(sol)
        num_sol += 1
    print("Hay {} soluciones".format(num_sol))


