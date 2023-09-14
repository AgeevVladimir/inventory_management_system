class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: ${self.price} - Quantity: {self.quantity}"


class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, brand, model, warranty_period):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.model = model
        self.warranty_period = warranty_period

    def __str__(self):
        return f"Electronic - {super().__str__()} - Brand: {self.brand} - Model: {self.model} - Warranty: {self.warranty_period} months"


class BookProduct(Product):
    def __init__(self, name, price, quantity, author, publisher, ISBN):
        super().__init__(name, price, quantity)
        self.author = author
        self.publisher = publisher
        self.ISBN = ISBN

    def __str__(self):
        return f"Book - {super().__str__()} - Author: {self.author} - Publisher: {self.publisher} - ISBN: {self.ISBN}"


class ClothingProduct(Product):
    def __init__(self, name, price, quantity, material, size, color):
        super().__init__(name, price, quantity)
        self.material = material
        self.size = size
        self.color = color

    def __str__(self):
        return f"Clothing - {super().__str__()} - Material: {self.material} - Size: {self.size} - Color: {self.color}"
