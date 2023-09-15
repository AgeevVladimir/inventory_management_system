from typing import Dict, Union

from product import Product, ElectronicProduct, BookProduct, ClothingProduct


class Inventory:
    def __init__(self):
        self.products: Dict[str, Union[Product, ElectronicProduct, BookProduct, ClothingProduct]] = {}

    def add_product(self, product: Union[Product, ElectronicProduct, BookProduct, ClothingProduct]):
        if product.name not in self.products:
            self.products[product.name] = product
        else:
            self.products[product.name].quantity += product.quantity

    def remove_product(self, product_name: str):
        if product_name in self.products:
            del self.products[product_name]

    def update_product(self, product_name: str, new_attributes: dict):
        if product_name in self.products:
            product = self.products[product_name]
            for attr, value in new_attributes.items():
                setattr(product, attr, value)

    def check_quantity(self, product_name: str):
        if product_name in self.products:
            return self.products[product_name].quantity
        else:
            return 0

    def search_products(self, query: str):
        result = []
        for product in self.products.values():
            if any(query.lower() in str(getattr(product, attr)).lower() for attr in product.__dict__):
                result.append(product)
        return result
