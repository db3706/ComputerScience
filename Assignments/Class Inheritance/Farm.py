
class Animal:

    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def speed(self, sprint_speed):
        return f"{self.name} is {sprint_speed} at running"

    def diet(self, consumption):
        return f"{self.name}'s species are {consumption}s"

    def burger(self, taste):
        return f"{self.name}'s meat would make a {taste} burger patty"


class Dog(Animal):
    
    def speak(self, sound="Bark!"):
        # Call the function speak () from parent Animal class
        return super().speak(sound)

    def speed (self, sprint_speed="fast"):
        return super().speed(sprint_speed)

    def diet(self, consumption="omnivore"):
        return super().diet(consumption)



class Cow(Animal):
    
    def speak(self, sound="Moo!"):
        return super().speak(sound)

    def burger(self, taste="very tasty"):
        return super().burger(taste)

    def diet(self, consumption="herbivore"):
        return super().diet(consumption)

class Horse(Animal):
    
    def speak(self, sound="Neigh!"):
        return super().speak(sound)

    def speed(self, sprinting_speed="very fast"):
        return super().speed(sprinting_speed)

    def diet(self, consumption="herbivore"):
        return super().diet(consumption)

class Pig(Animal):

    def speak(self, sound="Oink!"):
        return super().speak(sound)

    def diet(self, consumption="omnivore"):
        return super().diet(consumption)


# Printing the properties of the animals

# Define a dog
dog = Dog("Doug","12","Golden")
# Print dog's age
print(f"{dog.name} is {dog.age} years old")
# Print the colour of the dog's coat
print(f"{dog.name} has a {dog.colour} coloured coat")
# Print the sound of the dog
print(dog.speak())
# Print the dog's running speed
print(dog.speed())
# Print the dog's diet type
print(dog.diet())

print("") # Provides space between each printed description
# Define a cow
cow = Cow("Bessie","6","Black and White")
print(f"{cow.name} is {cow.age} years old")
print(cow.speak())
# Print if the cow would make a good burger
print(cow.burger())
print(cow.diet())

print("")
# Define a horse
horse = Horse("Charlie","10","white")
print(f"{horse.name} is {horse.age} years old")
print(horse.speak())
print(horse.speed())
print(horse.diet())

print("")
# Define a pig
pig = Pig("Napoleon","11","dark brown")
print(f"{pig.name} is {pig.age} years old")
print(pig.speak())
# Print the pig's diet
print(pig.diet())