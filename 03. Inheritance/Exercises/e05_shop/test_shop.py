from F03_Inheritance.Exercises.e05_shop.drink import Drink
from F03_Inheritance.Exercises.e05_shop.food import Food
from F03_Inheritance.Exercises.e05_shop.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)

