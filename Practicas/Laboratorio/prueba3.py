friends = {'Pau':20, 'Lalo':21, 'Xavier':2}

name = str(input("Introduce el nombre de tu amigo: "))

if name in friends:
    print("La edad de {} es {}".format(name, friends[name]))
else:
    print("No se su edad")