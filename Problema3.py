import math
class circulo:
    def __init__(self, radio)->None:
        self.radio=radio
        pass
    def calculo_area(self):
         print(f'El área del circulo es {math.pi*(self.radio)**2}')
         pass
    pass

radioingresado=circulo(float(input('Ingrese el radio del circulo: ')))
radioingresado.calculo_area()