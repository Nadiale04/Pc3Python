def suma(n1,n2):
    try:
        resultado=n1+n2
        return resultado      
    except TypeError:
        print("Error: Tipo de dato no válido.")
        pass

def resta(n1,n2):
    try:
        resultado=n1-n2
        return resultado       
    except TypeError:
        print("Error: Tipo de dato no válido.")
        pass

def producto(n1,n2):
    try:
        resultado=n1*n2
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        pass

def division(n1,n2):
    try:
        if n2==0:
            raise ZeroDivisionError
        resultado=n1/n2
        return resultado
           
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    except TypeError:
        print("Error: Tipo de dato no válido.")
        pass