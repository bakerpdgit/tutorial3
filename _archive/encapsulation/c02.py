class Fleet:
  def __init__(self, vehicles):
    self.vehicles = vehicles

  def dispatch_by_registration(self, registration, destination):
    _, vehicle = self.get_vehicle_by_registration(registration)
    vehicle.travel(destination)

  def locate_by_registration(self, name):
    _, vehicle = self.get_vehicle_by_registration(name)
    vehicle.locate()

  def get_vehicle_by_registration(self, registration):
    for i, vehicle in enumerate(self.vehicles):
      if registration == vehicle.registration:
        return i, vehicle
    raise ValueError(f"No vehicle named {registration} exists")


class Vehicle:
  def __init__(self, name, registration):
    self.name = name
    self.registration = registration
    self.location = "depot"

  def travel(self, destination):
    self.move_distance(self.get_distance(self.location, destination))
    self.location = destination

  def locate(self):
    print(f"{self.name} is at {self.location}")

  def get_distance(self, start, end):
    # These vehicles travel by changing letters
    return max(len(start), len(end)) - \
        sum(map(lambda x: x[0] == x[1], zip(start, end)))

  def move_distance(self, distance):
    pass


class Car(Vehicle):
  def __init__(self, name, registration):
    super().__init__(name, registration)
    self.fuel = 10

  def travel(self, destination):
    print(f"Vroom vroom! {self.name} is travelling to {destination}")
    super().travel(destination)

  def move_distance(self, distance):
    self.fuel -= distance
    if self.fuel <= 0:
      print("Oh no! The car is out of fuel")


class Bicycle(Vehicle):
  def move_distance(self, distance):
    print(("huff puff " * (distance // 2))[:-1])


fleet = Fleet([
    Car("Car one", "AB01 CDE"),
    Bicycle("Bicycle one", "FG23 HIJ")
])
fleet.dispatch_by_registration("AB01 CDE", "New York")
fleet.dispatch_by_registration("AB01 CDE", "New Orleans")
fleet.locate_by_registration("FG23 HIJ")
