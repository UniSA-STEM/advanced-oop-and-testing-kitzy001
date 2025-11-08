""""
File: animal.py
Description: This file contains the Animal class and relevant subclasses.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
import random

class Animal(ABC):

    def __init__(self, name, species, age, id=None, diet=None, health=100, hunger=50):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__id = id
        self.__diet = diet
        self.__health = health
        self.__hunger = hunger

    def __str__(self):
        return(
            f"Name: {self.__name}\n"
            f"Age: {self.__age}\n"
            f"ID: {self.__id if self.__id is not None else "Not registered yet"}\n"
            f"Diet: {self.__diet if self.__diet is not None else "Not yet set"}\n"
            f"Health status: {self.__health} ({self.get_health_string()})\n"
        )

    def get_name(self):
        return self.__name

    def set_id(self, new_id):
        if isinstance(new_id, str):
            self.__id = new_id

    def get_health(self):
        return self.__health

    def set_health(self, health):
        if isinstance(health, int) or isinstance(health, float):
            self.__health += health

    def get_health_string(self):
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
        return health

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_diet(self):
        return self.__diet

    def set_diet(self, diet):
        if isinstance(diet, str):
            self.__diet = diet
        else:
            raise TypeError("Diet must be a string")

    @abstractmethod
    def cry(self):
        pass

    def eat(self, quantity):
        if self.__diet is not None:
            print(f"Eating {quantity} {self.__diet}...")
        else:
            print(f"No food assigned to {self.__name}...")


class Mammal(Animal):
    def __init__(self, name, species, age, id, diet, health, hunger):
        Animal.__init__(self, name, species, age, id, diet, health, hunger)

    def cry(self):
        print("Mammal crying...")


class Reptile(Animal):
    def __init__(self, name, species, age, diet=None, health=100, hunger=50, egg_count=0):
        Animal.__init__(self, name, species, age, diet, health, hunger)
        self.__egg_count = egg_count

    def cry(self):
        print("Hisssss...")

class MarineAnimal(Animal):
    def __init__(self, name, species, age, diet=None, health=100, hunger=50):
        Animal.__init__(self, name, species, age, diet=diet, health=health, hunger=hunger)

    def cry(self):
        print("Underwater noises....")


class BigCat(Mammal):
    def __init__(self, name, species, age, id=None, diet=None, health=100, hunger=50, strength=25):
        Mammal.__init__(self, name, species, age, id=id, diet=diet, health=health, hunger=hunger)
        self.__strength = strength
        self.__animals_attacked = [] # Save animals as an object to this set.
        self.__violence_rating = len(self.get_animals_attacked())

    def get_violence_rating(self):
        return self.__violence_rating

    def get_animals_attacked(self):
        return self.__animals_attacked

    def cry(self):
        print("Roar!!!")

    def attack(self, opponent):
        if isinstance(opponent, BigCat): # Add condition for if they are in the same enclosure?
            self_damage = opponent.get_damage()
            self.set_health(self_damage)
            opponent_damage = self.get_damage()
            opponent.set_health(opponent_damage)
            self.__animals_attacked.append(opponent)
            print(self.__animals_attacked)
        else:
            print(f"{self.get_name()} cannot attack {opponent.get_name()} as they are a {opponent.get_species()}.")

    def get_damage(self):
        roll = random.random()
        damage = round((self.__strength * roll), 0)
        return - damage

class Monkey(Mammal):
    def __init__(self, name, species, age, diet=None, health=100, hunger=50):
        Mammal.__init__(self, name, species, age, diet=diet, health=health, hunger=hunger)

    def cry(self):
        print("Give orange me give eat orange me eat orange give me eat orange give me you.")


