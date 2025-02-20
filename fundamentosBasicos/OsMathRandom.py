# import os 


# cwd = os.getcwd() # current working directory [saber en que directorio estoy]
# print("Directorio actual", cwd)

# #listar archivos .txt
# txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
# print("Archivos txt", txt_files)

# os.rename('introduccion_python.txt', 'python.txt')
# print("Archivo renombrado")

# # Crear un nuevo directorio
# os.mkdir('nuevo_directorio')
# print("Directorio 'nuevo_directorio' creado")

# # Cambiar el directorio actual
# os.chdir('nuevo_directorio')
# print("Directorio cambiado a 'nuevo_directorio'")

# # Crear un nuevo archivo en el nuevo directorio
# with open('archivo_nuevo.txt', 'w') as file:
#     file.write('Contenido de prueba')
# print("Archivo 'archivo_nuevo.txt' creado en 'nuevo_directorio'")

# # Volver al directorio anterior
# os.chdir('..')
# print("Directorio cambiado al anterior")

# # Eliminar el archivo creado
# os.remove('nuevo_directorio/archivo_nuevo.txt')
# print("Archivo 'archivo_nuevo.txt' eliminado")

# # Eliminar el directorio creado
# os.rmdir('nuevo_directorio')
# print("Directorio 'nuevo_directorio' eliminado")

#-------------------------------------------------------------------------------------------------

# import math

# # Calcular la raíz cuadrada
# print("Raíz cuadrada de 16:", math.sqrt(16))

# # Calcular el seno de un ángulo (en radianes)
# print("Seno de pi/2:", math.sin(math.pi / 2))

# # Calcular el coseno de un ángulo (en radianes)
# print("Coseno de pi:", math.cos(math.pi))

# # Calcular el logaritmo natural
# print("Logaritmo natural de 10:", math.log(10))

# # Calcular el logaritmo en base 10
# print("Logaritmo base 10 de 100:", math.log10(100))

# # Calcular el valor absoluto
# print("Valor absoluto de -20:", math.fabs(-20))

# # Calcular el factorial de un número
# print("Factorial de 5:", math.factorial(5))

# # Calcular la potencia
# print("2 elevado a 3:", math.pow(2, 3))

# # Redondear hacia arriba
# print("Redondear 4.3 hacia arriba:", math.ceil(4.3))

# # Redondear hacia abajo
# print("Redondear 4.7 hacia abajo:", math.floor(4.7))

#-------------------------------------------------------------------------------------------------

import random

# Generar un número aleatorio entre 0 y 1
print("Número aleatorio entre 0 y 1:", random.random())

# Generar un número entero aleatorio entre dos valores
print("Número entero aleatorio entre 1 y 10:", random.randint(1, 10))

# Seleccionar un elemento aleatorio de una lista
lista = ['a', 'b', 'c', 'd', 'e']
print("Elemento aleatorio de la lista:", random.choice(lista))

# Barajar una lista
random.shuffle(lista)
print("Lista barajada:", lista)

# Generar un número aleatorio flotante entre dos valores
print("Número flotante aleatorio entre 1.5 y 5.5:", random.uniform(1.5, 5.5))

# Seleccionar una muestra aleatoria de una lista
print("Muestra aleatoria de 3 elementos de la lista:", random.sample(lista, 3))