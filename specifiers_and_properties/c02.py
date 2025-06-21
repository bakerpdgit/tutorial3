class Person:
    '''Person class as a base class'''

    def __init__(self, name: str, age: int) -> None:
        self._age: str = ______  # age (protected)
        self._name: int = ______  # private (protected)

    '''GETTERS'''

    def get_age(self) -> str:  # Getter for age
        return ________

    def get_name(self) -> int:  # Getter for name
        return _______

    '''SETTERS'''

    def set_age(self, age: int) -> None:  # Setter for age with validation
        if age >= 0:
            _______ = age
        else:
            raise ValueError("Age cannot be negative")

    def set_name(self, name: str) -> None:  # Setter for name with validation
        if len(name) > 0 and name.isalpha():
            ________ = name
        else:
            raise ValueError(
                "Name cannot be empty or contain non-alphabetic characters")


class Employee(Person):
    '''Employee class inherits from Person class'''

    def __init__(self, name: str, age: int, employee_id: int):
        super().__init__(name, age)  # Call the parent class constructor
        self.__employee_id: int = _________  # Additional private attribute for Employee

    def get_employee_id(self) -> int:
        return _____________

    def set_employee_id(self, employee_id: str) -> None:
        try:
            employee_id_int = int(employee_id)
            if employee_id_int >= 0:
                _____________ = employee_id_int
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
print(employee.get_age(), employee.________(), employee.get_employee_id())
