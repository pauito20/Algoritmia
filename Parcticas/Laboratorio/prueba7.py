class Estudiante:
    def __init__(self, name: str ):
        self.name = name
        self.asignaturas = {}

    def califica(self, asig:str, nota:int):
        self.asignaturas[asig] = nota

    def nota(self, asig:str):
        if (asig in self.asignaturas):
            return  self.asignaturas.get(asig)
        else:
            return None

    def media(self):
        if len(self.asignaturas) != 0:
            n = 0
            for nota in self.asignaturas.values():
                n += nota
            return n / len(self.asignaturas)
        else:
            return None

    def muestra_expediente(self):
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Notas del alumno {} ".format(self.name))
        print()
        for asig, nota in self.asignaturas.items():
            print(f"{asig}: {nota}")
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

estudiante =  Estudiante("Lalo")
estudiante.califica("EI1022", 10)
estudiante.califica("EI1023",8)
estudiante.califica("EI1021",7.5)

print("La nota de {} en EI1022 es: {} ".format(estudiante.name, estudiante.nota("EI1022")))
print("La nota media del alumno {} es {} ".format(estudiante.name, estudiante.media()))
estudiante.muestra_expediente()