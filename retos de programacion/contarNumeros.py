"""
RETO 123456789
Simula el reto viral 123456789.
Crea una funcion que cuente de 1 a 9, eliminando cada vez un digito 
y mostrando un espacio en blanco en su lugar, de manera ascendente y descendente
"""

for i in range(1, 9):
    for j in range(i, 9):
        print(j, end="")
    print()

for i in range(8, 0, -1):
    for j in range(i, 9):
        print(j, end="")
    print()

      