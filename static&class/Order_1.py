class Order:
    # Descuento global aplicable a todas las órdenes
    global_discount = 10
    
    def __init__(self, amount):
        # Inicializa la instancia con un monto específico
        self.amount = amount
        
    @classmethod
    def update_global_discount(cls, new_discount):
        # Actualiza el descuento global con un nuevo valor
        cls.global_discount = new_discount
        
# Actualiza el descuento global a 15
Order.update_global_discount(15)
# Imprime el valor del descuento global actualizado
print(Order.global_discount)