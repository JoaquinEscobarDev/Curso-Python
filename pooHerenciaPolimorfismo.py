# Definimos una clase base llamada Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # Método genérico que será sobrescrito por las clases derivadas
        pass

# Definimos una clase derivada llamada Dog que hereda de Animal
class Dog(Animal):
    def speak(self):
        # Implementación específica del método speak para la clase Dog
        return f"{self.name} says Woof!"

# Definimos una clase derivada llamada Cat que hereda de Animal
class Cat(Animal):
    def speak(self):
        # Implementación específica del método speak para la clase Cat
        return f"{self.name} says Meow!"

# Definimos una función que toma un objeto de tipo Animal y llama a su método speak
def make_animal_speak(animal):
    print(animal.speak())

# Creamos instancias de Dog y Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Usamos polimorfismo para llamar al método speak de cada objeto
make_animal_speak(dog)  # Output: Buddy says Woof!
make_animal_speak(cat)  # Output: Whiskers says Meow!

# Definimos una clase derivada llamada Bird que hereda de Animal
class Bird(Animal):
    def speak(self):
        # Implementación específica del método speak para la clase Bird
        return f"{self.name} says Tweet!"

# Creamos una instancia de Bird
bird = Bird("Tweety")

# Usamos polimorfismo para llamar al método speak del objeto Bird
make_animal_speak(bird)  # Output: Tweety says Tweet!