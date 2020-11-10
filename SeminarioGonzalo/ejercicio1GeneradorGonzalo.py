
import math

#Ejercicio1

def sec_cuadrado(l):
    for i in l:
        yield i*i


#Ejercicio2

def first ( n : int, it ):
    j = 0
    for i in it:
        if j < n:
            yield i
            j +=1

#Ejercicio3

def filter(cond, it):
    for i in it:
        if cond(i):
            yield i

#Ejercicio4

def take_while(cond, it):
    for i in it:
        if not cond(i):
           yield i

#Ejercicio5

def squares():
    i=0
    while i < j:
        if math.sqrt(i):
            yield i * i
        i += 1



if __name__ == '__main__':


    print("Ejercio 1: ")
    for sq in sec_cuadrado([1, 2, 10, 4, 5]):
        print(sq)

    print("\n Ejercicio 2: ")
    for i in first(20, range(50,200)):
        print(i)
    print("------------")
    for i in first(100, [2,4,5,7,2]):
        print(i)

    print("\n Ejercicio 3: ")
    for i in filter(lambda n: n < 100, range(50,200)):
        print(i)
    print("------------")
    for i in filter(lambda n : n%2 == 0, [2,4,5,7,2]):
        print(i)


    for i in take_while(lambda n: n < 100, range(50, 200)):
        print(i)
    print("------------")
    for i in take_while(lambda n: n % 2 == 0, [2, 4, 5, 7, 2]):
        print(i)
    print("\n Ejercicio 4: ")
    for i in squares():
        print(i)