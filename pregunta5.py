# creamos el programa
def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    print(f"Número ingresado: {numero} y Dígito: {digito}")
    print(f"Cantidad de veces {digito} en el número: {cantidad}")

# ingresar el numero y el digito a verificar
numero_ingresado = int(input("Ingrese un número entero: "))
digito_a_verificar = int(input("Ingrese el dígito a verificar: "))

# imprimir el resultado
contar_digitos(numero_ingresado, digito_a_verificar)
