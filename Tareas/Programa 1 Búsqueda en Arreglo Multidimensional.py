#Arreglo Dimensional
lista = [
    [20, 21, 22],
    [23, 24, 25],
    [26, 27, 28]
]
no_fila = 0
busqueda = int(input('Ingrese un número entre 20 y 28: '))
for fila in lista:
    no_columna = 0
    for columna in fila:
        if (columna == busqueda):
            print(f'El número ingresado es {busqueda}, y pertenece a la posición [{no_fila}][{no_columna}]')
            no_columna += 1
    no_fila += 1




