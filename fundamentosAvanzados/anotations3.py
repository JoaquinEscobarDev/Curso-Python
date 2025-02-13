class employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary


    def introduce(self) -> str:
        return f"Hola soy {self.name}.\nTengo {self.age} años."

employee1 = employee('Carlos',30, 5000.0)
print(employee1.introduce())
