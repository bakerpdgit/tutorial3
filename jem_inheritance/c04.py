import math


class GasGiant:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    def get_volume(self):
        return 4/3 * math.pi * self.radius ** 3

    def get_density(self):
        return self.mass / self.get_volume()

    def get_surface_gravity(self):
        return 6.67E-11 * self.mass / self.radius ** 2

    def establish_orbital_base(self, height):
        orbital_velocity = math.sqrt(6.67E-11 * self.mass / (self.radius + height))
        print(f"The base orbits {height}m above the surface of the planet at a speed of {orbital_velocity}m/s")


class SaturnianPlanet(GasGiant):
    def __init__(self, total_mass, radius, ring_mass):
        super().__init__(total_mass, radius)
        self.ring_mass = ring_mass

    def get_density(self):
        return (self.mass - self.ring_mass) / self.get_volume()

    def establish_orbital_base(self, height):
        super().establish_orbital_base(height)
        # or equivalently GasGiant.establish_orbital_base(self, height)
        print("The new base has a beautiful aerial view of the planet's rings")


saturn = SaturnianPlanet(568E26, 60268, 1.5E19)
saturn.establish_orbital_base(100)
