class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Nombre del titular de la cuenta
        self.balance = balance  # Saldo de la cuenta
        self.is_active = True  # Estado de la cuenta (activa/inactiva)
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount  # Incrementa el saldo con el monto depositado
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")  # Mensaje de error si la cuenta está inactiva

    def withdraw(self, amount):
        if self.is_active:  # Verifica si la cuenta está activa
            if amount <= self.balance:
                self.balance -= amount  # Decrementa el saldo con el monto retirado
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}")

    def desactive_account(self):
        self.is_active = False  # Desactiva la cuenta
        print("La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True  # Activa la cuenta
        print("La cuenta ha sido activada")

# Crear cuentas bancarias
account1 = BankAccount("Joaquin", 500)
account2 = BankAccount("Camila", 1000)

# Llamada de métodos
account1.deposit(200)  # Depositar en la cuenta 1
account2.deposit(200)  # Depositar en la cuenta 2
account1.desactive_account()  # Desactivar la cuenta 1
account1.deposit(100)  # Intentar depositar en la cuenta 1 inactiva
account1.activate_account()  # Activar la cuenta 1
account1.deposit(100)  # Depositar en la cuenta 1 activa