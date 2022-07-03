from F02_Classes_and_Objects.Exercises.project_guild_system.guild import Guild
from F02_Classes_and_Objects.Exercises.project_guild_system.player import Player

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
