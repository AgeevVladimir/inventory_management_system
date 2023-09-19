from fastapi import FastAPI, Body, Path
from product.models import ElectronicProduct, BookProduct, ClothingProduct
from utils.handlers import *

app = FastAPI()

@app.post("/add_product/electronic/", tags=["Add Product"])
async def add_electronic_product(product: ElectronicProduct):
    return handle_add_product(product, "Electronic")


@app.post("/add_product/book/", tags=["Add Product"])
async def add_book_product(product: BookProduct):
    return handle_add_product(product, "Book")


@app.post("/add_product/clothes/", tags=["Add Product"])
async def add_clothing_product(product: ClothingProduct):
    return handle_add_product(product, "Clothing")


@app.put("/update_product/electronic/", tags=["Update Product"])
async def update_electronic_product(product: ElectronicProduct, new_attributes: dict = Body(...)):
    return handle_update_product(product, new_attributes, "Electronic")


@app.put("/update_product/book/", tags=["Update Product"])
async def update_book_product(product: BookProduct, new_attributes: dict = Body(...)):
    return handle_update_product(product, new_attributes, "Book")


@app.put("/update_product/clothes/", tags=["Update Product"])
async def update_clothing_product(product: ClothingProduct, new_attributes: dict = Body(...)):
    return handle_update_product(product, new_attributes, "Clothing")


@app.get("/get_products/{category}/", tags=["Products"])
async def get_products_by_category(category: str = Path(..., example="Electronics/Books/Clothing")):
    return handle_get_products_by_category(category)
