from F03_Inheritance.Exercises.e05_shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self,product_name: str):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)


    def __repr__(self):
        products_info = ''
        for product in self.products:
            products_info += f"{product.name}: {product.quantity}\n"
        return products_info.strip()


