import os

def crear_archivo_txt():
    contenido = """Introducción a Python

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. Python es conocido por su sintaxis clara y legible, lo que lo hace ideal para principiantes y para el desarrollo rápido de aplicaciones.

Características de Python:
- Sintaxis simple y fácil de aprender
- Gran cantidad de bibliotecas y frameworks
- Soporte para múltiples paradigmas de programación (orientado a objetos, funcional, etc.)
- Comunidad activa y en crecimiento

¡Bienvenido al mundo de Python!"""

    file_path = os.path.abspath("introduccion_python.txt")
    with open(file_path, "w") as archivo:
        archivo.write(contenido)
    
    print(f"Archivo guardado en: {file_path}")

if __name__ == "__main__":
    crear_archivo_txt()

    