
n = int(input("Introduce un número positivo: "))
list = []

while n >= 0 :
    list.append(n)
    n = int(input("Introduce un número positivo: "))

#Ordena la lista
list.sort()

for e in list:
    print(e)
