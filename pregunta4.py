# función para ingresar datos de los alumnos
def ingresar_datos_alumnos():
    lista_alumnos = []  # Lista para almacenar los datos de los alumnos

    n = int(input("Ingrese la cantidad de alumnos: "))

    for i in range(n):
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        notas = []

        # Ingresar las 3 calificaciones
        for j in range(3):
            calificacion = float(input(f"Ingrese la calificación {j+1} para {nombre_alumno}: "))
            notas.append(calificacion)

        # Crear un diccionario con los datos del alumno
        alumno = {"Alumno": nombre_alumno, "Notas": notas}

        # Agregar el diccionario a la lista de alumnos
        lista_alumnos.append(alumno)

    return lista_alumnos

# funcion para mostrar la lista
def mostrar_listado_alumnos(lista_alumnos):
    for alumno in lista_alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Programa que nos pide los datos del alumno
if __name__ == "__main__":
    # Ingresar datos de los alumnos
    lista_alumnos = ingresar_datos_alumnos()

    # imprimimos el resultado
    mostrar_listado_alumnos(lista_alumnos)