class Alumno:
    def __init__(self, nombre, numeroregisto):
        self.nombre = nombre
        self.numeroregisto = numeroregisto
        self.edad=None
        self.notas=[]

    def display(self):
        print(f'Nombre: {self.nombre}, N°registro: {self.numeroregisto}')
        if self.edad is not None:
            print(f'Edad: {self.edad}')
        if self.notas:
            print(f'Notas: {self.notas}')

    def set_age(self):
        edad = input('Ingrese la edad: ')
        self.edad=edad

    def set_nota(self):
        notas = input('Ingrese notas: ')
        self.notas=notas

alum1=Alumno('Rosa', 3242)
alum1.display()
alum1.set_age()
alum1.set_nota()
alum1.display()

alum2=Alumno('Juan', 4920)
alum1.display()
alum1.set_age()
alum1.set_nota()
alum1.display()
