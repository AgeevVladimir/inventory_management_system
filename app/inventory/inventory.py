"""
Inventory Management System

This class represents the core functionality of the inventory management system:
- `add_product`: Adds a new product to the inventory.
- `remove_product`: Removes an existing product from the inventory.
- `update_product`: Modifies attributes of an existing product.
- `check_quantity`: Returns the quantity of a specified product.
- `search_products`: Searches for products based on a query string.
- `get_products_by_category`: Retrieves products of a specified category.

The class uses decorators to validate certain operations, such as checking the existence of a product before modifying it.
"""

from functools import wraps
from typing import Dict, List

from app.model.product_models import Product


class Inventory:

    def __init__(self):
        self.products: Dict[tuple, Product] = {}

    def check_product_existence(f):

        @wraps(f)
        def wrapper(self, *args, **kwargs):
            product = args[0]
            key = product.key_attributes()
            existing_product = self.products.get(key)
            if not existing_product:
                raise ValueError("Trying to operate on a product that doesn't exist")
            return f(self, *args, **kwargs)

        return wrapper

    def add_product(self, product: Product):
        key = product.key_attributes()
        existing_product = self.products.get(key)

        if existing_product:
            raise ValueError("Product already exists; to update price or quantity, use the `update_product` function.")
        else:
            self.products[key] = product

    @check_product_existence
    def remove_product(self, product: Product):
        key = product.key_attributes()
        self.products.pop(key)

    @check_product_existence
    def update_product(self, product: Product, new_attributes: dict):
        old_key = product.key_attributes()
        existing_product = self.products.get(old_key)

        for attr, value in new_attributes.items():
            setattr(existing_product, attr, value)

        del self.products[old_key]

        new_key = existing_product.key_attributes()

        another_existing_product = self.products.get(new_key)
        if another_existing_product:
            another_existing_product.quantity += existing_product.quantity
            another_existing_product.price = existing_product.price
        else:
            self.products[new_key] = existing_product

    @check_product_existence
    def check_quantity(self, product: Product) -> int:
        key = product.key_attributes()
        return self.products.get(key).quantity

    def search_products(self, query: str) -> List[Product]:
        return [
            product for product in self.products.values()
            if any(query.lower() in str(getattr(product, attr)).lower() for attr in vars(product))
        ]

    def get_products_by_category(self, category: str) -> List[Product]:
        return [product for product in self.products.values() if product.category == category]
