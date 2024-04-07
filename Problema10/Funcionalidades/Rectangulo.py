class rectangulo:
    def __init__(self,largo,ancho)->None:
        self.largo=largo
        self.ancho=ancho
        
    def calculo_area(self):
        print(f'El área del rectangulo es de {self.largo*self.ancho}')
       