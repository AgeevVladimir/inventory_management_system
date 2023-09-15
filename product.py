from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int

    def __str__(self):
        return f"{self.name} - Price: ${self.price} - Quantity: {self.quantity}"


class ElectronicProduct(Product):
    brand: str
    model: str
    warranty_period: int

    def __str__(self):
        return f"Electronic - {super().__str__()} - " \
               f"Brand: {self.brand} - " \
               f"Model: {self.model} - " \
               f"Warranty: {self.warranty_period} months"


class BookProduct(Product):
    author: str
    publisher: str
    ISBN: str

    def __str__(self):
        return f"Book - {super().__str__()} - " \
               f"Author: {self.author} - " \
               f"Publisher: {self.publisher} - " \
               f"ISBN: {self.ISBN}"


class ClothingProduct(Product):
    material: str
    size: str
    color: str

    def __str__(self):
        return f"Clothing - {super().__str__()} - " \
               f"Material: {self.material} - " \
               f"Size: {self.size} - " \
               f"Color: {self.color}"
