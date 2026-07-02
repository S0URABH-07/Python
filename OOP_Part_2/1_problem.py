# BankAccount problem with private variable __Var
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(10000)

account.deposit(5000)
account.withdraw(12000)
account.show_balance()