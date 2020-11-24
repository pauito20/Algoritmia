import os
import sys
from typing import List, Tuple

import srt as srt

Pos = Tuple[int, int]

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



    level_map, player_pos, boxes_start, boxes_end = read_level(puzle)

    print(f"El numero maximo de movimientos es: {numMaxMovimientos}")
    print(read_level(puzle))