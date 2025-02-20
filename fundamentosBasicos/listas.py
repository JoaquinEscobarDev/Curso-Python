# listas.py

# Crear una lista de ejemplo
mi_lista = [1, 2, 3, 4, 5]

# Imprimir la lista
print(mi_lista)

# Método slice para obtener una sublista
sub_lista = mi_lista[1:4]

# Imprimir la sublista
print(sub_lista)

# Crear una tupla de ejemplo
mi_tupla = (10, 20, 30, 40, 50)

# Imprimir la tupla
print(type(mi_tupla))
print(mi_tupla)

# Obtener la longitud de la lista y la tupla
longitud_lista = len(mi_lista)
longitud_tupla = len(mi_tupla)

# Imprimir las longitudes
print(f"Longitud de la lista: {longitud_lista}")
print(f"Longitud de la tupla: {longitud_tupla}")

# Crear una matriz de ejemplo (lista de listas)
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimir la matriz
print("Matriz:")
for fila in mi_matriz:
    print(fila)

# Obtener la longitud de la matriz
longitud_matriz = len(mi_matriz)

# Imprimir la longitud de la matriz
print(f"Longitud de la matriz: {longitud_matriz}")