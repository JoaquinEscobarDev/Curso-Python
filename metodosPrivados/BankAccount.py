#Implementar una clase CuentaBancaria con un metodo proegido pr ctulizr el sldo y un metodo 
#privado par registrar las transacciones internamente

class BankAccount:
    def __init__(self, initial_balance=0):
        # Inicializa la cuenta bancaria con un saldo inicial y una lista de transacciones
        self._balance = initial_balance
        self.__transactions = []

    def deposit(self, amount):
        # Verifica que el monto a depositar sea positivo
        if amount > 0:
            # Incrementa el saldo con el monto del depósito
            self._balance += amount
            # Registra la transacción como un depósito
            self.__record_transaction('deposit', amount)

    def withdraw(self, amount):
        # Verifica que el monto a retirar sea positivo y no exceda el saldo actual
        if 0 < amount <= self._balance:
            # Deduce el monto del saldo
            self._balance -= amount
            # Registra la transacción como un retiro
            self.__record_transaction('withdraw', amount)

    def get_balance(self):
        # Retorna el saldo actual de la cuenta
        return self._balance

    def _update_balance(self, amount):
        # Método protegido para actualizar el saldo
        self._balance += amount

    def __record_transaction(self, transaction_type, amount):
        # Método privado para registrar las transacciones internamente
        self.__transactions.append({'type': transaction_type, 'amount': amount})

    def get_transactions(self):
        # Retorna la lista de transacciones
        return self.__transactions

# Prueba de la clase BankAccount
if __name__ == "__main__":
    account = BankAccount(100)  # Crea una cuenta con un saldo inicial de 100
    account.deposit(50)         # Deposita 50 en la cuenta
    account.withdraw(30)        # Retira 30 de la cuenta
    print("Balance:", account.get_balance())  # Imprime el saldo actual
    print("Transactions:", account.get_transactions())  # Imprime la lista de transacciones