class BankAccount:
    """
        Class for a bank account, contains an account number and a balance
    """

    def __init__(self, account_number: str) -> None:  # Constructor
        self.__account_number: str = account_number
        self.__balance: float = 0

    '''Getters'''

    @property
    def account_number(self) -> str:  # A read-only getter for account number with property decorator
        return self.__account_number

    @property
    def balance(self) -> float:  # A read-only getter for balance
        return self.__balance

    '''Bank methods'''

    def deposit(self, amount: float) -> None: # add money to bank
        """
            Method to deposit money into the bank
        """
        if amount >= 0:
            self.__balance += amount
        else:
            ValueError("Amount added cannot be negative")

    def withdraw(self, amount: float) -> None: # remove money from bank
        """
            Method to withdraw money from the bank
        """
        if amount < 0:
            raise ValueError("Amount withdrawn is negative")
        elif amount > self.__balance:
            raise ValueError("Amount withdrawn exceeds the current balance")
        else:
            self.__balance -= amount

    # string representation of the bank account 
    def __repr__(self) -> str:
        return f"BankAccount(Account Number: {self.__account_number}, Balance: {self.__balance})"


# Creating an instance of BankAccount
account: BankAccount = BankAccount("012345678")

account.deposit(1000) # add 1000 to bank

# Access via getter (NO brackets because @property is used)
print(account.account_number, account.balance) # Access via getters

try:
    print("this next line should trigger an error ...")
    account.withdraw(2000) # do not have enough money
except Exception as err:
    print(f"Error caught: {err}")

account.withdraw(600) # have enough money

print(account)  # print details still shows old balance
