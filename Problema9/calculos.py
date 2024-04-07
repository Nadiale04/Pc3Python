import operaciones

try:
    n1=float(input('Ingrese el valor de n1: '))
    n2=float(input('Ingrese el valor de n2: '))

    print('El resultado de la suma es:', operaciones.suma(n1,n2))
    print('El resultado de la resta es:', operaciones.resta(n1,n2))
    print('El resultado del producto es:', operaciones.producto(n1,n2))
    print('El resultado de la división:', operaciones.division(n1,n2))

except ValueError:
    print('Error: Los valores deben ser números.')