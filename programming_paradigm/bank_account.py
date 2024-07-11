class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0 #default balance for all account instances

    def display_balance(self):
        balance = self.account_balance
        print(f"Current Balance: $[{float(balance)}]")

    def deposit(self, amount):
        self.account_balance += amount
        self.initial_balance += self.account_balance
    
    def withdraw(self, amount):
        if amount < self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")