import random

class User():
    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account

    def show_details(self):
        print("Banking details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Account: ", self.account)


class Bank(User):
    def __init__(self, name, age, account):
        super().__init__(name, age, account)
        self.balance = random.randint(100,150)

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated: NOK", self.balance)

    def withdrawal(self, amount):
        self.amount = amount
        if self.amount> self.balance:
            print("Insufficient funds, balance available: NOK", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: NOK", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: NOK", self.balance)

