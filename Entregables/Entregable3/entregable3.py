import os
import sys
from typing import *

from typing import Tuple

from Teoría.bt_scheme import PartialSolution, Solution, BacktrackingSolver, State

Pos = Tuple[int, int]


def puzleSolver(matrizMapa , player_pos : Tuple[int, ...], boxes_start : List[Tuple[int, int]], boxes_end : List[Tuple[int, int]], maximoMovimientos : int ):
    class puzlePS(PartialSolution):
        def __init__(self, decisiones: List[str], posActualPlayer: Tuple[int, ...], posActualBoxes : List[Tuple[int, int]] ):
            self.decisiones = decisiones
            self.posActualPlayer = posActualPlayer
            self.posActualBoxes = posActualBoxes
            self.n = len(decisiones)

        def is_solution(self) -> bool:
            return self.n <= maximoMovimientos and self.posActualBoxes == boxes_end

        def get_solution(self) -> Solution:
            return self.decisiones

        def successors(self) -> Iterable["puzlePS_Lista"]:
            if self.n <= maximoMovimientos:
                #IZQUIERDA
                leftPos = tuple[self.posActualPlayer[0] - 1, self.posActualPlayer[1]]
                if leftPos == self.posActualBoxes[0]:
                    leftBox = tuple[leftPos[0] - 1, leftPos[1]]
                    if matrizMapa[leftBox[0]][leftBox[1]] == " ":
                        self.posActualBoxes[0] = leftBox
                        yield puzlePS(self.decisiones.append("L"), leftPos, self.posActualBoxes)
                elif leftPos == self.posActualBoxes[1]:
                    leftBox = Tuple[leftPos[0] - 1, leftPos[1]]
                    if matrizMapa[leftBox[0]][leftBox[1]] == " ":
                        self.posActualBoxes[1] = leftBox
                        yield puzlePS(self.decisiones.append("L"), leftPos, self.posActualBoxes)
                else:
                    if matrizMapa[leftPos[0], leftPos[1]] != "#":
                        yield puzlePS(self.decisiones.append("L"), leftPos, self.posActualBoxes)

                #DERECHA
                rightPos = Tuple[self.posActualPlayer[0] + 1, self.posActualPlayer[1]]
                if rightPos == self.posActualBoxes[0]:
                    rightBox = Tuple[rightPos[0] + 1, rightPos[1]]
                    if matrizMapa[rightBox[0]][rightBox[1]] == " ":
                        self.posActualBoxes[0] = rightBox
                        yield puzlePS(self.decisiones.append("R"), rightPos, self.posActualBoxes)
                elif rightPos == self.posActualBoxes[1]:
                    rightBox = Tuple[rightPos[0] + 1, rightPos[1]]
                    if matrizMapa[rightBox[0]][rightBox[1]] == " ":
                        self.posActualBoxes[1] = rightBox
                        yield puzlePS(self.decisiones.append("R"), rightPos, self.posActualBoxes)
                else:
                    if matrizMapa[rightPos[0], rightPos[1]] != "#":
                        yield puzlePS(self.decisiones.append("R"), rightPos, self.posActualBoxes)

                #ARRIBA
                upPos = Tuple[self.posActualPlayer[0], self.posActualPlayer[1] + 1]
                if upPos == self.posActualBoxes[0]:
                    upBox = Tuple[upPos[0], upPos[1] + 1]
                    if matrizMapa[upBox[0]][upBox[1]] == " ":
                        self.posActualBoxes[0] = upBox
                        yield puzlePS(self.decisiones.append("U"), upPos, self.posActualBoxes)
                elif upPos == self.posActualBoxes[1]:
                    upBox = Tuple[upPos[0], upPos[1] + 1]
                    if matrizMapa[upBox[0]][upBox[1]] == " ":
                        self.posActualBoxes[1] = upBox
                        yield puzlePS(self.decisiones.append("U"), upPos, self.posActualBoxes)
                else:
                    if matrizMapa[upPos[0], upPos[1]] != "#":
                        yield puzlePS(self.decisiones.append("U"), upPos, self.posActualBoxes)

                # ABAJO
                downPos = Tuple[self.posActualPlayer[0], self.posActualPlayer[1] - 1]
                if upPos == self.posActualBoxes[0]:
                    downBox = Tuple[downPos[0], downPos[1] - 1]
                    if matrizMapa[downBox[0]][downBox[1]] == " ":
                        self.posActualBoxes[0] = downBox
                        yield puzlePS(self.decisiones.append("D"), downPos, self.posActualBoxes)
                elif downPos == self.posActualBoxes[1]:
                    downBox = Tuple[downPos[0], downPos[1] - 1]
                    if matrizMapa[downBox[0]][downBox[1]] == " ":
                        self.posActualBoxes[1] = downBox
                        yield puzlePS(self.decisiones.append("D"), downPos, self.posActualBoxes)
                else:
                    if matrizMapa[downPos[0], downPos[1]] != "#":
                        yield puzlePS(self.decisiones.append("D"), downPos, self.posActualBoxes)

    '''
        def state(self) -> State:  
           return (self.posActualPlayer, self.n)
       
        def f(self) -> Union[int, float]:   #Es la funcion que queremos optimizar
            return self.n
    '''



    initial_ps = puzlePS([], player_pos, boxes_start)
    return BacktrackingSolver.solve(initial_ps)

def contruyeMatriz(levelMap):
    m = []
    for i in range(len(level_map)):
        fila = []
        for c in str(level_map[i]):
            fila.append(c)
        m.append(fila)
    return m

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


    numMaxMovimientos = int ( input("Introduce el numero maximo de movimientos: ") )
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

    res = []

    matrizMapa = contruyeMatriz(level_map)

    for sol in puzleSolver( matrizMapa , player_pos , boxes_start , boxes_end, numMaxMovimientos):
        res.append(sol)

    print(sol)



