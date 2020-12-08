import sys

























if __name__ == '__main__':
    # Convertimos el fichero en una lista de líneas
    lineas_fich = sys.stdin.readlines()
    numEdificios = int(lineas_fich[0])

    alturas = []
    for i in range(1, len(lineas_fich)):
        alturas.append(int(lineas_fich[i]))


    print("Nº de edificios: ", numEdificios)
    print("Alturas de los edificios: ", alturas)


