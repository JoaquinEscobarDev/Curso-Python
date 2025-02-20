#Implementar una clase CuentaBancaria con un metodo proegido pr ctulizr el sldo y un metodo 
#privado par registrar las transacciones internamente
#el metodo protegido(_actualizar_saldo) solo debe ser utilizado dentro de la clase y sus subclases
#el metodo provado (__registrar_transaccion) debe ser completamente interno y no accesible fuera de la clase

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        # Inicializa la cuenta bancaria con un saldo inicial
        self.saldo = saldo_inicial
        self.__transacciones = []

    def depositar(self, cantidad):
        # Método público para depositar dinero en la cuenta
        self._actualizar_saldo(cantidad)
        self.__registrar_transaccion('Depósito', cantidad)

    def retirar(self, cantidad):
        # Método público para retirar dinero de la cuenta
        if cantidad <= self.saldo:
            self._actualizar_saldo(-cantidad)
            self.__registrar_transaccion('Retiro', cantidad)
        else:
            print("Saldo insuficiente")

    def _actualizar_saldo(self, cantidad):
        # Método protegido para actualizar el saldo
        self.saldo += cantidad

    def __registrar_transaccion(self, tipo, cantidad):
        # Método privado para registrar una transacción
        self.__transacciones.append({'tipo': tipo, 'cantidad': cantidad})

    def obtener_saldo(self):
        # Método público para obtener el saldo actual
        return self.saldo

    def obtener_transacciones(self):
        # Método público para obtener el historial de transacciones
        return self.__transacciones

# Prueba funcional
if __name__ == "__main__":
    cuenta = CuentaBancaria(1000)
    print("Saldo inicial:", cuenta.obtener_saldo())
    
    cuenta.depositar(500)
    print("Saldo después del depósito:", cuenta.obtener_saldo())
    
    cuenta.retirar(200)
    print("Saldo después del retiro:", cuenta.obtener_saldo())
    
    cuenta.retirar(1500)  # Intento de retiro con saldo insuficiente
    
    print("Historial de transacciones:", cuenta.obtener_transacciones())