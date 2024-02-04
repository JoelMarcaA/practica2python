from datetime import datetime
# creamos el programa 
def convertir_fecha(input_fecha):
    # Intenta parsear la fecha en dos formatos diferentes
    try:
        fecha = datetime.strptime(input_fecha, '%m/%d/%Y')
    except ValueError:
        try:
            fecha = datetime.strptime(input_fecha, '%B %d, %Y')
        except ValueError:
            print("Formato de fecha no válido. Introduce la fecha en el formato correcto.")
            return
    
    # Convierte la fecha al formato AAAA-MM-DD
    fecha_formateada = fecha.strftime('%Y-%m-%d')
    
    print(f"Input: {input_fecha} | Output: {fecha_formateada}")

# ingrese una fecha en formato mes-día-año
fecha_usuario = input("Introduce una fecha")

# imprimimos el resultado
convertir_fecha(fecha_usuario)

