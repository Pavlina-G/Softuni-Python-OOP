from F03_Inheritance.Lab.l05_hierarchical_inheritance.animal import Animal


class Cat(Animal):
    def meow(self):
        return 'meowing...'


# cat = Cat()
# print(cat.eat())
# print(cat.meow())