# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Dog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Cat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Rabbit:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Goat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Turtle:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Salamander:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Newt:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Dolphin:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Shark:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Octopus:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Seahorse:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()




# Instances for animals that walk (petting zoo animals)
miss_fuzz = Llama("Miss Fuzz", "domestic llama")
spot = Dog("Spot", "canine")
whiskers = Cat("Whiskers", "feline")
bunny = Rabbit("Bunny", "lagomorph")
billy = Goat("Billy", "caprine")

# Instances for animals that slither (pond animals)
slippy = Snake("Slippy", "serpentine")
hoppy = Frog("Hoppy", "amphibian")
shelly = Turtle("Shelly", "reptile")
sammy = Salamander("Sammy", "amphibian")
newtie = Newt("Newtie", "amphibian")

# Instances for animals that swim (tank animals)
nemo = Fish("Nemo", "fish")
flipper = Dolphin("Flipper", "mammal")
jaws = Shark("Jaws", "fish")
inky = Octopus("Inky", "cephalopod")
bubbles = Seahorse("Bubbles", "fish")


print(miss_fuzz)
print(nemo)
