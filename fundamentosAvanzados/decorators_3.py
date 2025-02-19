import datetime

#Implementar un decorador llamado log_employee_action 
#que registre cualquier accion realizada por un empleado en 
#un archivo de texto


def log_employee_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('/home/joaquin/Escritorio/Platzi/Curso-Python/fundamentosAvanzados/employee_actions.log', 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()}: {func.__name__} was called with args: {args}, kwargs: {kwargs}\n")
        return result
    return wrapper