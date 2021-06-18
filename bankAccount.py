class BankAccount:
    def __init__(self, int_rate = 0.0345, balance = 100.0):
        self.rate = int_rate
        self.acctBalance = balance

    def deposit(self, amount):
        self.acctBalance += amount
    
    def withdraw(self, amount):
        self.acctBalance -= amount

    def display_account_info(self):
        print("Balance: ", self.acctBalance)

    # def getMonthlyInterestRate(self):
    #     return self.rate / 12

    def yield_interest(self):
        self.acctBalance += self.acctBalance * self.rate

bnkacct1 = BankAccount(0.0345, 150)

bnkacct1.deposit(150)
bnkacct1.yield_interest()
bnkacct1.display_account_info()


