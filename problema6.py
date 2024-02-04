# damos valor de los dos primeros numeros de la serie
a, b = 0, 1

# imprimir el primer número de la serie 
print(a)

# calculamos la serie de Fibonacci hasta el número 50
while b <= 50:
    print(b)
    a, b = b, a + b
