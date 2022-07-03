class Player:
    default_guild = "Unaffiliated"

    def __init__(self, name, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_result = [f"==={key} - {value}" for key, value in self.skills.items()]
        return f"Name: {self.name}\n" + f"Guild: {self.guild}\n" + \
               f"HP: {self.hp}\n" + f"MP: {self.mp}\n" + \
               '\n'.join(skills_result)

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
