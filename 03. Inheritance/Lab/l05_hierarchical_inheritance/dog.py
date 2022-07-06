from F03_Inheritance.Lab.l05_hierarchical_inheritance.animal import Animal


class Dog(Animal):
    def bark(self):
        return 'barking...'


# dog = Dog()
# print(dog.eat())
# print(dog.bark())