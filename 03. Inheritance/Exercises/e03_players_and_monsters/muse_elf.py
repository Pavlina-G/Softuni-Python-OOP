from F03_Inheritance.Exercises.e03_players_and_monsters.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)

