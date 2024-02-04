# funcion de python
def calcular_factorial(numero):
    # Verificar si el número es 0 o 1
    if numero == 0 or numero == 1:
        return 1
    else:
        # Calcular el factorial para números mayores que 1
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

# ingresar un numero
numero_colocado = int(input("Ingrese un número para calcular su factorial: "))

# imprimimos el resultado
factorial_numero = calcular_factorial(numero_colocado)
print(f"El factorial de {numero_colocado} es: {factorial_numero}")
