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

    def __init__(self, name, species, age, id=None, diet=None):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__id = id
        self.__diet = diet
        self.__health = 100
        self.__hunger = 100
        self.__energy = 100
        self.__aggression = 0

    def __str__(self):
        return(
            f"Name: {self.__name}\n"
            f"Age: {self.__age}\n"
            f"ID: {self.__id if self.__id is not None else "Not registered yet"}\n"
            f"Diet: {self.__diet if self.__diet is not None else "Not yet set"}\n"
            f"Health status: {self.__health} ({self.get_health_string()})\n"
        )

    @property
    def name(self):
        return self.__name

    def set_name(self, name):    # Setter for animal name.
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be a string.")

    @property
    def id(self):
        return self.__id

    def set_id(self, new_id):    # Setter for animal ID, called when adding animal to registry
        if isinstance(new_id, str):
            self.__id = new_id

    @property
    def health(self):
        return self.__health

    def set_health(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__health = max(0, min(self.__health + value, 100))
        else:
            raise TypeError("Health must be numeric.")

    def get_health_string(self):
        if self.get_health() >= 95:
            health_str = "excellent"
        elif self.get_health() >= 75:
            health_str = "healthy"
        elif self.get_health() >= 50:
            health_str = "average"
        elif self.get_health() >= 30:
            health_str = "not great"
        elif self.get_health() < 30:
            health_str = "critical"
        return health_str

    def get_health(self):
        return self.__health

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_hunger(self):
        return self.__hunger

    def set_hunger(self, value):    # Takes an integer and updates the value for hunger.
        self.__hunger = max(0, min(self.__hunger + value, 100))    # Set to be minimum 0 or maximum 100 value.

    def set_diet(self, diet):
        if isinstance(diet, str):
            self.__diet = diet
        else:
            raise TypeError("Diet must be a string")

    def eat(self, quantity):
        if self.__diet is not None:
            print(f"Eating {quantity} {self.__diet}...\n")
        else:
            print(f"No diet set for {self.__name}. Please set a diet.\n")

    @abstractmethod
    def cry(self):
        pass

    def sleep(self):
        energy_increase = 20
        self.__energy = min(100, self.__energy + energy_increase) # Ensure value does not exceed 100.


class Mammal(Animal):
    def __init__(self, name, species, age, id, diet, health, hunger):
        super().__init__(name, species, age, id, diet, health, hunger)
        self.__habitat = None

    def get_habitat(self):
        return self.__habitat

    def set_habitat(self, habitat):
        if isinstance(habitat, str):
            self.__habitat = habitat
        else:
            raise TypeError("Habitat must be of type string.")

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
        self.__attack_count = len(self.get_animals_attacked())

    @property
    def attack_count(self):
        return self.__attack_count

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


