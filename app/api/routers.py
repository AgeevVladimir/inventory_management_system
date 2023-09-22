from fastapi import APIRouter, Body, Path

from app.model.product_models import ElectronicProduct, BookProduct, ClothingProduct
from app.utils.handlers import *

router = APIRouter()


@router.get("/get_products/{category}/", tags=["Products"])
async def get_products_by_category(category: str = Path(..., example="Electronics/Books/Clothing")):
    return handle_get_products_by_category(category)


@router.post("/search_products/", tags=["Products"])
async def search_products(query: str):
    return handle_search_products(query)


@router.post("/add_product/electronic/", tags=["Add Product"])
async def add_electronic_product(product: ElectronicProduct):
    return handle_add_product(product, "Electronic")


@router.post("/add_product/book/", tags=["Add Product"])
async def add_book_product(product: BookProduct):
    return handle_add_product(product, "Book")


@router.post("/add_product/clothes/", tags=["Add Product"])
async def add_clothing_product(product: ClothingProduct):
    return handle_add_product(product, "Clothing")


@router.put("/update_product/electronic/", tags=["Update Product"])
async def update_electronic_product(product: ElectronicProduct, new_attributes: dict = Body(...)):
    return handle_update_product(product, new_attributes, "Electronic")


@router.put("/update_product/book/", tags=["Update Product"])
async def update_book_product(product: BookProduct, new_attributes: dict = Body(...)):
    return handle_update_product(product, new_attributes, "Book")


@router.put("/update_product/clothes/", tags=["Update Product"])
async def update_clothing_product(product: ClothingProduct, new_attributes: dict = Body(...)):
    return handle_update_product(product, new_attributes, "Clothing")


@router.delete("/remove_product/electronic/", tags=["Remove Product"])
async def remove_electronic_product(product: ElectronicProduct):
    return handle_remove_product(product, "Electronic")


@router.delete("/remove_product/book/", tags=["Remove Product"])
async def remove_book_product(product: BookProduct):
    return handle_remove_product(product, "Book")


@router.delete("/remove_product/clothes/", tags=["Remove Product"])
async def remove_clothing_product(product: ClothingProduct):
    return handle_remove_product(product, "Clothing")
