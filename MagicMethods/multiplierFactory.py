class MultiplierFactory:
    
    def __init__(self, factor: int):
        print(f'Inicializando con factor {factor}')
        self.factor = factor
        
    def __new__(cls, factor: int):
        print(f'Creando instancia con factor {factor}')
        return super(MultiplierFactory, cls).__new__(cls)
      
    def __call__(self, number: int) -> int:
        return number * self.factor
    
    