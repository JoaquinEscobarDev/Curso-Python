import os

def crear_archivo_txt():
    # Contenido del archivo de texto
    contenido = """Introducción a Python

    Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. Python es conocido por su sintaxis clara y legible, lo que lo hace ideal para principiantes y para el desarrollo rápido de aplicaciones.

    Características de Python:
    - Sintaxis simple y fácil de aprender
    - Gran cantidad de bibliotecas y frameworks
    - Soporte para múltiples paradigmas de programación (orientado a objetos, funcional, etc.)
    - Comunidad activa y en crecimiento

    ¡Bienvenido al mundo de Python!"""

    # Obtener la ruta absoluta del archivo
    file_path = os.path.abspath("introduccion_python.txt")
    # Crear y escribir el contenido en el archivo
    with open(file_path, "w") as archivo:
        archivo.write(contenido)
    
    # Imprimir la ruta donde se guardó el archivo
    print(f"Archivo guardado en: {file_path}")

def leer_archivo_txt():
    # Obtener la ruta absoluta del archivo
    file_path = os.path.abspath("introduccion_python.txt")
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        # Leer y mostrar el contenido del archivo
        with open(file_path, "r") as archivo:
            contenido = archivo.read()
        print(contenido)
    else:
        print("El archivo no existe.")

def agregar_contenido_txt(nuevo_contenido):
    # Obtener la ruta absoluta del archivo
    file_path = os.path.abspath("introduccion_python.txt")
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        # Agregar nuevo contenido al archivo
        with open(file_path, "a") as archivo:
            archivo.write("\n" + nuevo_contenido)
        print("Contenido agregado.")
    else:
        print("El archivo no existe.")

def eliminar_archivo_txt():
    # Obtener la ruta absoluta del archivo
    file_path = os.path.abspath("introduccion_python.txt")
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        # Eliminar el archivo
        os.remove(file_path)
        print("Archivo eliminado.")
    else:
        print("El archivo no existe.")

if __name__ == "__main__":
    # Crear el archivo de texto
    crear_archivo_txt()
    # Leer el contenido del archivo
    leer_archivo_txt()
    # Agregar nuevo contenido al archivo
    agregar_contenido_txt("Este es un nuevo contenido agregado al archivo.")
    # Leer el contenido actualizado del archivo
    leer_archivo_txt()
    # Eliminar el archivo
    eliminar_archivo_txt()

