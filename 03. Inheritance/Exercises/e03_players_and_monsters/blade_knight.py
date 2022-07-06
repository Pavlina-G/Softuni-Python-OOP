from F03_Inheritance.Exercises.e03_players_and_monsters.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)


# b = BladeKnight('B', 9)
# print(b)
# print(b.__class__.__bases__[0].__name__)