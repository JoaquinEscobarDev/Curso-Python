class BaseClass:
    def __init__(self):
        self._protected_variable = 'Protected'
        
    
    def _protected_method(self):
        print('Este es un metodo protegido')

base = BaseClass()
print(base._protected_variable)
base._protected_method()