#EJERCICIO5

import math


def sec_cuadrado(l):
    for i in l:
        yield i*i


def first ( n : int, it ):
    j = 0
    for i in it:
        if j < n:
            yield i
            j +=1


def filter(cond, it):
    for i in it:
        if cond(i):
            yield i


def take_while(cond, it):
    for i in it:
        if not cond(i):
           yield i


def squares():
    i = 0
    while True:
        if math.sqrt(i):
            yield i * i
        i += 1



if __name__ == '__main__':

    i = 0