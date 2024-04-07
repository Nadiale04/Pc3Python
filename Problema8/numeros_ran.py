import random

def numerosaleatorios():
    numeros=[random.randrange(0,101) for x in range (20)]
    return numeros
    
def mostrar(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero)

def ordenar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for numero in lista_ordenada:
        print(numero)
