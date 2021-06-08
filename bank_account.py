class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate =  0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = self.balance - amount - 5
            return print("Insufficient funds: Charging a $5 fee"), self
        else:
            self.balance -= amount
            return self
    
    def display_account_info(self):
        return print(f"Balance: {self.balance}"), self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
            return self


account1 = BankAccount(balance=1)
account2 = BankAccount(0.5, 50000)

account1.deposit(500).deposit(600).deposit(700).withdraw(1200).yield_interest().display_account_info()
account2.deposit(700).deposit(700).withdraw(5).withdraw(700).withdraw(10000).withdraw(678).yield_interest().display_account_info()