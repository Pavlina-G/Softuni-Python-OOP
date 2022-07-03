from F02_Classes_and_Objects.Exercises.project_spoopify.album import Album
from F02_Classes_and_Objects.Exercises.project_spoopify.song import Song
from F02_Classes_and_Objects.Exercises.project_spoopify.band import Band


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
