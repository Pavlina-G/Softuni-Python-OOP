from F03_Inheritance.Exercises.e02_zoo.mammal import Mammal


class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)