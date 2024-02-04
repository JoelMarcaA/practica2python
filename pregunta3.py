# creamos una lista para agregar los numeros
numeros = []

while True:
    try:
        # Solicitar al usuario que ingrese un número
        numero = int(input("Ingresa un número (o ingresa cualquier letra para detener): "))
        # Agregar el número a la lista
        numeros.append(numero)
    except ValueError:
        # Si el usuario ingresa una letra, detener el bucle
        break

# muestra los numeros ingresados
print("Números ingresados:", numeros)

# contar la cantidad de números pares e impares
numeros_pares = sum(1 for num in numeros if num % 2 == 0)
numeros_impares = sum(1 for num in numeros if num % 2 != 0)

# imprimir los resultados
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)

