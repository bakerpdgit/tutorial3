class Dog: # Dog Class
    
    def __init__(self):
        pass

    def sound(self):
        print("Woof!")

class Cat: # Cat Class

    def __init__(self):
        pass

    def sound(self):
        print("Meow!")

class Bulldog(Dog): # Bulldog class, inherits from Dog

    def __init__(self):
        super().__init__()

    def sound(self): # OVERRIDING: Override method inherited from Dog
        print("Woof! I'm a Bulldog!")

class PersianCat(Cat): # Persian Cat class, inherits from Cat

    def __init__(self):
        super().__init__()

    def sound(self): # OVERRIDING: Override method inherited from Cat
        print("Meow! I'm a Persian Cat!")

# Call method for each animal, example of run-time polymorphism
# Note that Dog and Cat are unrelated classes, yet they can be accessed from the same interface (NOT overriding)
def make_sound(animal):
    animal.sound()

# Create instances of each class
dog = Dog()
cat = Cat()
bulldog = Bulldog()
persian_cat = PersianCat()

# RUN-TIME POLYMORPHISM: one interface for multiple objects
make_sound(dog)
make_sound(cat)
make_sound(bulldog)
make_sound(persian_cat)

