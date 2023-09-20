import pytest

from app.inventory.inventory import Inventory
from app.utils.serializer import serialize_inventory, deserialize_inventory


def test_add_product(electronic_product):
    inventory = Inventory()
    inventory.add_product(electronic_product)
    assert inventory.check_quantity(electronic_product) == 10


def test_add_existing_product_raises_exception(electronic_product):
    inventory = Inventory()
    inventory.add_product(electronic_product)

    with pytest.raises(Exception) as e_info:
        inventory.add_product(electronic_product)
    assert str(
        e_info.value) == "Product already exists; to update price or quantity, use the `update_product` function."


def test_remove_product(electronic_product):
    inventory = Inventory()
    inventory.add_product(electronic_product)
    inventory.remove_product(electronic_product)
    with pytest.raises(Exception) as e_info:
        inventory.check_quantity(electronic_product)
    assert str(e_info.value) == "Trying to operate on a product that doesn't exist"


def test_remove_product_that_doesnt_exist(electronic_product):
    inventory = Inventory()
    with pytest.raises(Exception) as e_info:
        inventory.remove_product(electronic_product)
    assert str(e_info.value) == "Trying to operate on a product that doesn't exist"


def test_update_product(electronic_product):
    inventory = Inventory()
    inventory.add_product(electronic_product)
    key = electronic_product.key_attributes()
    inventory.update_product(electronic_product, {"price": 900})
    assert inventory.products.get(key).price == 900


def test_update_product_calculating_price_and_quantity(electronic_product, another_electronic_product):
    inventory = Inventory()
    inventory.add_product(electronic_product)
    inventory.add_product(another_electronic_product)
    key = electronic_product.key_attributes()
    inventory.update_product(another_electronic_product, {"brand": "Dell"})
    assert inventory.products.get(key).price == 1000
    assert inventory.products.get(key).quantity == 60


def test_update_product_that_doesnt_exist(electronic_product):
    inventory = Inventory()
    with pytest.raises(Exception) as e_info:
        inventory.update_product(electronic_product, {"price": 900})
    assert str(e_info.value) == "Trying to operate on a product that doesn't exist"


def test_serialize_deserialize(electronic_product):
    inventory = Inventory()
    inventory.add_product(electronic_product)

    filename = "tests/test_inventory_data.json"
    serialize_inventory(inventory, filename)
    new_inventory = deserialize_inventory(filename)

    key = electronic_product.key_attributes()

    assert new_inventory.check_quantity(electronic_product) == 10
    assert new_inventory.products.get(key).brand == "Dell"


def test_deserialize_negative():
    filename = "tests/test_unknown_inventory_data.json"
    with pytest.raises(ValueError) as excinfo:
        deserialize_inventory(filename)
    assert "Unknown product_type: Vehicle" in str(excinfo.value)


def test_search_products(book_product, electronic_product):
    inventory = Inventory()
    inventory.add_product(book_product)
    inventory.add_product(electronic_product)
    search_result = inventory.search_products("Dell")

    assert len(search_result) == 2


def test_get_products_by_category(book_product, electronic_product, another_electronic_product):
    inventory = Inventory()
    inventory.add_product(book_product)
    inventory.add_product(electronic_product)
    inventory.add_product(another_electronic_product)

    electronic_products = inventory.get_products_by_category("Electronics")
    assert len(electronic_products) == 2

    book_products = inventory.get_products_by_category("Books")
    assert len(book_products) == 1
    assert book_products[0].title == "Reinventing Organizations"

    clothing_products = inventory.get_products_by_category("Clothing")
    assert len(clothing_products) == 0

    # Проверка на несуществующую категорию
    assert inventory.get_products_by_category("NonExistent") == []
