while True:
    try:
        fraccioningresada=input('Ingrese la fracción de combustible (X/Y): ')
        numerador,denominador=fraccioningresada.split('/')
        x=int(numerador)
        y=int(denominador)
        fraccion=int((x/y)*100)
        if x>y:
            raise ValueError
    except ValueError:
        print('¡Eror! Solo se permiten números enteros y X debe ser menos o igual a Y')
    except ZeroDivisionError:
        print('¡Error! Ingrese otro número por favor')
    else:
        if fraccion<1:
            print('E')
        elif fraccion>99:
            print('F')
        elif fraccion>1 and fraccion<99:
            print(f'{fraccion} %')
        break