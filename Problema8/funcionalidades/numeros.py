import random

def numerosaleatorios():
    numeros=[]
    for x in range (20):
        numeros.append(random.randrange(0,101))
        return numeros
    
def mostrar_lista(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for numero in lista_ordenada:
        print(numero)

def mostrar_lista(lista):
    print('Lista de número')
    for numero in lista:
        print(numero)