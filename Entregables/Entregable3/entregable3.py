import sys
from typing import *

from typing import Tuple

from bt_scheme import PartialSolutionWithOptimization, Solution, BacktrackingOptSolver, State

Pos = Tuple[int, int]


def puzleSolver(matrizMapa , player_pos : Tuple[int, ...], boxes_start : List[Tuple[int, int]], boxes_end : List[Tuple[int, int]], maximoMovimientos : int ):
    class puzlePS(PartialSolutionWithOptimization):
        def __init__(self, decisiones: Tuple[str,...], posActualPlayer: Tuple[int, ...], posActualBoxes : List[Tuple[int, int]]):
            self.decisiones = decisiones
            self.posActualPlayer = posActualPlayer
            self.posActualBoxes = posActualBoxes
            self.n = len(decisiones)

            '''
            print("Decisiones: ", self.decisiones)
            print("Posición Actual: ", self.posActualPlayer)
            print("Posición Actual Caja: ", self.posActualBoxes)
            print("Posición Final de la caja: ", boxes_end)
            print("Numero decisiones: ", self.n)
            print("- - - - - - - - - - - - - - -")
            '''




        def is_solution(self) -> bool:
            return self.n <= maximoMovimientos and sonIguales(self.posActualBoxes, boxes_end)

        def get_solution(self) -> Solution:
            return self.decisiones

        def successors(self) -> Iterable["puzlePS_lista"]:

            if self.n < maximoMovimientos:

                upPos = (self.posActualPlayer[0] - 1, self.posActualPlayer[1])
                downPos = (self.posActualPlayer[0] + 1, self.posActualPlayer[1])
                rightPos = (self.posActualPlayer[0], self.posActualPlayer[1] + 1)
                leftPos = (self.posActualPlayer[0], self.posActualPlayer[1] - 1)

                # ARRIBA
                if upPos in self.posActualBoxes:
                    upBox = (upPos[0] - 1, upPos[1])
                    if matrizMapa[int(upBox[0])][int(upBox[1])] != "#" and upBox not in self.posActualBoxes:
                        posicionesBoxes = []
                        for box in self.posActualBoxes:
                            posicionesBoxes.append(box)
                        posicionesBoxes.remove(upPos)
                        posicionesBoxes.append(upBox)
                        if not (upBox not in boxes_end and matrizMapa[upBox[0] - 1][upBox[1]] == "#" and (matrizMapa[upBox[0]][upBox[1] - 1] == "#" or matrizMapa[upBox[0]][upBox[1] + 1] == "#")):
                            yield puzlePS(self.decisiones + ("U",), upPos, posicionesBoxes)
                else:
                    if matrizMapa[int(upPos[0])][int(upPos[1])] != "#":
                        yield puzlePS(self.decisiones + ("U",), upPos, self.posActualBoxes)

                # ABAJO

                if downPos in self.posActualBoxes:
                    downBox = (downPos[0] + 1, downPos[1])
                    if matrizMapa[int(downBox[0])][int(downBox[1])] != "#"  and downBox not in self.posActualBoxes:
                        posicionesBoxes = []
                        for box in self.posActualBoxes:
                            posicionesBoxes.append(box)
                        posicionesBoxes.remove(downPos)
                        posicionesBoxes.append(downBox)
                        if not (downBox not in boxes_end and matrizMapa[downBox[0] + 1][downBox[1]] == "#" and (matrizMapa[downBox[0]][downBox[1] - 1] == "#" or matrizMapa[downBox[0]][downBox[1] + 1] == "#")):
                            yield puzlePS(self.decisiones + ("D",), downPos, posicionesBoxes)
                else:
                    if matrizMapa[int(downPos[0])][int(downPos[1])] != "#":
                        yield puzlePS(self.decisiones + ("D",), downPos, self.posActualBoxes)

                # DERECHA

                if rightPos in self.posActualBoxes:
                    rightBox = (rightPos[0], rightPos[1] + 1)
                    if matrizMapa[int(rightBox[0])][int(rightBox[1])] != "#" and rightBox not in self.posActualBoxes:
                        posicionesBoxes = []
                        for box in self.posActualBoxes:
                            posicionesBoxes.append(box)
                        posicionesBoxes.remove(rightPos)
                        posicionesBoxes.append(rightBox)
                        if not (rightBox not in boxes_end and matrizMapa[rightBox[0]][rightBox[1]+1] == "#" and (matrizMapa[rightBox[0]+1][rightBox[1]] == "#" or matrizMapa[rightBox[0]-1][rightBox[1]] == "#")):
                            yield puzlePS(self.decisiones + ("R",), rightPos, posicionesBoxes)
                else:
                    if matrizMapa[int(rightPos[0])][int(rightPos[1])] != "#":
                        yield puzlePS(self.decisiones + ("R",), rightPos, self.posActualBoxes)

                #IZQUIERDA

                if leftPos in self.posActualBoxes:
                    leftBox = (leftPos[0], leftPos[1]-1)
                    if matrizMapa[int(leftBox[0])][int(leftBox[1])] != "#" and leftBox not in self.posActualBoxes:
                        posicionesBoxes = []
                        for box in self.posActualBoxes:
                            posicionesBoxes.append(box)
                        posicionesBoxes.remove(leftPos)
                        posicionesBoxes.append(leftBox)
                        if not (leftBox not in boxes_end and matrizMapa[leftBox[0]][leftBox[1] - 1] == "#" and (matrizMapa[leftBox[0] - 1][leftBox[1]] == "#" or matrizMapa[leftBox[0] + 1][leftBox[1]] == "#")):
                            yield puzlePS(self.decisiones + ("L",), leftPos, posicionesBoxes)
                else:
                    if matrizMapa[int(leftPos[0])][int(leftPos[1])] != "#":
                        yield puzlePS(self.decisiones + ("L",), leftPos, self.posActualBoxes)



        def state(self) -> State:  
           return(self.posActualPlayer, tuple(self.posActualBoxes))
       
        def f(self) -> Union[int, float]:   #Es la funcion que queremos optimizar
            return self.n



    initial_ps = puzlePS((), player_pos, boxes_start)
    return BacktrackingOptSolver.solve(initial_ps)

def sonIguales (tuplas1:List[Tuple[int, int]], tuplas2:List[Tuple[int, int]]):
    iguales = True
    for e in tuplas1:
        if e not in tuplas2:
            iguales = False
    return iguales

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

    '''
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


    level_map, player_pos, boxes_start, boxes_end = read_level(puzle)

    res = ()

    matrizMapa = contruyeMatriz(level_map)

    haySolucion = False
    solu = None
    for sol in puzleSolver( matrizMapa , player_pos , boxes_start , boxes_end, numMaxMovimientos):
        solu = sol
        haySolucion = True
        break

    res = ""
    if haySolucion:
        for e in solu:
            res += e
    print(res)

    if not haySolucion:
        print(f"NO HAY SOLUCIÓN CON LOS MOVIMIENTOS PEDIDOS")







