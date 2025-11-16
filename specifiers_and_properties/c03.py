class BankAccount:
  """
      Class for a bank account, contains an account number and a balance
  """

  def __init__(self, account_number: str, balance: float = 0) -> None:  # Constructor
    self.__account_number: str = account_number
    self.__balance: float = balance

  '''Getters'''

  @property
  # A read-only getter for account number with property decorator
  def account_number(self) -> str:
    return self.__account_number

  @property
  def balance(self) -> float:  # A read-only getter for balance
    return self.__balance

  '''Setters'''

  @balance.setter
  def balance(self, amount: float) -> None:  # set new balance if amount is valid
    if amount >= 0:
      self.__balance = amount
    else:
      raise ValueError("Balance cannot be negative")

  # string representation of the bank account
  def __repr__(self) -> str:
    return f"Account Number: {self.__account_number}\nBalance: {self.__balance}"


# Creating an instance of BankAccount
account: BankAccount = BankAccount("012345678", 1000)

# Attempting to change account number attribute
try:
  print("this next line should trigger an error ...")
  account.account_number = "876543210"
except Exception as err:
  print(f"Error caught: {err}")

# Access via getter (NO brackets because @property is used)
print(account.account_number)
print(account.balance)  # Access via getter

account.balance = 200  # set balance to 200

# Attempting to set negative balance
try:
  print("this next line should trigger an error ...")
  account.balance = -100
except Exception as err:
  print(f"Error caught: {err}")

print(account)  # print details still shows old balance
