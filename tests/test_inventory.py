import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from inventory import Inventory
from product import Product, ElectronicProduct, BookProduct
from serializer import serialize_inventory, deserialize_inventory


def test_add_product():
    inventory = Inventory()
    product = Product(name="TestProduct", price=100.0, quantity=5)

    inventory.add_product(product)

    assert inventory.check_quantity("TestProduct") == 5


def test_remove_product():
    inventory = Inventory()
    product = Product(name="TestProduct", price=100.0, quantity=5)
    inventory.add_product(product)

    inventory.remove_product("TestProduct")

    assert inventory.check_quantity("TestProduct") == 0


def test_update_product():
    inventory = Inventory()
    product = ElectronicProduct(name="Laptop", price=1000, quantity=3, brand="BrandX", model="ModelY",
                                warranty_period=12)
    inventory.add_product(product)

    inventory.update_product("Laptop", {"price": 900})

    updated_product = inventory.products["Laptop"]
    assert updated_product.price == 900


def test_serialize_deserialize():
    inventory = Inventory()
    product = ElectronicProduct(name="Laptop", price=1000, quantity=3, brand="BrandX", model="ModelY",
                                warranty_period=12)
    inventory.add_product(product)

    filename = "test_inventory_data.json"
    serialize_inventory(inventory, filename)
    new_inventory = deserialize_inventory(filename)

    assert new_inventory.check_quantity("Laptop") == 3
    assert new_inventory.products["Laptop"].brand == "BrandX"


def test_search_products():
    inventory = Inventory()
    inventory.add_product(ElectronicProduct(name="Laptop", price=1000, quantity=3, brand="Dell", model="Model1",
                                            warranty_period=12))
    inventory.add_product(BookProduct(name="Nonfiction", price=120, quantity=7, author="Frederic Lalu",
                                      publisher="Dell", ISBN="1223-456-zd4"))
    search_result = inventory.search_products("Dell")

    assert len(search_result) == 2
