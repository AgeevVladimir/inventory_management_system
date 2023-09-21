import logging

from fastapi import HTTPException

from app.inventory.inventory import Inventory
from app.utils.config import *

logging.basicConfig(level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)

inventory = Inventory()


def handle_add_product(product, product_type):
    try:
        inventory.add_product(product)
        logger.info(f"{product_type} Product added: {product}")
        return {"message": "Product added", "product": product}
    except Exception as e:
        logger.error(f"Failed to add {product_type} model: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_remove_product(product_id: int, product_type: str):
    try:
        inventory.remove_product(product_id)
        logger.info(f"{product_type} Product removed with ID: {product_id}")
        return {"message": "Product removed", "product_id": product_id}
    except Exception as e:
        logger.error(f"Failed to remove {product_type} product: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_update_product(product_id: int, new_attributes: dict, product_type: str):
    try:
        inventory.update_product(product_id, new_attributes)
        logger.info(f"{product_type} Product updated with ID: {product_id}. Attributes: {new_attributes}")
        return {"message": f"{product_type} Product updated", "product_id": product_id, "attributes": new_attributes}
    except ValueError as e:
        logger.error(f"Failed to update {product_type} product: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Failed to update {product_type} product: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_get_products_by_category(category: str):
    known_categories = ["Electronics", "Books", "Clothing"]

    if category not in known_categories:
        raise HTTPException(status_code=404, detail=f"Category {category} not found")

    try:
        products_in_category = inventory.get_products_by_category(category)
        if products_in_category:
            return {"message": f"Products in category {category}", "products": products_in_category}
        else:
            return {"message": f"No products found in category {category}"}
    except Exception as e:
        logger.error(f"Failed to get products in category {category}: {e}")
        raise HTTPException(status_code=400, detail=str(e))


def handle_search_products(query: str):
    try:
        search_result = inventory.search_products(query)
        if search_result:
            return {"message": f"Products by word {query}", f"Products found": search_result}
        else:
            return {"message": f"No products by word {query} found"}
    except Exception as e:
        logger.error(f"Failed to get products: {e}")
        raise HTTPException(status_code=400, detail=str(e))
