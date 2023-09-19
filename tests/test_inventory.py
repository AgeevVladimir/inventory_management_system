import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.inventory.inventory import Inventory
from app.model.product_models import ElectronicProduct, BookProduct
from app.utils.serializer import serialize_inventory, deserialize_inventory


def test_add_product():
    inventory = Inventory()
    product = (ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                 price=800, quantity=10))
    inventory.add_product(product)
    assert inventory.check_quantity(product) == 10


def test_add_existing_product_raises_exception():
    inventory = Inventory()
    product = ElectronicProduct(subcategory="Laptop", brand="Dell", model="XPS 13", warranty_period=24, price=800,
                                quantity=10)
    inventory.add_product(product)

    with pytest.raises(Exception) as e_info:
        inventory.add_product(product)
    assert str(
        e_info.value) == "Product already exists; to update price or quantity, use the `update_product` function."


def test_remove_product():
    inventory = Inventory()
    product = (ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                 price=800, quantity=10))
    inventory.add_product(product)
    inventory.remove_product(product)
    with pytest.raises(Exception) as e_info:
        inventory.check_quantity(product)
    assert str(e_info.value) == "Trying to operate on a model that doesn't exist"


def test_remove_product_that_doesnt_exist():
    inventory = Inventory()
    product = (ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                 price=800, quantity=10))

    with pytest.raises(Exception) as e_info:
        inventory.remove_product(product)
    assert str(e_info.value) == "Trying to operate on a model that doesn't exist"


def test_update_product():
    inventory = Inventory()
    product = (ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                 price=800, quantity=10))
    inventory.add_product(product)
    key = product.key_attributes()
    inventory.update_product(product, {"price": 900})
    assert inventory.products.get(key).price == 900


def test_update_product_calculating_price_and_quantity():
    inventory = Inventory()
    product = (ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                 price=800, quantity=10))
    product_2 = (ElectronicProduct(subcategory="TestProduct", brand="Lenovo", model="XPS 13", warranty_period=24,
                                   price=1000, quantity=50))
    inventory.add_product(product)
    inventory.add_product(product_2)
    key = product.key_attributes()
    inventory.update_product(product_2, {"brand": "Dell"})
    assert inventory.products.get(key).price == 1000
    assert inventory.products.get(key).quantity == 60


def test_update_product_that_doesnt_exist():
    inventory = Inventory()
    product = (ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                 price=800, quantity=10))
    with pytest.raises(Exception) as e_info:
        inventory.update_product(product, {"price": 900})
    assert str(e_info.value) == "Trying to operate on a model that doesn't exist"


def test_serialize_deserialize():
    inventory = Inventory()
    product = (ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                 price=800, quantity=10))
    inventory.add_product(product)

    filename = "test_inventory_data.json"
    serialize_inventory(inventory, filename)
    new_inventory = deserialize_inventory(filename)

    key = product.key_attributes()

    assert new_inventory.check_quantity(product) == 10
    assert new_inventory.products.get(key).brand == "Dell"


def test_deserialize_negative():
    filename = "test_unknown_inventory_data.json"
    with pytest.raises(ValueError) as excinfo:
        deserialize_inventory(filename)
    assert "Unknown product_type: Vehicle" in str(excinfo.value)


def test_search_products():
    inventory = Inventory()
    inventory.add_product(ElectronicProduct(subcategory="TestProduct", brand="Dell", model="XPS 13", warranty_period=24,
                                            price=800, quantity=10))
    inventory.add_product(BookProduct(subcategory="Nonfiction", title="Reinventing Organizations", price=120,
                                      quantity=7, author="Frederic Lalu", publisher="Dell", ISBN="1223-456-zd4"))
    search_result = inventory.search_products("Dell")

    assert len(search_result) == 2
