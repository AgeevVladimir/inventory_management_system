from inventory import Inventory
from product import ElectronicProduct, BookProduct, ClothingProduct
from serializer import serialize_inventory, deserialize_inventory

if __name__ == "__main__":
    # Create an example inventory
    inventory = Inventory()
    inventory.add_product(ElectronicProduct("Laptop", 800, 10, "Dell", "XPS 13", 24))
    inventory.add_product(BookProduct("Python Cookbook", 40, 30, "David Beazley", "O'Reilly", "978-1449340377"))
    inventory.add_product(ClothingProduct("T-shirt", 15, 50, "Cotton", "L", "Red"))

    # Serialize and Deserialize
    serialize_inventory(inventory, "inventory_data.json")
    new_inventory = deserialize_inventory("inventory_data.json")

    # Simulate Inventory Operations
    new_inventory.add_product(ElectronicProduct("Tablet", 400, 20, "Samsung", "Galaxy Tab S7", 12))
    new_inventory.update_product("Laptop", {"price": 900})
    new_inventory.remove_product("T-shirt")

    # Search for products
    search_result = new_inventory.search_products("Dell")
    for product in search_result:
        print(product)

    # Check product quantity
    print("Quantity of 'Laptop' after operations:", new_inventory.check_quantity("Laptop"))
