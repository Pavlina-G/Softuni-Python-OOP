from F03_Inheritance.Exercises.e03_players_and_monsters.hero import Hero


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


# elf = Elf("E", 4)
# print(elf)