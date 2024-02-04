# creamos el programa que nos indica si es primo o no

def es_primo(numero):
    # Verificar si el número es menor o igual a 1 (los números negativos no son primos)
    if numero <= 1:
        return False
    # Verificar divisibilidad por todos los números desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    # Si no se encontraron divisores, el número es primo
    return True

# ingresar un numero
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

# imprimimos el resultado
if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")
