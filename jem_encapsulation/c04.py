class Rocket:
    def __init__(self, size):
        self.fuel_mass = 200 * size
        # Need some oxygen to burn the fuel
        self.oxygen_mass = 200 * size
        self.structure_mass = 300 * size

    def calculate_mass(self):
        return self.fuel_mass + self.oxygen_mass + self.structure_mass


class PassengerRocket(Rocket):
    def __init__(self, passenger_capacity):
        super().__init__(passenger_capacity + 2)
        self.passenger_capacity = passenger_capacity
        # Need extra oxygen for breathing
        self.oxygen_mass += passenger_capacity * 100

    def calculate_mass(self):
        # Include the mass of the astronauts
        return super().calculate_mass() + self.passenger_capacity * 50


class SpaceStation:
    def __init__(self):
        self.fuel_reserve = 10000
        self.astronauts = 2

    def refuel(self, rocket):
        if rocket.fuel_mass < 1000:
            self.fuel_reserve = self.fuel_reserve - 1000 + rocket.fuel_mass
            rocket.fuel_mass = 1000

    def dock(self, passenger_rocket):
        print(f"A rocket carrying {passenger_rocket.passenger_capacity} passengers of mass "
              f"{passenger_rocket.calculate_mass()} has docked safely")
        self.astronauts += passenger_rocket.passenger_capacity

    def dispatch(self, passenger_rocket):
        print(f"Farewell to {passenger_rocket.passenger_capacity} astronauts returning home")
        self.astronauts -= passenger_rocket.passenger_capacity


station = SpaceStation()
rocket = PassengerRocket(2)
station.dock(rocket)
station.refuel(rocket)
station.dispatch(rocket)
