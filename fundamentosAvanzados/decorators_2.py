
def check_acces(func):
    def wrapper(employee):
        #Comprobar el rol 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('Acceso denegado. solo los administradores pueden acceder.')
    return wrapper
      
        
@check_acces
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado.')

admin = {'name': 'Carlos', 'role': 'admin'} 
employee = {'name': 'Joaquin', 'role': 'employee'} 

delete_employee(admin)
delete_employee(employee)  
    