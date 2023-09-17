from typing import Dict, List

from product import Product


class Inventory:
    def __init__(self):
        self.products: Dict[tuple, Product] = {}

    def add_product(self, product: Product):

        # Получаем старый ключ для поиска существующего продукта
        key = product.key_attributes()
        existing_product = self.products.get(key)

        if existing_product:
            raise Exception("Product is already exist, to update price or quantity use function update_product")
        else:
            self.products[key] = product

    def remove_product(self, product: Product):
        key = product.key_attributes()
        existing_product = self.products.get(key)

        if not existing_product:
            raise Exception("Trying to remove a product that doesn't exist")

        self.products.pop(key, None)

    def update_product(self, product: Product, new_attributes: dict):
        # Получаем старый ключ для поиска существующего продукта
        old_key = product.key_attributes()
        existing_product = self.products.get(old_key)

        if not existing_product:
            raise Exception("Trying to update a product that doesn't exist")

        # Обновляем атрибуты продукта
        for attr, value in new_attributes.items():
            setattr(existing_product, attr, value)

        # Удаляем старую запись из инвентаря
        del self.products[old_key]

        # Получаем новый ключ после обновления
        new_key = existing_product.key_attributes()

        # Объединяем продукты с одинаковыми ключевыми атрибутами, если таковые имеются
        another_existing_product = self.products.get(new_key)
        if another_existing_product:
            another_existing_product.quantity += existing_product.quantity
            another_existing_product.price = existing_product.price  # или какая-то другая логика для обновления цены
        else:
            # Добавляем обновленную запись в инвентарь
            self.products[new_key] = existing_product

    def check_quantity(self, product: Product) -> int:
        # Получаем старый ключ для поиска существующего продукта
        key = product.key_attributes()
        existing_product = self.products.get(key)

        if not existing_product:
            raise Exception("Trying to find a product that doesn't exist")

        return self.products.get(key).quantity

    def search_products(self, query: str) -> List[Product]:
        result = []
        for product in self.products.values():
            if any(query.lower() in str(getattr(product, attr)).lower() for attr in vars(product)):
                result.append(product)
        return result
