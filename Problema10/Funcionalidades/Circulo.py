import math
class circulo:
    def __init__(self, radio)->None:
        self.radio=radio
    
    def calculo_area(self):
         print(f'El área del circulo es {math.pi*(self.radio)**2}')
         

