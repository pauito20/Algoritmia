from math import sqrt
#Ecuación de Segundo Grado



print("Bienvenido al solucionador de ecuaciones de segundo grado ax^2 + bx + c = 0")

a = float(input("Introduce un valor para a: "))
b = float(input("Introduce un valor para b: "))
c = float(input("Introduce un valor para c: "))



def seconGrade(a,b,c):

    if ((b ** 2) - 4 * a * c) < 0:
        print("La solución de la ecuación es con numeros complejos")
    else:
        x1 = (-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)  # Fórmula de Bhaskara parte positiva
        x2 = (-b - sqrt(b ** 2 - (4 * a * c))) / (2 * a)  # Fórmula de Bhaskara parte negativa
        print("Las soluciones de la ecuación son:")
        print(x1)
        print(x2)


seconGrade(a,b,c)



