from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class Product(BaseModel, metaclass=ABCMeta):
    category: str = "Default Category"
    subcategory: str
    price: float = 0
    quantity: int = 0

    @abstractmethod
    def key_attributes(self):
        pass

    def __str__(self):
        return f"Price: ${self.price}; Quantity: {self.quantity}"


class ElectronicProduct(Product):
    category: str = "Electronics"
    subcategory: str
    brand: str
    model: str
    warranty_period: int

    def key_attributes(self):
        return self.subcategory, self.brand, self.model, self.warranty_period

    def __str__(self):
        return f"Category: {self.category}; " \
               f"Subcategory: {self.subcategory}; " \
               f"Brand: {self.brand}; " \
               f"Model: {self.model}; " \
               f"Warranty: {self.warranty_period} months; " \
               f"{super().__str__()}"


class BookProduct(Product):
    category: str = "Books"
    subcategory: str
    title: str
    author: str
    publisher: str
    ISBN: str

    def key_attributes(self):
        return self.subcategory, self.title, self.author, self.publisher, self.ISBN

    def __str__(self):
        return f"Category: {self.category}; " \
               f"Subcategory: {self.subcategory}; " \
               f"Title: {self.title}; " \
               f"Author: {self.author}; " \
               f"Publisher: {self.publisher}; " \
               f"ISBN: {self.ISBN}; " \
               f"{super().__str__()}"


class ClothingProduct(Product):
    category: str = "Clothing"
    subcategory: str
    material: str
    size: str
    color: str

    def key_attributes(self):
        return self.subcategory, self.material, self.size, self.color

    def __str__(self):
        return f"Category: {self.category}; " \
               f"Subcategory: {self.subcategory}; " \
               f"Material: {self.material}; " \
               f"Size: {self.size}; " \
               f"Color: {self.color}; " \
               f"{super().__str__()}"
