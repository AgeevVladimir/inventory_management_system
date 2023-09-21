from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    category = Column(String)
    subcategory = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'products',
        'polymorphic_on': type
    }


class ElectronicProduct(Product):
    __tablename__ = 'electronic_products'

    id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    brand = Column(String)
    model = Column(String)
    warranty_period = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'electronic_products',
    }


class BookProduct(Product):
    __tablename__ = 'book_products'

    id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    ISBN = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'book_products',
    }


class ClothingProduct(Product):
    __tablename__ = 'clothing_products'

    id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    material = Column(String)
    size = Column(String)
    color = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'clothing_products',
    }
