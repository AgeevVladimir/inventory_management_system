import json

from inventory import Inventory
from product import Product, ElectronicProduct, BookProduct, ClothingProduct

class_lookup = {
    'Product': Product,
    'ElectronicProduct': ElectronicProduct,
    'BookProduct': BookProduct,
    'ClothingProduct': ClothingProduct
}


def serialize_inventory(inventory: Inventory, filename: str):
    """
    Serialize an Inventory object to a JSON file.
    """
    with open(filename, 'w') as file:
        serialized_products = []
        for product in inventory.products.values():
            product_data = product.__dict__.copy()
            product_data['product_type'] = product.__class__.__name__
            serialized_products.append(product_data)
        json.dump(serialized_products, file, indent=4)


def deserialize_inventory(filename: str) -> Inventory:
    """
    Deserialize an Inventory object from a JSON file.
    Raises ValueError If an unknown product_type is found in the JSON file.
    """
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
