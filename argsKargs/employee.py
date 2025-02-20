class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.detail = kwargs
        
    def show_employee(self):
        print(f'Employee {self.name}')
        print('Skills', self.skills)
        print('Detail', self.detail)
    

employee = Employee('Carlos', 'Python','Java','C++', age = 30, city = 'Santiago')
employee.show_employee()

        