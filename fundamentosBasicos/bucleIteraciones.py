# numbers = [1, 2, 3, 4, 5, 6]

# for i in numbers:
#     print("Aqui i es: ", i + 1)

# for i in range(3, 10):
#     print(i)

# fruits = ["manzana", "pera", "uva", "naranja", "tomate"]
# for fruta in fruits:
#     print(fruta)
#     if fruta == "naranja":
#         print("es una naranja")

# x = 0
# while x < 5:
#     if x == 3:
#         break
#     print(x)
#     x += 1

# for i in numbers:
#     if i == 3:
#         break
#     print("Aquí i es igual a 3")

# Iteración

# my_list = [1,2,3,4]

# my_iter = iter(my_list)

# print(next(my_iter))

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# # Usando un bucle for para iterar a través de un iterador
# my_iter = iter(my_list)
# for item in my_iter:
#     print(item)

# # Usando un bucle while para iterar a través de un iterador
# my_iter = iter(my_list)
# while True:
#     try:
#         item = next(my_iter)
#         print(item)
#     except StopIteration:
#         break

#         # Usando range para crear un iterador
#         range_iter = iter(range(5, 15))

#         # Usando un bucle for para iterar a través del iterador de rango
#         for item in range_iter:
#             print(item)

#         # Usando un bucle while para iterar a través del iterador de rango
#         range_iter = iter(range(5, 15))
#         while True:
#             try:
#                 item = next(range_iter)
#                 print(item)
#             except StopIteration:
#                 break

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Ejemplo de uso de la función de Fibonacci
for num in fibonacci(10):
    print(num)


