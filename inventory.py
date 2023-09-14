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
