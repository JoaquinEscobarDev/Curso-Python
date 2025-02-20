# Base class to demonstrate the 4 fundamental pillars of Object-Oriented Programming (OOP)

# 1. Abstracción
# La abstracción permite representar conceptos complejos en términos más simples.
# En este ejemplo, abstraemos la idea de un "Animal" con atributos y métodos básicos.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

# 2. Herencia
# La herencia permite crear nuevas clases basadas en clases existentes.
# Aquí, "Dog" y "Cat" heredan de la clase "Animal".

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# 3. Polimorfismo
# El polimorfismo permite que objetos de diferentes clases sean tratados como objetos de una clase común.
# En este caso, podemos tratar a "Dog" y "Cat" como "Animal" y llamar al método "make_sound".

def print_sound(animal):
    print(animal.make_sound())

# 4. Encapsulamiento
# El encapsulamiento restringe el acceso directo a algunos de los componentes de un objeto.
# Aquí, usamos un atributo privado para almacenar la salud del animal.

class AnimalWithHealth(Animal):
    def __init__(self, name, age, health):
        super().__init__(name, age)
        self.__health = health

    def get_health(self):
        return self.__health

    def set_health(self, health):
        if 0 <= health <= 100:
            self.__health = health
        else:
            print("Invalid health value")

# Ejemplo de uso
dog = Dog("Rex", 5)
cat = Cat("Miau", 3)
print_sound(dog)  # Salida: Woof
print_sound(cat)  # Salida: Meow

healthy_animal = AnimalWithHealth("Lion", 7, 90)
print(healthy_animal.get_health())  # Salida: 90
healthy_animal.set_health(110)      # Salida: Invalid health value