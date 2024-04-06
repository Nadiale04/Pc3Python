class Alumno:
    def __init__(self, nombre, numeroregisto):
        self.nombre = nombre
        self.numeroregisto = numeroregisto
        self.edad=None
        self.notas=[]

    def display(self):
        print(f'Nombre: {self.nombre}, número de registro: {self.numeroregisto}')
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

nombre = input('Ingrese nombre del alumno: ').capitalize()
numeroregistro = input('Ingrese número de registro: ')
alumno = Alumno(nombre, numeroregistro)

alumno.display()
alumno.set_age()
alumno.set_nota()
alumno.display()