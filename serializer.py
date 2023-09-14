import json

from inventory import Inventory
from product import Product, ElectronicProduct, BookProduct, ClothingProduct


def serialize_inventory(inventory, filename):
    with open(filename, 'w') as file:
        json.dump([vars(product) for product in inventory.products.values()], file, indent=4)


def deserialize_inventory(filename):
    new_inventory = Inventory()
    with open(filename, 'r') as file:
        data = json.load(file)
        for item in data:
            product = Product(item['name'], item['price'], item['quantity'])

            if 'brand' in item:  # Determine product category by checking attributes
                product = ElectronicProduct(item['name'], item['price'], item['quantity'],
                                            item['brand'], item['model'], item['warranty_period'])
            elif 'author' in item:
                product = BookProduct(item['name'], item['price'], item['quantity'],
                                      item['author'], item['publisher'], item['ISBN'])
            elif 'material' in item:
                product = ClothingProduct(item['name'], item['price'], item['quantity'],
                                          item['material'], item['size'], item['color'])

            new_inventory.add_product(product)

    return new_inventory
