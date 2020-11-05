import math

def sec_cuadrado(l):
    for i in l:
        yield i * i


def first(n, it):
    max = 0
    for i in it:
        if max <= n:
            yield i
            max += 1


def filter(cond, it):
    for i in it:
        if cond(i):
            yield i


def take_while(cond, it):
    for i in it:
        if not cond(i):
            yield i


def squares():
    p = 1
    while True:
        if math.sqrt(p):
            yield p * p
        p += 1


if __name__ == '__main__':

    lista = [1, 2, 3, 4, 5]
    print("Probamos sec_cuadrado")
    for sq in sec_cuadrado(lista):
        print(sq)

    print("Probamos first con range")
    for elem in first(20, range(50, 200)):
        print(elem)

    print("Probamos first con lista")
    for elem in first(100, [2, 4, 5, 7, 2]):
        print(elem)

    print("Probamos filter con range")
    for fil in filter(lambda n: n < 100, range(50, 200)):
        print(fil)

    print("Probamos filter con lista")
    for fil in filter(lambda n: n % 2 == 0, [2, 4, 5, 7, 2]):
        print(fil)

    print("Probamos take_while con range")
    for fil in take_while(lambda n: n < 100, range(50, 200)):
        print(fil)

    print("Probamos take_while con lista")
    for fil in take_while(lambda n: n % 2 == 0, [2, 4, 5, 7, 2]):
        print(fil)

    print("Probamos squares")
    for per_sq in squares():
        print(per_sq)

