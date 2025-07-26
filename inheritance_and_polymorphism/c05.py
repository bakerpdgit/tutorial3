class Vehicle:
  """
      Vehicle has a make, model and year
  """

  def __init__(self, make: str, model: str, year: int) -> None:
    self._make: str = make
    self._model: str = _____
    self._year: int = _____

  # virtual method
  def description(self) -> str:
    return f"{self._year} {self._make} {self._model}"


class Car(________):
  """
      Car is a vehicle with a fuel type
  """

  def __init__(self, make: str, model: str, year: int, fuel_type: str):
    super().___________(make, model, year)
    self._fuel_type: str = _______

  # add fuel type to the parent class's description
  # virtual method
  def description(self) -> str:
    return ________.description() + f", Fuel Type: {self._fuel_type}"


class ElectricCar(_______):
  """
      Electric car is a car with a battery capacity and has an electric fuel type
  """

  def __init__(self, make: str, model, year, battery_capacity) -> None:
    super()._________(make, model, year, fuel_type="Electric")
    self.____________ = battery_capacity

  # add battery capacity to parent class's description
  def description(self) -> str:
    return ________.description(
    ) + f", Battery Capacity: {self._battery_capacity} kWh"


class Bicycle(_______):
  """
      Bicycle is a vehicle with a gear count and a bell
  """

  def __init__(self, make: str, model: str, year: int,
               gear_count: int) -> None:
    super().__init__(make, model, year)
    self.________ = gear_count

  def description(self) -> str:
    return super().____________ + f", Gear Count: {self._gear_count}"

  def ring_bell(self) -> str:  # unique method of bicycle
    return "Ring ring!"


# Create instances of each class
vehicle: Vehicle = Vehicle("GenericMake", "GenericModel", 2020)
car: Car = Car("Toyota", "Corolla", 2021, "Gasoline")
electric_car: ElectricCar = ElectricCar("Tesla", "Model 3", 2022, 75)
bicycle: Bicycle = Bicycle("Giant", "Escape 3", 2023, 21)

# Basic description of each variable using polymorphism
vehicles: list[Vehicle] = [vehicle, car, electric_car, bicycle]
for v in vehicles:
  print(v.description())

# Test unique method of Bicycle
print(bicycle.ring_bell())
