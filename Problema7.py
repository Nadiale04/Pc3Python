import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def constructor(self):
        x = input('Ingrese coordenada x: ')
        y = input('Ingrese coordenada y: ')
        if x and y:
            x = int(x)
            y = int(y)
        else:
            x = 0
            y = 0
        return Punto(x,y)

    def __str__(self):
        return 'A({}, {})'.format(self.x, self.y)
    
    def cuadrante(self):
        if self.x ==0 and self.y!= 0:
            print('Se sitúa en el eje y')
        elif self.y==0 and self.x!= 0:
            print('Se sitúa en el eje x')
        elif self.y==0 and self.x== 0:
            print('Está sobre el origen')
        elif self.x > 0 and self.y > 0:
            print('Se sitúa en el primer cuadrante')
        elif self.x < 0 and self.y > 0:
            print('Se sitúa en el segundo cuadrante')
        elif self.x < 0 and self.y < 0:
            print('Se sitúa en el tercer cuadrante')
        elif self.x > 0 and self.y < 0:
            print('Se sitúa en el cuarto cuadrante')
    

    def vector(self):
        x1 = int(input('Ingrese un nuevo x2: '))
        y1 = int(input('Ingrese un nuevo y2: '))
        print(f'AB({x1 - self.x}, {y1 - self.y})')
    
    def distancia(self, x1, y1):
        d = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        print(f'La distancia es:{d}')


punto = Punto(0, 0)
punto = punto.constructor()
print(punto)
punto.cuadrante()
punto.vector()
x2 = int(input('Ingrese un nuevo x3: '))
y2 = int(input('Ingrese un nuevo y3: '))
punto.distancia(x2, y2)