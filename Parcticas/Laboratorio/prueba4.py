def myfunction(a, b):
    a += 1
    b.append(0)
x = 1
y = [2, 1]
myfunction(x, y)

print(x, y)

#El resultado es x = 1 e y = [2, 1, 0]
#La lista al cambiarla en la función se cambia, es MUTABLE
#El entero no cambia al ser cambiado en la función, es INMUTABLE
