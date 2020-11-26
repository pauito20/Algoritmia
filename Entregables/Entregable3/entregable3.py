import os
import sys
from typing import *
from Teoría.bt_scheme import PartialSolution, Solution, BacktrackingSolver

Pos = Tuple[int, int]

def puzleSolver(level_map : List[str], player_pos : Tuple[int, ...], boxes_start : Tuple[Tuple[int, ...], ...], boxes_end : Tuple[Tuple[int, ...], ...], maximoMovimientos : int ):
    class puzlePS(PartialSolution):
        def __init__(self, decisiones: Tuple[str, ...], pendiente: int, posActualPlayer: Tuple[int, ...], posActualBoxes : Tuple[Tuple[int, ...], ...] ):
            self.decisiones = decisiones
            self.pendiente = pendiente
            self.posActualPlayer = posActualPlayer
            self.posActualBoxes = posActualBoxes
            self.n = len(decisiones)

        def is_solution(self) -> bool:
            return self.pendiente == 0 and self.n <= maximoMovimientos

        def get_solution(self) -> Solution:
            return self.decisiones

        def successors(self) -> Iterable["NQueensPS_lista"]:
            if self.n < maximoMovimientos:
                pass



    initial_ps = puzlePS((), maximoMovimientos, player_pos, boxes_start)
    return BacktrackingSolver.solve(initial_ps)


def read_level(puzle_lines: List[str]) -> Tuple[List[str], Pos, List[Pos], List[Pos]]:

    # Averigua la posición del jugador y las posiciones iniciales y finales de las cajas
    player_pos, boxes_start, boxes_end = None, [], []
    num_rows = len(puzle_lines)
    num_cols = len(puzle_lines[0].strip())

    for r in range(num_rows):
        for c in range(num_cols):
            if puzle_lines[r][c] == 'p':
                player_pos = (r, c)
            elif puzle_lines[r][c] == 'o':
                boxes_start.append((r, c))
            elif puzle_lines[r][c] == 'x':
                boxes_end.append((r, c))

    # Crea un mapa (incluye únicamente paredes y pasillos, borra 'p','x' y 'o'):
    tr = str.maketrans("pxo", "   ")
    level_map = []
    for l in puzle_lines:
        level_map.append(l.strip().translate(tr))

    return  level_map, player_pos, boxes_start, boxes_end




if __name__ == '__main__':


    numMaxMovimientos = input("Introduce el numero maximo de movimientos: ")
    name_fich = input("Introduce el nombre(ruta) del fichero: ")

    if not os.path.isfile(name_fich):
        print("El parametro introducido(", name_fich, ") no es un fichero.")
        exit(0)


    file = open(name_fich, "r")
    puzle = []
    linea = str(file.readline())

    while linea != "":
        puzle.append(linea)
        linea = str(file.readline())

    '''
    #Creamos un entero para almacenar el numero maximos de movimientos
    numMaxMovimientos = int(sys.argv[1])

    #Convertimos el fichero en una lista de líneas
    puzle = sys.stdin.readlines()
    '''

    level_map, player_pos, boxes_start, boxes_end = read_level(puzle)

    res=[]

    print(level_map)
    print(player_pos)
    print(boxes_start)
    print(boxes_end)

    for sol in puzleSolver():
        res.append(sol)

    print(sol)
