#OOP 4.1
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        distance_from_sun_to_earth = 147000000  # in kilometers
        return abs(self.distance_from_sun - distance_from_sun_to_earth)

#Testing Parent class
random_planet = Planet("random_planet", 148000000, "terrestrial")
print(random_planet.get_distance_to_earth())  # Output: 1000000
print()
print()

#OOP 4.2
#inheritance child class
class Mercury(Planet):
    def __init__(self, name, distance_from_sun, planet_type):
        super().__init__(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        days_in_mercury_year = 88 # Earth days
        print(f"A year on Mercury lasts {days_in_mercury_year} Earth days. Happy New Year!")

#Testing mercury class
mercury = Mercury("Mercury", 57000000, "terrestrial")
print(f"Planet name: {mercury.name}")
print(f"Distance from the Sun: {mercury.distance_from_sun} km")
print(f"Planet type: {mercury.planet_type}")
distance_to_earth = mercury.get_distance_to_earth()
print(f"Distance to Earth: {distance_to_earth} km")
mercury.happy_new_year()
print()
print()

#OOP 4.3
#Inheritance Jupiter class
class Jupiter(Planet):
    def __init__(self, name, distance_from_sun, planet_type, number_of_moons):
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        days_in_jupiter_year = 4383  # Earth days
        print(f"A year on Jupiter lasts {days_in_jupiter_year} Earth days. Happy New Year!")

#Testing Jupiter Class
jupiter = Jupiter("Jupiter", 779000000, "gas giant", 80)
print(f"Planet name: {jupiter.name}")
print(f"Distance from the Sun: {jupiter.distance_from_sun} km")
print(f"Planet type: {jupiter.planet_type}")
print(f"Number of moons: {jupiter.number_of_moons}")
distance_to_earth = jupiter.get_distance_to_earth()
print(f"Distance to Earth: {distance_to_earth} km")
jupiter.happy_new_year()
