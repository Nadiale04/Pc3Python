while True:
    try:
        notasingresadas=input('Ingrese las notas:')
        notasindividuales=notasingresadas.split(',')
        notas= [int(float(nota)) for nota in notasindividuales]
        print(f'Calificaciones:{notas}')
        break
    except:
        print('Nota no válida')