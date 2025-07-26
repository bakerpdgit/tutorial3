import math


class TerrestrialPlanet:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    def get_volume(self):
        return 4/3 * math.pi * self.radius ** 3

    def get_density(self):
        return self.mass / self.get_volume()

    def get_surface_gravity(self):
        return 6.67E-11 * self.mass / self.radius ** 2

    def mine_resources(self):
        self.mass -= 3E12
        print("Harvested 3bn tonnes of ores (this is about the amount mined annually on Earth)")

    def establish_terrestrial_base(self):
        self.mass += 1E6
        print("Built a 1000 tonne base on the surface of the planet")


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


class IceGiant:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    def get_volume(self):
        return 4 / 3 * math.pi * self.radius ** 3

    def get_density(self):
        return self.mass / self.get_volume()

    def get_surface_gravity(self):
        return 6.67E-11 * self.mass / self.radius ** 2

    def establish_subsurface_base(self, depth):
        pressure = self.get_density() * self.get_surface_gravity() * depth
        print(f"The base needs to be able to endure a pressure of approximately {pressure}Pa")


earth = TerrestrialPlanet(5.97E24, 6371)
print(earth.get_surface_gravity())
earth.mine_resources()

jupiter = GasGiant(1.90E27, 69911)
print(jupiter.get_volume())
jupiter.establish_orbital_base(100)

neptune = IceGiant(1.02E26, 24622)
print(neptune.get_density())
neptune.establish_subsurface_base(10)
