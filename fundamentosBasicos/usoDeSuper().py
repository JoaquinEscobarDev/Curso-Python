class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hi, I'm {self.name}, and I'm a student with ID: {self.student_id}")

# Crear instancia de Student y llamar a greet
student = Student("Ana", 20, "S12345")
student.greet()  # Output: Hello! I am a person.
#Hi, I'm Ana, and I'm a student with ID: S12345


def __str__(self):
    return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"

def __repr__(self):
    return self.__str__()

def __eq__(self, other):
    if isinstance(other, Student):
        return self.student_id == other.student_id
    return False

def __lt__(self, other):
    if isinstance(other, Student):
        return self.age < other.age
    return NotImplemented

# Crear otra instancia de Student para comparar
student2 = Student("Luis", 22, "S12346")

# Comparar estudiantes
print(student == student2)  # Output: False
print(student < student2)   # Output: True

# Representación de los objetos
print(student)  # Output: Student(name=Ana, age=20, student_id=S12345)
print(repr(student2))  # Output: Student(name=Luis, age=22, student_id=S12346)