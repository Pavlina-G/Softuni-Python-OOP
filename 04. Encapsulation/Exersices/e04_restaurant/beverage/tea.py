from e04_restaurant import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)