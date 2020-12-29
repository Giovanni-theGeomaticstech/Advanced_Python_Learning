# CLass is the blueprint while
# Instance is the object that is build from a class

class Owner:
    pet = "Gio"

class Dog:

    # Class Attribute
    species = "Canis familiaris9"

    # The properties all dogs must have
    # Initial State
    def __init__(self, name, age):
        self.name = name
        self.age = age


#
sample = Dog()
# print(sample.initial)