class Account:
    def __init__(self,  account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__( account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest}")

class CheckingAccount(Account):
    def __init__(self, account_holder, balance=0, overdraft_limit=100):
        super().__init__( account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds and overdraft limit reached!")

# Example usage
savings_account = SavingsAccount( account_holder="ion", balance=1000)
checking_account = CheckingAccount( account_holder="ion", balance=500, overdraft_limit=200)

savings_account.deposit(500)
savings_account.calculate_interest()
savings_account.withdraw(200)

checking_account.deposit(300)
checking_account.withdraw(900)
