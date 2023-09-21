from typing import List

from sqlalchemy import or_

from app.database.database import Session  # Импортируйте Session из вашего файла database.py
from app.database.model import Product, ClothingProduct, BookProduct, ElectronicProduct  # Ваш импорт модели продукта


class Inventory:
    def __init__(self):
        self.session = Session()

    def add_product(self, product: Product):
        with Session() as session:
            session.add(product)
            session.commit()

    def remove_product(self, product_id: int):
        with Session() as session:
            existing_product = session.query(Product).filter_by(id=product_id).first()
        if not existing_product:
            raise ValueError("Product does not exist")
        session.delete(existing_product)
        session.commit()

    def update_product(self, product_id: int, new_attributes: dict):
        with Session() as session:
            existing_product = session.query(Product).filter_by(id=product_id).first()
            if not existing_product:
                raise ValueError("Product does not exist")
            for attr, value in new_attributes.items():
                setattr(existing_product, attr, value)
            session.commit()

    def check_quantity(self, product: Product) -> int:
        existing_product = self.session.query(Product).filter_by(id=product.id).first()
        if not existing_product:
            raise ValueError("Product does not exist")

        return existing_product.quantity

    def search_products(self, query: str) -> List[Product]:
        return self.session.query(Product).join(
            ElectronicProduct, BookProduct, ClothingProduct, isouter=True
        ).filter(
            or_(
                Product.type.ilike(f"%{query}%"),
                Product.category.ilike(f"%{query}%"),
                Product.subcategory.ilike(f"%{query}%"),

                ElectronicProduct.brand.ilike(f"%{query}%"),
                ElectronicProduct.model.ilike(f"%{query}%"),
                ElectronicProduct.warranty_period.ilike(f"%{query}%"),

                BookProduct.title.ilike(f"%{query}%"),
                BookProduct.author.ilike(f"%{query}%"),
                BookProduct.publisher.ilike(f"%{query}%"),
                BookProduct.ISBN.ilike(f"%{query}%"),

                ClothingProduct.material.ilike(f"%{query}%"),
                ClothingProduct.size.ilike(f"%{query}%"),
                ClothingProduct.color.ilike(f"%{query}%")
            )
        ).all()

    def get_products_by_category(self, category: str) -> List[Product]:
        return self.session.query(Product).filter_by(category=category).all()
