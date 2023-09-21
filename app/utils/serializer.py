"""
Serialization Utility for Inventory System

This module provides utility functions to serialize and deserialize the inventory:
- `serialize_inventory`: Converts the current state of the inventory into a JSON format and writes to a file.
- `deserialize_inventory`: Reads the JSON data from a file and recreates the inventory state.

Serialization includes saving the type of each product so it can be properly deserialized later.
"""

import json

from app.inventory.inventory import Inventory
from app.model.product_models import Product, ElectronicProduct, BookProduct, ClothingProduct

class_lookup = {
    'Product': Product,
    'ElectronicProduct': ElectronicProduct,
    'BookProduct': BookProduct,
    'ClothingProduct': ClothingProduct
}


def serialize_inventory(inventory: Inventory, filename: str):
    with open(filename, 'w') as file:
        serialized_products = []
        for product in inventory.products.values():
            product_data = product.__dict__.copy()
            product_data['product_type'] = product.__class__.__name__
            serialized_products.append(product_data)
        json.dump(serialized_products, file, indent=4)


def deserialize_inventory(filename: str) -> Inventory:
    new_inventory = Inventory()
    with open(filename, 'r') as file:
        data = json.load(file)
        for item in data:
            product_type = item.pop('product_type', 'Product')
            if product_type in class_lookup:
                product = class_lookup[product_type](**item)
                new_inventory.add_product(product)
            else:
                raise ValueError(f"Unknown product_type: {product_type}")
    return new_inventory
