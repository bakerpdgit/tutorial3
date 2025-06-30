# Allowing type annotations to be used before it is fully defined
from __future__ import annotations

class Product:

    # A static class attribute to store all products
    _registry: dict[str, Product] = {}

    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price
        Product._registry[name] = self

    # SEE THE DESCRIPTION IN THE EXERCISE FOR WHY @classmethod IS USED HERE
    @classmethod
    def get_product(cls, name) -> Product:
        return cls._registry[name]

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price})"


class ProductFactory:

    # ADD A STATIC METHOD TO THIS FACTORY CLASS THAT CREATES A PRODUCT
    @___________________
    def create_product(name: str, price: float) -> Product:
        if name in Product._registry:
            print(f"Product '{name}' already exists.")
            return Product.get_product(name)
        else:
            print(f"Creating product '{name}'.")
            return _______(name, price)


# Usage
product1: Product = ProductFactory.create_product("Laptop", 1500)
product2: Product = ProductFactory.create_product("Smartphone", 800)

# TRY TO CREATE A PRODUCT THAT ALREADY EXISTS
product3: Product = ProductFactory.________________("Laptop", 1600)

print(Product.get_product("Smartphone"))
print(Product.get_product("Laptop"))
