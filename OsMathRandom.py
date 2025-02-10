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
