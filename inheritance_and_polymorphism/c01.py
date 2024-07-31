class Animal:
    def __init__(self) -> None:
        pass

class Mammal(Animal):
    def __init__(self) -> None:
        super().__init__()

class Dog(Mammal):
    def __init__(self) -> None:
        super().__init__()
    
    
