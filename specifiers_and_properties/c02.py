class Employee:
  """
      Class for an employee, contains a name, age and employee id
  """

  def __init__(self, name: str, age: int, employee_id: int):
    self.__age: int = age  # private variable for age
    self.__name: str = _______  # private variable for name
    self.__employee_id: int = ________  # private variable for employee id

  '''GETTERS'''

  def get_age(self) -> int:  # Getter for age
    return self.__age

  def get_name(self) -> str:  # Getter for name
    return __________

  def get_employee_id(self) -> int:
    return self.__employee_id

  '''SETTERS'''

  def set_age(self, age: int) -> None:  # Setter for age with validation
    if age >= 0:
      _________ = age
    else:
      raise ValueError("Age cannot be negative")

  def _______________(self, name: str) -> None:  # Setter for name with validation
    if len(name) > 0 and name.isalpha():
      ________ = name
    else:
      raise ValueError(
          "Name cannot be empty or contain non-alphabetic characters")

  def set_employee_id(self, employee_id: str | int) -> None:  # Setter for employee id
    try:
      employee_id_int = int(employee_id)
      if employee_id_int >= 0:
        __________ = employee_id_int
      else:
        raise ValueError("Employee ID cannot be negative")
    except ValueError:
      raise ValueError("Employee ID must be an integer")


employee: Employee = Employee("John", 25, 1234)

# get attributes
print(employee.________(), employee.get_name(), employee.get_employee_id())

employee.set_age(30)  # set age
employee.set_name("Mike")  # set name
employee.____________(5678)  # set employee id

# get attributes
print(employee.get_age(), employee._________(), employee.get_employee_id())
