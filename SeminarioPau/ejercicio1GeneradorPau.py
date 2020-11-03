
def sec_cuadrado(l):
    for i in l:
        yield i*i


if __name__ == '__main__':

    lista = [1,2,3,4,5]
    for sq in sec_cuadrado(lista):
        print(sq)
