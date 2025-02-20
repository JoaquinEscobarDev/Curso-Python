# def greet(name, last_name=" "):
#     print("Hola", name, last_name)


# greet("Carli", "Florida")
# greet("Diego")
# greet(last_name="Escobar", name="Joaquín")

# Calculadora


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def calculator():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '5':
            print("Saliendo de la calculadora...")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Por favor ingrese solo números.")
                continue
            
            if choice == '1':
                print(f"Resultado: {add(a, b)}")
            elif choice == '2':
                print(f"Resultado: {substract(a, b)}")
            elif choice == '3':
                print(f"Resultado: {multiply(a, b)}")
            elif choice == '4':
                if b != 0:
                    print(f"Resultado: {divide(a, b)}")
                else:
                    print("Error: División por cero")
        else:
            print("Opción no válida, por favor intente de nuevo.")


calculator()
