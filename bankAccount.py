class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Corregir el nombre del atributo
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")  # Corregir el mensaje de error

    def withdraw(self, amount):
        if self.is_active:  # Corregir el nombre del atributo
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}")

    def desactive_account(self):
        self.is_active = False
        print("La cuenta ha sido desactivada")  # Corregir el mensaje de error

    def activate_account(self):
        self.is_active = True
        print("La cuenta ha sido activada")


account1 = BankAccount("Joaquin", 500)
account2 = BankAccount("Camila", 1000)

#llamada de metodos

account1.deposit(200)  
account2.deposit(200)
account1.desactive_account()
account1.deposit(100)
account1.activate_account()  # Activar la cuenta
account1.deposit(100)