#Primera practica

#Ej1 Diseña un programa que pida dos números por teclado, a y b, y muestre por pantalla su suma como en el siguiente ejemplo:
#Introduce a: 2
#Introduce b: 5
#La suma de 2 y 5 es 7

a=2
b=5
print(f"La suma de {a} y {b} es {a+b}")

#Diseña un programa que lea enteros de teclado hasta que el usuario teclee uno negativo.
# Los enteros positivos se irán añadiendo a una lista.
# Muestra el contenido de la lista ordenado de menor a mayor valor, con un elemento por línea de pantalla.


lista=[]
n=int(input("Introduce numeros positivos: "))

while n >=0:
    lista.append(n)
    n = int(input("Introduce numeros positivos: "))

lista.sort()
for elem in lista:
    print(elem)

#Escribe un programa que: Cree un diccionario con el nombre de tres amigos y asocie a cada uno su edad.
# Pida el nombre de un amigo y escriba su edad. Si el nombre no está en el diccionario queescriba: ‘No sé su edad’.

diccionario = {'Pau': 20,'Marta':21,"Pepe":56}

n=str(input("Introduce el nombre de un amigo: "))

if n in diccionario.keys():
    print(f'La edad de {n} es {diccionario[n]}')
else:
    print('No se su edad.')


#Diseña una función que, dados tres números, a, b y c, devuelva las dos raíces de la ecuación de segundo grado:
#a x2 + b x + c = 0
#Usa la función en un programa que pida los tres números y muestre por pantalla la(s) solución(es) de la ecuación.
#¡Ojo! Si sólo hay una solución, no muestres dos valores.

a = int(input("Introduce un numero: "))
b = int(input("Introduce un numero: "))
c = int(input("Introduce un numero: "))

from math import sqrt

def ecuacion(a,b,c):
    if ((b**2)-4*a*c)<0:
        print("La solución de la ecuación es con numeros complejos")
    else:
        res1 = (-b + sqrt(((b**2)-4*a*c)))/(2*a)
        res2 = (-b - sqrt(((b**2)-4*a*c)))/(2*a)

        if res1 == res2:
            return res1
        else :
            return res1,res2

print(ecuacion(a,b,c))




#Ejercicio 7 Define una clase Estudiante en el que almacenamos su
# nombre y un diccionario cuyas claves son asignaturas a las que asociamos calificaciones.
from typing import TypeVar

class Estudiante:
    T = TypeVar('T', int, float)

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.notas = {}

    def califica(self, cod:str, nota: T):
        self.notas[cod] = nota

    def nota(self,cod:str):
        return self.notas[cod]

    def media(self):
        if len(self.notas)!=0:

            #suma =0
            #for nota in self.notas.values():
             #   suma += nota
            #return suma/len(self.notas)

            # Hacen los mismo pero con menos codigo

            suma = sum(self.notas.values())
            return suma/len(self.notas)

        else:
            return None

    def expediente(self):
        print(self.nombre)
        print()
        for asig,nota in self.notas.items():
            print(f"{asig}: {nota}")



#Ejercicio 8 Utilizando una expresión generatriz, inicializa un diccionario que asocie a cada número entre
# 1 y 100 el valor True si el número es divisible por 3 y False en caso contrario.


d = dict(( i,i%3==0) for i in range(1,100))
print(d)

