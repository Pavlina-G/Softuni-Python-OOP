from F03_Inheritance.Lab.l01_food.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date=None):
        super().__init__(expiration_date)
        self.name = name

