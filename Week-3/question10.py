#No10
class BankAccount:
    def __init__(self, owner, balance: int):
        self.owner = owner
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount
        return f'Deposited: {amount} current amount: {self.__balance}'
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return 'Withdraw failed. Not enough balance'
        self.__balance -= amount
        return f'Withdrawn: {amount} current amount: {self.__balance}'
    
    def get_balance(self):
        return f'Current account balance: {self.__balance}'
    
acc = BankAccount("Hannah", 3204290)
print(acc.get_balance())