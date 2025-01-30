class Person:
    def __init__(self, name, age):
        # Inicializar los atributos de la clase
        self.name = name
        self.age = age
    
    def greet(self):
        # Método para imprimir un saludo con el nombre y la edad
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")
    
# Crear instancias de la clase Person
person1 = Person("Joaquín", 23)
person2 = Person("Camila", 21)

# Llamar al método greet para cada instancia
person1.greet()
person2.greet()
