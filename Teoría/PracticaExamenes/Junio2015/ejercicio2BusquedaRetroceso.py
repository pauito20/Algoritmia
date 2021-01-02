
from algoritmia.datastructures.digraphs import UndirectedGraph

from bt_scheme import *


def ciclo_hamiltoniano_solver(g: UndirectedGraph):
    class CicloHamiltonianoPS(PartialSolutionWithVisitedControl):

        def __init__(self, visitados: Tuple[int, ...]):
            self.visitados = visitados
            self.n = len(visitados)
            '''
            print("-" * 10)
            print(self.visitados)
            print(self.n)
            print("-" * 10)
            '''


        def is_solution(self) -> bool:
            return self.n == len(g.V)

        def get_solution(self) -> Solution:
            return self.visitados

        def successors(self) -> Iterable["PartialSolutionWithVisitedControl"]:
            if self.n <= len(g.V):
                actual = self.visitados[self.n-1]
                for suc in g.succs(actual):
                    if suc not in self.visitados:
                        yield CicloHamiltonianoPS(self.visitados+(suc,))

        def state(self) -> State:
            return self.n

    print("Vertices: ", G.V)
    print("Aristas: ", G.E)

    initialPS = CicloHamiltonianoPS((1,))
    return BacktrackingVCSolver.solve(initialPS)


if __name__ == '__main__':
    G = UndirectedGraph(V=[1, 2, 3, 4], E=[(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 4)])
    soluçao = []
    for sol in ciclo_hamiltoniano_solver(G):
        soluçao = sol
    if len(soluçao) == 0:
        print("NO HAY SOLUCIÓN")
    else:
        print("Solución: ", soluçao)


