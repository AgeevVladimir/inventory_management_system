from inventory import Inventory
from product import Product, ElectronicProduct, BookProduct, ClothingProduct
from serializer import serialize_inventory, deserialize_inventory

if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_product(ElectronicProduct(name="Laptop", price=800, quantity=10,
                                            brand="Dell", model="XPS 13", warranty_period=24))
    inventory.add_product(BookProduct(name="Python Cookbook", price=40, quantity=30,
                                      author="David Beazley", publisher="O'Reilly", ISBN="978-1449340377"))
    inventory.add_product(ClothingProduct(name="T-shirt", price=15, quantity=50,
                                          material="Cotton", size="L", color="Red"))

    serialize_inventory(inventory, "inventory_data.json")
    new_inventory = deserialize_inventory("inventory_data.json")

    new_inventory.add_product(ElectronicProduct(name="Tablet", price=400, quantity=20,
                                                brand="Samsung", model="Galaxy Tab S7", warranty_period=12))
    new_inventory.update_product("Laptop", {"price": 900})
    new_inventory.remove_product("T-shirt")

    search_result = new_inventory.search_products("Dell")
    for product in search_result:
        print(product)

    print("Quantity of 'Laptop' after operations:", new_inventory.check_quantity("Laptop"))
