from F03_Inheritance.Exercises.e03_players_and_monsters.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)
