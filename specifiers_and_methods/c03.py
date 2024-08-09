from abc import ABC, abstractmethod

# Class to store player skins
class Skins:

    # Static attributes
    SKIN0 = "(^ω^)"
    SKIN1 = "(●´ω｀●)"
    SKIN2 = "ᕦ(ò_óˇ)ᕤ"

    @staticmethod
    def get_skin_names(): # STATIC METHOD to get skin names
        return [attr for attr in dir(Skins) if not callable(getattr(Skins, attr)) and not attr.startswith("__")]

# Player class (abstract class)
class Player(ABC):

    def __init__(self): # Constructor
        super().__init__()
        self._skin = Skins.SKIN0
        self._position = [0, 0]
    
    def set_skin(self, skin):
        self._skin = skin
    
    @property
    def position(self):
        return self._position

    # ABSTRACT METHOD, must be implemented for class to be instantiated
    @abstractmethod
    def attack(self): 
        pass

    def move(self): # VIRTUAL METHOD, has an implementation but is overriden later
        self._position[0] += 1
        self._position[1] += 1
    
    def __repr__(self): # Printing method
        return self._skin

# Warrior class
class Warrior(Player):

    def __init__(self): # Constructor
        super().__init__()
    
    def move(self): # Override virtual method
        self._position[0] += 2
        self._position[1] += 2

    def attack(self): # Override the abstract method
        print("Warrior is attacking with a sword.")

# Mage class
class Mage(Player):

    def __init__(self): # Constructor
        super().__init__()
    
    def move(self): # Override virtual method
        self._position[0] += 0.5
        self._position[1] += 0.5
    
    def attack(self): # Override the abstract method
        print("Mage is casting a fireball.")

# Try to instantiate abstract class Player
try:
    player = Player()
except Exception as err:
    print(f"Error caught: {err}")

# Create instances of the classes
warrior = Warrior()
mage = Mage()

# Attack method (abstract method but overriden)
warrior.attack()
mage.attack()

# Move method (virtual method but overriden)
warrior.move()
mage.move()
print(warrior.position, mage.position)

# Change skins
warrior.set_skin(Skins.SKIN1) # Access static attributes to set skin
mage.set_skin(Skins.SKIN2) # Access static attributes to set skin

# Show skins of warrior and mage
print(warrior)
print(mage)

# See all available skins
print(Skins.get_skin_names())