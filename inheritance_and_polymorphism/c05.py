class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self._make: str = make
        self._model: str = model
        self._year : int = year

    def description(self):
        return f"{self._year} {self._make} {self._model}"


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
    _________.__init__(make, model, year)
    self.fuel_type = fuel_type

def description(self):  # add fuel type to the parent class's description
    return super()._________ + f", Fuel Type: {self.fuel_type}"


class ElectricCar(________):
    def __init__(self, make, model, year, battery_capacity):
    __________.__init__(make, model, year, fuel_type="Electric")
    self._______________ = battery_capacity

def description(self):  # add battery capacity to parent class's description
    return ________.description() + f", Battery Capacity: {self.battery_capacity} kWh"


class Bicycle(_________):
    def __init__(self, make, model, year, gear_count):
    super().__init__(make, model, year)
    self.gear_count = __________

def description(self):
    return super().description() + f", Gear Count: {self.gear_count}"

def ring_bell(self):  # unique method of bicycle
    return "Ring ring!"


# Create instances of each class
vehicle = Vehicle("GenericMake", "GenericModel", 2020)
car = Car("Toyota", "Corolla", 2021, "Gasoline")
electric_car = ElectricCar("Tesla", "Model 3", 2022, 75)
bicycle = Bicycle("Giant", "Escape 3", 2023, 21)

# Basic description of each variable using polymorphism
vehicles : list[Vehicle] = [vehicle, car, electric_car, bicycle]
for v in vehicles:
    print(v.description())

# Test unique method of Bicycle
print(bicycle._________())
