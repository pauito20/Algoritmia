from algoritmia.datastructures.digraphs import UndirectedGraph

from bt_scheme import *

def sumandos_solver(problema: List[List[int]], S: int) -> List[List[int]]:
    class BuscaSumandoPS(PartialSolution):
        def __init__(self, res: Tuple[int]):
            self.suma = sum(res)
            self.res = res
            self.n = len(res)
            '''
            print("-" * 10)
            print("suma:", self.suma)
            print("res:", self.res)
            print("n:", self.n)
            print("-" * 10)
            '''

        def is_solution(self) -> bool:
            return self.n == len(problema) and self.suma == S

        def get_solution(self) -> Solution:
            return self.res

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n < len(problema):
                actual = problema[self.n]
                for num in actual:
                    if self.suma + num <= S:
                        copia_res = self.res + (num,)
                        yield BuscaSumandoPS(copia_res)

    initial_ps = BuscaSumandoPS(())
    res = []
    for sol in BacktrackingSolver.solve(initial_ps):
        res.append(sol)
    return res

if __name__ == '__main__':
    L = [[4, 2], [10, 6], [8, 2]]
    N = 16

    solucion = sumandos_solver(L, N)

    print(solucion)