"""
Handlers for Product Management in Inventory System

This module provides handler functions to interact with the inventory, including:
- Adding a product (`handle_add_product`)
- Removing a product (`handle_remove_product`)
- Updating a product's attributes (`handle_update_product`)
- Fetching products by their category (`handle_get_products_by_category`)
- Searching for products based on a query (`handle_search_products`)

Each handler function typically interfaces with the inventory through serialization/deserialization,
logs the operation, and returns a message along with the relevant product details.
"""

import logging

from fastapi import HTTPException

from app.utils.config import *
from app.utils.serializer import serialize_inventory, deserialize_inventory

logging.basicConfig(level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)


def handle_add_product(product, product_type):
    try:
        inventory = deserialize_inventory(JSON_PATH)
        inventory.add_product(product)
        serialize_inventory(inventory, JSON_PATH)
        logger.info(f"{product_type} Product added: {product}")
        return {"message": "Product added", "product": product}
    except ValueError as e:
        logger.error(f"Failed to add {product_type} model: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_remove_product(product, product_type):
    try:
        inventory = deserialize_inventory(JSON_PATH)
        inventory.remove_product(product)
        serialize_inventory(inventory, JSON_PATH)
        logger.info(f"{product_type} Product removed: {product}")
        return {"message": "Product removed", "product": product}
    except ValueError as e:
        logger.error(f"Failed to remove {product_type} product: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_update_product(product, new_attributes: dict, product_type: str):
    inventory = deserialize_inventory(JSON_PATH)
    try:
        inventory.update_product(product, new_attributes)
        serialize_inventory(inventory, JSON_PATH)
        logger.info(f"{product_type} Product updated: {new_attributes}")
        return {"message": f"{product_type} Product updated", "product": new_attributes}
    except ValueError as e:
        logger.error(f"Failed to update {product_type} product: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Failed to update {product_type} product: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_get_products_by_category(category: str):
    inventory = deserialize_inventory(JSON_PATH)
    known_categories = ["Electronics", "Books", "Clothing"]

    if category not in known_categories:
        raise HTTPException(status_code=404, detail=f"Category {category} not found")

    try:
        products_in_category = inventory.get_products_by_category(category)
        if products_in_category:
            return {"message": f"Products in category {category}", "products": products_in_category}
        else:
            return {"message": f"No products found in category {category}"}
    except ValueError as e:
        logger.error(f"Failed to get products in category {category}: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_search_products(query: str):
    inventory = deserialize_inventory(JSON_PATH)

    try:
        search_result = inventory.search_products(query)
        if search_result:
            return {"message": f"Products by word {query}", f"Products found": search_result}
        else:
            return {"message": f"No products by word {query} found"}
    except ValueError as e:
        logger.error(f"Failed to get products: {e}")
        raise HTTPException(status_code=400, detail=str(e))
