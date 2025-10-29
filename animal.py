'''
File: animal.py
Description: A brief description of this Python module.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:

    def __init__(self, name, species, age, dietary_needs, health=100, hunger=50):
        self.__name = name
        self.__age = age
        self.__species = species
        self.__dietary_needs = dietary_needs
        self.__health = health
        self.__hunger = hunger

    def __str__(self):
        if self.get_health() >= 95:
            health = "excellent"
        elif self.get_health() >= 75:
            health = "healthy"
        elif self.get_health() >= 50:
            health = "average"
        elif self.get_health() >= 30:
            health = "not great"
        elif self.get_health() < 30:
            health = "critical"

        return(
            f"Name: {self.__name}\n"
            f"Age: {self.__age}\n"
            f"Dietary needs: {self.__dietary_needs}\n"
            f"Health status: {self.__health} ({health})\n"
        )

    def get_health(self):
        return self.__health

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def cry(self):
        print("Rawr!")

    def eat(self, quantity):
        print(f"{self.__name} eats {quantity} units of slop.")


class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs, health, hunger):
        super().__init__(self, name, species, age, dietary_needs, health, hunger)


class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs, health, hunger, egg_count):
        super().__init__(self, name, species, age, dietary_needs, health, hunger)
        self.__egg_count = egg_count

class MarineAnimal(Animal):
    def __init__(self, name, species, age, dietary_needs, health=100, hunger=50):
        super().__init__(self, name, species, age, dietary_needs, health, hunger)


class BigCat(Mammal):
    def __init__(self, name, species, age, dietary_needs, health, hunger, animals_attacked):
        Mammal.__init__(self, name, species, age, dietary_needs, health, hunger)
        self.__animals_attacked = set() # Save animals as an object to this set.
        self.__violence_rating = count(self.__animals_attacked)

class Monkey(Mammal):
    def __init__(self, name, species, age, dietary_needs, health, hunger):
        Mammal.__init__(self, name, species, age, dietary_needs, health, hunger)


animal = Animal("Tony", "Tiger", 12, "Carnivore")
print(animal)
animal.cry()
animal.eat(50)