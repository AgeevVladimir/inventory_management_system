from pydantic import BaseModel


class ProductBase(BaseModel):
    type: str
    category: str
    subcategory: str
    price: float
    quantity: int


class ElectronicProductBase(ProductBase):
    brand: str
    model: str
    warranty_period: int


class BookProductBase(ProductBase):
    title: str
    author: str
    publisher: str
    ISBN: str


class ClothingProductBase(ProductBase):
    material: str
    size: str
    color: str
