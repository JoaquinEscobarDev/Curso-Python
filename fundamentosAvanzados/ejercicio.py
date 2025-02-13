# Implementa una funcion que procese una lista de diccionarios con informacion de empleados, utilizando anotaciones de tipo.
#1 recibira una lista de diccionarios, cada diccionario tendra las claves: "nombre", "edad", "sueldo".
#2 devolvera una lista de empleados que ganen mas de cierto sueldo.

#importamos las librerias necesarias
from typing import List, Dict

#creamos la funcion filtrar_empleados_por_sueldo que recibe una lista de diccionarios y un sueldo minimo
def filtrar_empleados_por_sueldo(empleados: List[Dict[str, int]], sueldo_minimo: float) -> List[Dict[str, int]]:
    return [empleado for empleado in empleados if float(empleado['sueldo']) > sueldo_minimo]
    
#lista de diccionarios con informacion de empleados
empleados = [
                    {'nombre': 'Ana', 'edad': 28, 'sueldo': 1500},
                    {'nombre': 'Luis', 'edad': 35, 'sueldo': 2500},
                    {'nombre': 'Carlos', 'edad': 40, 'sueldo': 3500},
                    {'nombre': 'Maria', 'edad': 22, 'sueldo': 4500},
                    {'nombre': 'Jorge', 'edad': 29, 'sueldo': 5500},
                    {'nombre': 'Laura', 'edad': 31, 'sueldo': 6500},
                    {'nombre': 'Pedro', 'edad': 38, 'sueldo': 7500},
                    {'nombre': 'Sofia', 'edad': 26, 'sueldo': 8500},
                    {'nombre': 'Miguel', 'edad': 33, 'sueldo': 9500},
                    {'nombre': 'Lucia', 'edad': 27, 'sueldo': 10500}
                ]


#imprimimos la lista de empleados que ganan mas de 500
print(filtrar_empleados_por_sueldo(empleados, 7000)) 