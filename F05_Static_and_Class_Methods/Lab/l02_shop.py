class Shop:
    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity <= sum(self.items.values()):
            return "Not enough capacity in the shop"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    @staticmethod
    def can_remove_item_value(items, name, value):
        return name in items and items[name] >= value

    def remove_item(self, item_name, amount):
        if not self.can_remove_item_value(self.items, item_name, amount):
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            self.items.pop(item_name)
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)
