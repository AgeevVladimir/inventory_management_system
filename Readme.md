### Simple Inventory Management Prototype

This prototype offers basic functionality for managing an inventory of products. 
It currently handles a few types of products (Electronics, Books, and Clothing) and provides simple CRUD operations for them.
Features and Instructions are below

##### 1. Product Management
Supports different product categories: Electronics, Books, and Clothing.
Each product category has its own unique set of attributes.
##### 2. Basic Operations
- Add products to the inventory.
- Remove products.
- Update product attributes.
- Basic search functionality across product attributes.
- List products by their categories.
- Save the current inventory state to a JSON file.
- Load an inventory from a saved JSON file.

##### 3. Limitations and further enhancements

The current version is a prototype and may not be suitable for large-scale or production use.
Here is a list of planned enhancements:

- Transition from file-based serialization to a robust database system for storing inventory.
- Implement versioning for the data format to ensure compatibility between different versions of the software.
- Migrate the current system to Django to leverage its ORM, and introduce an admin panel for easier inventory management.

##### 4. Getting Started

To run the project follow instructions:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn main:app --reload
```

You can also run project in docker:
```
docker build -t inventory_app .
docker run -p 8080:8080 inventory_app

```

To run tests and check coverage:
```
pytests
coverage run -m pytest
coverage report -m  
```

Documentation:

[Standard FastAPI Documentation](http://127.0.0.1:8000/docs)
