# definir la función para imprimir el patrón
def imprimir_patron(filas):
    for i in range(1, filas + 1):
        # Imprimir i asteriscos en la fila actual
        print("* " * i)

    # Imprimir las filas inversas
    for i in range(filas - 1, 0, -1):
        # Imprimir i asteriscos en la fila actual
        print("* " * i)

# especificar el número de filas para el patrón
numero_filas = 5

# imprimimos el resultado
imprimir_patron(numero_filas)
