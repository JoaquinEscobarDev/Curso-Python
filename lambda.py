# Función lambda para sumar dos números
add = lambda x, y: x + y

# Una función lambda es una función anónima que se define en una sola línea usando la palabra clave 'lambda'.
# Las funciones lambda pueden tener cualquier número de argumentos, pero solo una expresión.
# La expresión se evalúa y se devuelve cuando se llama a la función.

# Ejemplo de uso
result = add(3, 5)
print(result)  # Salida: 8 

# Función lambda para generar tablas de multiplicación ordenadas
multiplication_table = lambda n: [n * i for i in range(1, 11)]

def print_multiplication_tables():
    for i in range(1, 11):
        print(f"Tabla de multiplicar del {i}: {multiplication_table(i)}")

# Ejemplo de uso de las tablas de multiplicación
print_multiplication_tables()

# Calculadora usando funciones lambda
operations = {
    '1': lambda a, b: a + b,
    '2': lambda a, b: a - b,
    '3': lambda a, b: a * b,
    '4': lambda a, b: a / b if b != 0 else "Error: División por cero"
}

def calculator_lambda():
    while True:
        print("\n--- Calculadora Lambda ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '5':
            print("Saliendo de la calculadora...")
            break
        
        if choice in operations:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Por favor ingrese solo números.")
                continue
            
            result = operations[choice](a, b)
            print(f"Resultado: {result}")
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejemplo de uso del menú de la calculadora lambda
calculator_lambda()

