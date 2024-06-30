"""OOP
    Object-oriented programming (OOP) in Python is a programming paradigm based on the concept of "objects",
    which can contain data and code: data in the form of fields (often known as attributes or properties),
    and code in the form of procedures (often known as methods).
"""

"""Defining a class
    A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have
"""

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
        
    # Another instance method
    def speak(self, sound = "Woof Woof"):
        return f"{self.name} says {sound}"

"""Creating an object
    An object is an instance of a class. When a class is instantiated,
    Python creates an object, which is an instance of that class.
"""

# Instantiate of Dog class
my_dog = Dog("Puppy", 5)

# Access the instance attributes
print(my_dog.age)
print(my_dog.name)

# Call our instance methods
print(my_dog.description())
print(my_dog.speak("box box!"))

# Inheritance
class Labrador(Dog):
    def run(self, speed):
        return f"{self.name} runs at {speed} km/h"
    
# Create a new Labrador object
my_labrador = Labrador("Max", 5)

# Use the new method
print(my_labrador.run(3))

# Use the inherited method
print(my_labrador.description())

# Polymorphism
class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def speak(self, sound="Meow"):
        return f"{self.name} says {sound}"

animals = [Dog("Buddy", 9), Cat("Whiskers", 3)]

for animal in animals:
    print(animal.speak())