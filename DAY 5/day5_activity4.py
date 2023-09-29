class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0) -> None:
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def check_balance(self):
        print(f"Current balance for {self.account_holder}: ${self.balance}")