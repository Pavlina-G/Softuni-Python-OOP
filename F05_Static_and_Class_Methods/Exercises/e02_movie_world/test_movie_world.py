from customer import Customer
from dvd import DVD
from movie_world import MovieWorld

# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)

movie_world = MovieWorld("Test")
d = DVD("A", 1, 1254, "February", 10)
c = Customer("Pesho", 20, 4)
movie_world.add_customer(c)
movie_world.add_dvd(d)
movie_world.rent_dvd(4, 1)
print(repr(movie_world))
print(repr(movie_world).strip('\n'))
expected = "4: Pesho of age 20 has 1 rented DVD's (A)\n1: A (February 1254) has age restriction 10. Status: rented"

