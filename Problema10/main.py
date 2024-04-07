from Funcionalidades.Circulo import circulo
from Funcionalidades.Cuadrado import cuadrado
from Funcionalidades.Rectangulo import rectangulo

mensaje_bienvenida='Bienvenido al menú interactivo'
opciones_menu="""¿Qué quieres hacer? Escribe una opción
        1) Calcular el área de un circulo
        2) Calcular el área de un rectangulo
        3) Calcular el área de un cuadrado
        4) Salir"""


def opcion1():
    radio=float(input('Ingrese el radio del círculo: '))
    c=circulo(radio)
    c.calculo_area()

def opcion2():
    largo=float(input('Ingrese el largo del rectángulo: '))
    ancho=float(input('Ingrese el ancho del rectángulo: '))
    r=rectangulo(largo,ancho)
    r.calculo_area()

def opcion3():
    lado=float(input('Ingrese el lado del cuadrado: '))
    cd=cuadrado(lado)
    cd.calculo_area()

def main():
    print(mensaje_bienvenida)
    while True:
        opcion = input(opciones_menu) # me devuelve un string ''
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion =='3':
            opcion3()
        elif opcion =='4':       
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break #con esto se sale por la opcion de termino
        else:
            print("Comando desconocido, vuelve a intentarlo")


if __name__=='__main__':
    main()