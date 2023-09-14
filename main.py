import json


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: ${self.price} - Quantity: {self.quantity}"


class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, brand, model, warranty_period):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.model = model
        self.warranty_period = warranty_period

    def __str__(self):
        return f"Electronic - {super().__str__()} - Brand: {self.brand} - Model: {self.model} - Warranty: {self.warranty_period} months"


class BookProduct(Product):
    def __init__(self, name, price, quantity, author, publisher, ISBN):
        super().__init__(name, price, quantity)
        self.author = author
        self.publisher = publisher
        self.ISBN = ISBN

    def __str__(self):
        return f"Book - {super().__str__()} - Author: {self.author} - Publisher: {self.publisher} - ISBN: {self.ISBN}"


class ClothingProduct(Product):
    def __init__(self, name, price, quantity, material, size, color):
        super().__init__(name, price, quantity)
        self.material = material
        self.size = size
        self.color = color

    def __str__(self):
        return f"Clothing - {super().__str__()} - Material: {self.material} - Size: {self.size} - Color: {self.color}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name not in self.products:
            self.products[product.name] = product
        else:
            self.products[product.name].quantity += product.quantity

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]

    def update_product(self, product_name, new_attributes):
        if product_name in self.products:
            product = self.products[product_name]
            for attr, value in new_attributes.items():
                setattr(product, attr, value)

    def check_quantity(self, product_name):
        if product_name in self.products:
            return self.products[product_name].quantity
        else:
            return 0

    def search_products(self, query):
        result = []
        for product in self.products.values():
            # Check if any attribute of the product contains the query string
            if any(query.lower() in str(getattr(product, attr)).lower() for attr in vars(product)):
                result.append(product)
        return result

    def serialize_inventory(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(product) for product in self.products.values()], file, indent=4)

    def deserialize_inventory(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                product = Product(item['name'], item['price'], item['quantity'])
                if 'brand' in item:  # Determine product category by checking attributes
                    product = ElectronicProduct(item['name'], item['price'], item['quantity'],
                                                item['brand'], item['model'], item['warranty_period'])
                elif 'author' in item:
                    product = BookProduct(item['name'], item['price'], item['quantity'],
                                          item['author'], item['publisher'], item['ISBN'])
                elif 'material' in item:
                    product = ClothingProduct(item['name'], item['price'], item['quantity'],
                                              item['material'], item['size'], item['color'])
                self.add_product(product)


# Create an example inventory
inventory = Inventory()
inventory.add_product(ElectronicProduct("Laptop", 800, 10, "Dell", "XPS 13", 24))
inventory.add_product(BookProduct("Python Cookbook", 40, 30, "David Beazley", "O'Reilly", "978-1449340377"))
inventory.add_product(ClothingProduct("T-shirt", 15, 50, "Cotton", "L", "Red"))

# Serialize and Deserialize
inventory.serialize_inventory("inventory_data.json")
new_inventory = Inventory()
new_inventory.deserialize_inventory("inventory_data.json")

# Simulate Inventory Operations
new_inventory.add_product(ElectronicProduct("Tablet", 400, 20, "Samsung", "Galaxy Tab S7", 12))
new_inventory.update_product("Laptop", {"price": 900})
new_inventory.remove_product("T-shirt")

# Search for products
search_result = new_inventory.search_products("Dell")
for product in search_result:
    print(product)

# Check product quantity
print("Quantity of 'Laptop' after operations:", new_inventory.check_quantity("Laptop"))
