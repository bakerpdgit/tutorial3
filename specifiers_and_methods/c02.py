class Person: # Person Class
    def __init__(self, name, age):
        self._age = ______  # age (protected)
        self._name = ______  # private (protected)

    def get_age(self): # Getter for age
        return ________
    
    def set_age(self, age): # Setter for age
        _______ = age
        
    def get_name(self): # Getter for name
        return _______

    def set_name(self, name): # Setter for name
        ________ = name

class Employee(Person): # Employee class inherits from Person class

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call the parent class constructor
        self.__employee_id = _________  # Additional attribute for Employee

    def get_employee_id(self):
        return _____________

    def set_employee_id(self, employee_id):
        _____________ = employee_id

employee = Employee("John", 25, 1234)

# get attributes
print(employee.________(), employee.get_name(), employee.get_employee_id())

employee.set_age(30) # set age
employee.set_name("Mike") # set name
employee.____________(5678) # set employee id

# get attributes
print(employee.get_age(), employee.________(), employee.get_employee_id())
