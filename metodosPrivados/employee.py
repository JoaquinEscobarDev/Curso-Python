class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannet be negative")
        self._salary = new_salary
        
employee = Employee("Ana", 5000)
print(employee.salary)

employee.salary = 6000
print(employee.salary)

# employee.salary = -1000
# print(employee.salary)
