from F03_Inheritance.Exercises.e05_shop.product import Product


class Food(Product):
    DEFAULT_QUANTITY = 15  # DEFAULT_QUANTITY is an attribute of the Product class

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_QUANTITY)