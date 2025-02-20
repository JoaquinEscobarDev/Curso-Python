class Employee:
    def __init__(self, name, salary):
        # Inicializa el nombre y el salario del empleado
        self.name = name
        self._salary = salary
    
    @property
    def salary(self):
        # Devuelve el salario del empleado
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        # Establece un nuevo salario para el empleado, si es válido
        if new_salary < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = new_salary
        
        
    @salary.deleter
    def salary(self):
        print(f'The salary of {self.name} has been deleted')
        del self._salary
        

# Crea una instancia de la clase Employee con nombre "Ana" y salario 5000
employee = Employee("Ana", 5000)
# Imprime el salario actual del empleado
print(employee.salary)

# Actualiza el salario del empleado a 6000
employee.salary = 6000
# Imprime el nuevo salario del empleado
print(employee.salary)

# Intenta establecer un salario negativo (comentado porque lanzaría una excepción)
# employee.salary = -1000
# print(employee.salary)

# Elimina el salario 
del employee.salary
