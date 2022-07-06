from F03_Inheritance.Lab.l04_multilevel_inheritance.car import Car


class SportsCar(Car):
    def race(self):
        return 'racing...'


# sport_car = SportsCar()
# print(sport_car.race())
# print(sport_car.drive())
# print(sport_car.move())