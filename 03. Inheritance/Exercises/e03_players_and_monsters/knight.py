from F03_Inheritance.Exercises.e03_players_and_monsters.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)