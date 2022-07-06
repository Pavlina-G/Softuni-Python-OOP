from F03_Inheritance.Exercises.e02_zoo.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)