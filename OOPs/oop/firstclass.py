# CLass is the blueprint while
# Instance is the object that is build from a class


class Owner:
    pet = "Gio"


class Dog:

    # Class Attribute
    species = "Canis familiaris"

    # The properties all dogs must have
    # Initial State
    def __init__(self, name=None, age=None, breed=None):
        self.name = name
        self.age = age
        self.breed = breed

    # For printing our object in a pythonic way
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # Inorder to not override the original function
        # We will still use super
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    def speak(self, sound="Woof"):

        return f"{self.name} says {sound}"


class Bulldog(Dog):
    def speak(self, sound="Grrr"):
        return f"{self.name} says {sound}"


print(JackRussellTerrier("Mickey", 9))
print(JackRussellTerrier("Mickey", 9).species)
print(JackRussellTerrier("Mickey", 9).species)

