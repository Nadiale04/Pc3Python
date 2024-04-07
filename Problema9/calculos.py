import operaciones
try:
    a=int(input('Ingrese un número: '))
    b=int(input('Ingrese otro número: '))
except:
    print("Error: Tipo de dato no válido.")
    
print("Suma:", operaciones.suma(a,b))
print("Resta:", operaciones.resta(a,b))
print("Producto:", operaciones.producto(a,b))
print("División:", operaciones.division(a,b))
