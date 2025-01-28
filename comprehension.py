from pprint import pprint

# Comprensión de listas para crear una lista de cuadrados
squares = [x**2 for x in range(10)]
pprint(squares)

# Comprensión de listas con una condición para crear una lista de números pares
evens = [x for x in range(20) if x % 2 == 0]
pprint(evens)

# Comprensión de listas para crear una lista de tuplas (número, cuadrado)
number_square_tuples = [(x, x**2) for x in range(10)]
pprint(number_square_tuples)

# Comprensión de listas para aplanar una lista de listas
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
pprint(flattened_list)

# Comprensión de listas para convertir una lista de temperaturas de Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
pprint(fahrenheit)

# Comprensión de listas para convertir una lista de temperaturas de Fahrenheit a Celsius
fahrenheit = [32, 50, 68, 86, 104]
celsius = [(temp - 32) * 5/9 for temp in fahrenheit]
pprint(celsius)