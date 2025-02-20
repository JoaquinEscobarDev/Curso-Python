def divide(a, b):
    try:
        result = a / b  # Intentar realizar la división
    except ZeroDivisionError:
        # Manejar la excepción si se intenta dividir por cero
        print("Error: No se puede dividir por cero.")
        pass  # Continuar la ejecución del programa
    except TypeError:
        # Manejar la excepción si los argumentos no son números
        print("Error: Ambos argumentos deben ser números.")
        pass  # Continuar la ejecución del programa
    else:
        # Si no hay excepciones, imprimir el resultado
        print(f"El resultado es: {result}")
    finally:
        # Este bloque se ejecuta siempre, haya o no excepciones
        print("Operación de división completada.")

# Ejemplos de uso
divide(10, 2)  # Debería imprimir el resultado
divide(10, 0)  # Debería manejar la excepción de división por cero
divide(10, 'a')  # Debería manejar la excepción de tipo

#Pass sirve para manejar excepciones sin alterar nada. se utiliza mayormente para hacer depuracion