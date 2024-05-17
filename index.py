from swimming import Fish, Dolphin, Shark, Octopus, Seahorse
from walking import Llama, Dog, Cat, Rabbit, Goat
from slithering import Snake, Frog, Turtle, Salamander, Newt



# Instances for animals that walk (petting zoo animals)
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "llama chow")
spot = Dog("Spot", "canine", "midday", "dog chow")
whiskers = Cat("Whiskers", "feline", "afternoon", "cat chow")
bunny = Rabbit("Bunny", "lagomorph", "morning", "rabbit chow")
billy = Goat("Billy", "caprine", "midday", "goat chow")

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
print(spot)
print(f'{spot.name} the {spot.species} is available to pet during the {spot.shift} shift.')
print(spot.feed())
