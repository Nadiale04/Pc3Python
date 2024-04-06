class rectangulo:
    def __init__(self,largo,ancho)->None:
        self.largo=largo
        self.ancho=ancho
        pass
    def calculo_area(self):
        print(f'El área del rectangulo es de {self.largo*self.ancho}')
        pass
    pass

largo=float(input('Ingrese el largo: '))
ancho=float(input('Ingrese el ancho: '))

Rectangulo=rectangulo(largo,ancho)

Rectangulo.calculo_area()