'''
class BankAccount:
    def __init__(self, holder, balance, deposit, withdraw):
        self.holder = holder
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
    def deposit(self):
        self.balance += deposit
        return self.balance
    
    def withdraw(self):
        self.balance -= withdraw
        return self.balance
'''
# Prof.Kaur's 100 times better version
class BankAccount:
    def __init__(self, name, balance): # no dunder, cuz it's refering to the argument 
        self.__name = name # create an attribute called 'name' inside of the BankAccount object

    def deposite(self, amount):
        self.__balance += amount # access the 'balance' attribute
        
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            
        self.__balance -= amount
        
    def __str__(self): # automatically access to private becuz it's inside the class 
        return f"Account Holder: {self.__name}," + \
               f"Balance: {self.__balance}"

def main():
    amrita_account = BankAccount("Amerita", 100)
    mike_account = BankAccount("Mike", 1000)

    amirita_account.deposite(500) 
if __name__ == "__main__":
    
