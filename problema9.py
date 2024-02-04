# programa
def omitir_vocales(cadena):
    # Inicializar una cadena vacía para almacenar el resultado
    resultado = ""

    # Iterar sobre cada caracter en la cadena
    for caracter in cadena:
        # Verificar si el caracter es una vocal (mayúscula o minúscula)
        if caracter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += caracter
    return resultado

# ingresar una palabra o texto
cadena_ingresada = input("Ingrese una cadena de texto: ")

# imprimimos el resultado
resultado_sin_vocales = omitir_vocales(cadena_ingresada)
print("Texto con vocales omitidas:", resultado_sin_vocales)
