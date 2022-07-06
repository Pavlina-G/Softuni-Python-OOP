from F03_Inheritance.Exercises.e05_shop.product import Product


class Drink(Product):
    DEFAULT_QUANTITY = 10 # DEFAULT_QUANTITY is an attribute of the Product class

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_QUANTITY)

    # DEFAULT_QUANTITY = 10
    # def __init__(self, name: str):
    #     super().__init__(name, self.DEFAULT_QUANTITY) DEFAULT_QUANTITY is an attribute of the Drink class

    # def __init__(self, name: str):
    #     super().__init__(name, 10)