class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
