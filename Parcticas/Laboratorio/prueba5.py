def myfunction(a, b):
    a=2*a
    b[0] = 10 #*
    b.append(0)#*
    b = list(range(3))
    return b*a #multiplicar listas = concatenar listas una detras de otra
x=1
y = list(range(6)) #Numeros del 0 al 5 "Vector de lenght 6"
print(x, y)
print(myfunction(x, y))
print(x, y)

#Al modificar el objeto que apunta la variable * no es lo mismo
# que al apuntar a la variable