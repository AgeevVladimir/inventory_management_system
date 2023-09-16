from inventory import Inventory
from product import ElectronicProduct, BookProduct, ClothingProduct
from serializer import serialize_inventory, deserialize_inventory

if __name__ == "__main__":

    # Create products and add to inventory
    inventory = Inventory()
    inventory.add_product(ElectronicProduct(subcategory="Laptop", brand="Dell", model="XPS 13", warranty_period=24,
                                            price=800, quantity=10))
    inventory.add_product(ElectronicProduct(subcategory="Laptop", brand="Dell", model="XPS 15", warranty_period=24,
                                            price=1000, quantity=10))
    inventory.add_product(BookProduct(subcategory="Nonfiction", title="Python Cookbook", author="David Beazley",
                                      publisher="O'Reilly", ISBN="978-1449340377", price=40, quantity=30))
    inventory.add_product(ClothingProduct(subcategory="T-shirt", material="Cotton", size="L", color="Red",
                                          price=15, quantity=50))

    # Print inventory
    for product_name, product_object in inventory.products.items():
        print(f"{product_object}")
    print("\n")

    # Serialize inventory to json
    serialize_inventory(inventory, "resources/inventory_data.json")

    # Deserialize json to new inventory
    new_inventory = deserialize_inventory("resources/inventory_data.json")

    # Remove product using key attributes
    new_inventory.remove_product(ClothingProduct(subcategory="T-shirt", material="Cotton", size="L", color="Red"))

    # update attributes for product in new inventory
    new_inventory.update_product(ElectronicProduct(subcategory="Laptop", brand="Dell", model="XPS 13",
                                                   warranty_period=24), {"brand": "Macbook", "model": "air"})

    # update attributes for product in new inventory
    new_inventory.update_product(ElectronicProduct(subcategory="Laptop", brand="Macbook", model="air",
                                                   warranty_period=24), {"price": 0})

    # Print new inventory
    for product_name, product_object in new_inventory.products.items():
        print(f"{product_object}")
    print("\n")

    # search something in new inventory
    search_result = new_inventory.search_products("Dell")
    for product in search_result:
        print(product)
    print("\n")

    # check quantity of a product in new inventory using key attributes
    quantity_checked_product = (ElectronicProduct(subcategory="Laptop", brand="Macbook", model="air",
                                                  warranty_period=24))
    print(f"Quantity of "
          f"{quantity_checked_product.key_attributes()}: {new_inventory.check_quantity(quantity_checked_product)}")
