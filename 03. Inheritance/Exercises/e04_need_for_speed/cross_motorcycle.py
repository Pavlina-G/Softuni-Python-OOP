from F03_Inheritance.Exercises.e04_need_for_speed.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)