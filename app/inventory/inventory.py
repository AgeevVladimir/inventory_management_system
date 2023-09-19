from functools import wraps
from typing import Dict, List, Callable

from app.model.product_models import Product


class Inventory:
    """
    A class representing a collection of products in an inventory.
    """

    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.products: Dict[tuple, Product] = {}

    def check_product_existence(func: Callable) -> Callable:
        """
        Decorator that checks if a model exists in the inventory before proceeding to call the decorated function.
        """

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            product = args[0]
            key = product.key_attributes()
            existing_product = self.products.get(key)
            if not existing_product:
                raise ValueError("Trying to operate on a model that doesn't exist")
            return func(self, *args, **kwargs)

        return wrapper

    def add_product(self, product: Product):
        """
        Adds a model to the inventory.
        Raises an exception if the model already exists.
        """
        key = product.key_attributes()
        existing_product = self.products.get(key)

        if existing_product:
            raise Exception("Product already exists; to update price or quantity, use the `update_product` function.")
        else:
            self.products[key] = product

    @check_product_existence
    def remove_product(self, product: Product):
        """
        Removes a model from the inventory.
        """
        key = product.key_attributes()
        self.products.pop(key)

    @check_product_existence
    def update_product(self, product: Product, new_attributes: dict):
        """
        Updates the attributes of a model in the inventory.
        In case of duplicates after updates: summarizes two products.
        """
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
        """
        Returns the quantity of products.
        """
        key = product.key_attributes()
        return self.products.get(key).quantity

    def search_products(self, query: str) -> List[Product]:
        """
        Searches the inventory based on a query and returns a list of matching products.
        """
        result = []
        for product in self.products.values():
            if any(query.lower() in str(getattr(product, attr)).lower() for attr in vars(product)):
                result.append(product)
        return result

    def get_products_by_category(self, category: str) -> List[Product]:
        return [product for product in self.products.values() if product.category == category]
