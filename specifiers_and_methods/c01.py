class BankAccount: # Class for bank account
    
    def __init__(self, account_number, balance=0): # Constructor
        self.__account_number = account_number
        self.__balance = balance
    
    '''Getters'''
    
    @property
    def account_number(self): # A getter for account number with property decorator
        return self.__account_number
    
    def get_balance(self): # A getter for balance
        return self.__balance
    
    '''Setters'''

    def deposit(self, amount): # Deposit money (add to balance)
        self.__balance += amount

    def withdraw(self, amount): # Withdraw money (subtract from balance)
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    # Method used to show specific message if class object is printed.
    # If this is not included, printing the class will show <__main__.BankAccount object at some address>
    def __repr__(self): 
        return f"Account Number: {self.__account_number}\nBalance: {self.__balance}"



# Creating an instance of BankAccount
account = BankAccount("1234567890", 1000)

# Attempting to access private attribute
try:
    print(account.__account_number)
except Exception as err:
    print(f"Error caught: {err}")

print(account.account_number) # Access via getter (NO brackets because @property is used)
print(account.get_balance()) # Access via getter

account.deposit(200) # deposit 200

# WHENEVER you call print(object), the string returned from __repr__ is printed
print(account) # print details

account.withdraw(100) # withdraw 100

print(account) # print details

account.withdraw(1500) # try to withdraw 1500

print(account) # print details

