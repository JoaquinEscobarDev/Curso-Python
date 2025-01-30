def factorial(n):
    # La función factorial calcula el producto de todos los números enteros positivos
    # desde 1 hasta n. Si n es 0, el factorial es 1 por definición.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
print(factorial(5))  # Output: 120


def fibonacci(n):
    # La función fibonacci calcula el n-ésimo número en la secuencia de Fibonacci.
    # La secuencia de Fibonacci es una serie de números donde cada número es la suma
    # de los dos números anteriores. Los dos primeros números son 0 y 1.
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso
print(fibonacci(6))  # Output: 8

def suma_naturales(n):
    # La función suma_naturales calcula la suma de los primeros n números naturales.
    # Si n es 0, la suma es 0 por definición.
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n - 1)

# Ejemplo de uso
print(suma_naturales(10))  # Output: 55