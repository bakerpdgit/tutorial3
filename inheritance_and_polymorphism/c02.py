class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make: str = _____
        self.____: str = model
        self.year: int = ______

    def description(self) -> str:
        return f"{self.year} {self.make} {self.model}"


class Car(________):
    def __init__(self, make: str, model: str, year: int, fuel_type: str) -> None:
        _________.__init__(make, model, year)
        self.fuel_type: str = fuel_type

    def description(self) -> str:  # add fuel type to the parent class's description
        return super()._________ + f", Fuel Type: {self.fuel_type}"


class ElectricCar(________):
    def __init__(self, make: str, model: str, year: str, battery_capacity: int) -> None:
        __________.__init__(make, model, year, fuel_type="Electric")
        self._______________ = battery_capacity

    def description(self) -> str:  # add battery capacity to parent class's description
        return ________.description() + f", Battery Capacity: {self.battery_capacity} kWh"


class Bicycle(_________):
    def __init__(self, make: str, model: str, year: int, gear_count: int) -> None:
        super().__init__(make, model, year)
        self.gear_count: int = __________

    def description(self) -> str:
        return super().description() + f", Gear Count: {self.gear_count}"

    def ring_bell(self) -> str:  # unique method of bicycle
        return "Ring ring!"


# Create instances of each class
vehicle: Vehicle = Vehicle("GenericMake", "GenericModel", 2020)
car: Car = Car("Toyota", "Corolla", 2021, "Gasoline")
electric_car: ElectricCar = ElectricCar("Tesla", "Model 3", 2022, 75)
bicycle: Bicycle = Bicycle("Giant", "Escape 3", 2023, 21)

# Basic description of each vehicle
print(vehicle.description())
print(car.description())
print(electric_car.description())
print(bicycle.description())

# Test unique method of Bicycle
print(bicycle._________())
