import csv

# Función para leer un archivo CSV y devolver los datos como una lista de diccionarios
def leer_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)  # Crear un objeto DictReader para leer el archivo CSV como diccionarios
        datos = [fila for fila in lector]
    return datos

# Función para escribir datos en un archivo CSV desde una lista de diccionarios
def escribir_csv(nombre_archivo, datos, encabezados):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()  # Escribir la fila de encabezados
        escritor.writerows(datos)  # Escribir las filas de datos

# Función para agregar una nueva fila a un archivo CSV existente
def agregar_fila_csv(nombre_archivo, nueva_fila, encabezados):
    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writerow(nueva_fila)  # Escribir la nueva fila

# Función para actualizar una fila en un archivo CSV basado en una condición
def actualizar_fila_csv(nombre_archivo, condicion, nueva_fila):
    datos = leer_csv(nombre_archivo)  # Leer los datos existentes
    for fila in datos:
        if condicion(fila):  # Si la fila cumple la condición
            fila.update(nueva_fila)  # Actualizar la fila con los nuevos datos
    encabezados = datos[0].keys() if datos else nueva_fila.keys()  # Obtener los encabezados
    escribir_csv(nombre_archivo, datos, encabezados)  # Escribir los datos actualizados

# Función para eliminar una fila de un archivo CSV basado en una condición
def eliminar_fila_csv(nombre_archivo, condicion):
    datos = leer_csv(nombre_archivo)  # Leer los datos existentes
    datos = [fila for fila in datos if not condicion(fila)]  # Filtrar las filas que no cumplen la condición
    encabezados = datos[0].keys() if datos else []  # Obtener los encabezados
    escribir_csv(nombre_archivo, datos, encabezados)  # Escribir los datos actualizados

# Ejemplo de uso
if __name__ == "__main__":
    nombre_archivo = 'datos.csv'
    encabezados = ['nombre', 'edad', 'ciudad']
    datos = [
        {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'},
        {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Barcelona'}
    ]

    # Escribir datos iniciales en el archivo CSV
    escribir_csv(nombre_archivo, datos, encabezados)

    # Leer y mostrar los datos del archivo CSV
    datos_leidos = leer_csv(nombre_archivo)
    print(datos_leidos)

    # Agregar una nueva fila al archivo CSV
    nueva_fila = {'nombre': 'Luis', 'edad': 28, 'ciudad': 'Valencia'}
    agregar_fila_csv(nombre_archivo, nueva_fila, encabezados)

    # Actualizar una fila en el archivo CSV
    actualizar_fila_csv(nombre_archivo, lambda fila: fila['nombre'] == 'Ana', {'edad': 26})

    # Eliminar una fila del archivo CSV
    eliminar_fila_csv(nombre_archivo, lambda fila: fila['nombre'] == 'Juan')