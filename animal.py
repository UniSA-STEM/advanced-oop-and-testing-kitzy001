""""
File: animal.py
Description: This file contains the Animal class and relevant subclasses.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
from enclosure import Enclosure
import random

class Animal(ABC):

    def __init__(self, name, species, age, diet=None):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__id = None
        self.__diet = diet
        self.__enclosure = None
        self.__health = 100
        self.__hunger = 100
        self.__energy = 100
        self.__aggression = 0
        self.__happiness = 50
        self.__is_sick = False


    def __str__(self):
        return(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"ID: {self.id if self.id is not None else "Not registered yet"}\n"
            f"Diet: {self.__diet if self.__diet is not None else "Not yet set"}\n"
            f"Health status: {self.health} ({self.check_health()})\n"
            f"Enclosure: {self.__enclosure}\n"
        )

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def respond_to_zookeeper(self):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def age(self):
        return self.__age

    @property
    def health(self):
        return self.__health

    @property
    def aggression(self):
        return self.__aggression

    @property
    def happiness(self):
        return self.__happiness

    @property
    def energy(self):
        return self.__energy

    @property
    def hunger(self):
        return self.__hunger

    @property
    def species(self):
        return self.__species

    @property
    def is_sick(self):
        return self.__is_sick

    @property
    def diet(self):
        return self.__diet

    def get_enclosure(self):
        return self.__enclosure

    def set_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            self.__enclosure = enclosure

    def set_id(self, new_id):    # Setter for animal ID, called when adding animal to registry.
        if isinstance(new_id, str):
            self.__id = new_id

    def check_health(self):    # Returns a string describing animal health.
        if self.health >= 95:
            health_str = "excellent"
        elif self.health >= 75:
            health_str = "healthy"
        elif self.health >= 50:
            health_str = "average"
        elif self.health >= 25:
            health_str = "unhealthy"
            self.__is_sick = True
        else:
            health_str = "critical"
            self.__is_sick = True
        return health_str

    def set_health(self, value):    # Takes an integer and updates the value for health.
        if isinstance(value, int):
            self.__health = max(0, min(self.__health + value, 100))    # Ensure value does not exceed 100.

    def set_hunger(self, value):    # Takes an integer and updates the value for hunger.
        if isinstance(value, int):
            self.__hunger = max(0, min(self.__hunger + value, 100))    # Ensure value does not exceed 100.

    def set_energy(self, value):    # Takes an integer and updates the value for energy.
        if isinstance(value, int):
            self.__energy = max(0, min(self.__energy + value, 100))    # Ensure value does not exceed 100.

    def set_happiness(self, value):    # Takes an integer and updates the value for happiness.
        if isinstance(value, int):
            self.__happiness = max(0, min(self.__happiness + value, 100))  # Ensure value is between 0-100.

    def set_aggression(self, value):    # Takes an integer and updates the value for aggression.
        if isinstance(value, int):
            self.__aggression = max(0, min(self.__aggression + value, 100))  # Ensure value is between 0-100.

    def set_diet(self, diet):
        if isinstance(diet, str):
            self.__diet = diet
        else:
            raise TypeError("Diet must be a string")

    def eat(self, quantity):
        if self.__diet is not None:
            print(f"Eating {quantity} {self.__diet}...\n")
            self.set_hunger(quantity)
        else:
            print(f"No diet set for {self.name}. Please set a diet.\n")

    def sleep(self):
        energy_increase = 50
        health_increase = 10
        self.set_energy(energy_increase)
        self.set_health(health_increase)

    def explore(self):
        energy_spent = -20
        happiness_gained = 20
        aggression_decrease = 20
        hunger_change = -20
        health_change = -15
        self.set_energy(energy_spent)
        self.set_happiness(happiness_gained)
        self.set_aggression(aggression_decrease)
        self.set_hunger(hunger_change)
        self.set_health(health_change)


class Mammal(Animal):
    def __init__(self, name, species, age, diet=None, habitat=None):
        super().__init__(name, species, age, diet)
        self.__habitat = habitat

    @property
    def habitat(self):
        return self.__habitat

    def set_habitat(self, habitat):
        if isinstance(habitat, str):
            self.__habitat = habitat
        else:
            raise TypeError("Habitat must be of type string.")

    def cry(self):
        print("Mammal noises...")

    def respond_to_zookeeper(self):
        if self.aggression == 0:
            happiness_gained = 20
        elif self.aggression <= 50:
            happiness_gained = 5
        else:
            happiness_gained = -20
        self.set_happiness(happiness_gained)


class Reptile(Animal):
    def __init__(self, name, species, age, diet=None):
        Animal.__init__(self, name, species, age, diet)
        self.__egg_count = 0

    def cry(self):
        print("Hiss...")

    def respond_to_zookeeper(self):
        if self.aggression == 0:
            happiness_gained = 50
        elif self.aggression <= 50:
            happiness_gained = 10
        else:
            happiness_gained = - 40
        self.set_happiness(happiness_gained)

    def lay_egg(self):
        self.__egg_count += 1

    def bathe_in_sun(self):
        happiness_gained = 20
        aggression_decrease = -20
        self.set_happiness(happiness_gained)
        self.set_aggression(aggression_decrease)

    def explore(self):
        super().explore()
        print(f"{self.name} explores their terrarium and finds a new hiding place!\n")


class MarineAnimal(Animal):
    def __init__(self, name, species, age, diet=None):
        Animal.__init__(self, name, species, age, diet)

    def cry(self):
        print("Underwater noises....")

    def respond_to_zookeeper(self):
        if self.aggression == 0:
            happiness_gained = 10
        elif self.aggression <= 50:
            happiness_gained = 0
        else:
            happiness_gained = -50
        self.set_happiness(happiness_gained)

    def swim_with_trainer(self):
        happiness_gained = 30
        energy_spent = -30
        self.set_happiness(happiness_gained)
        self.set_energy(energy_spent)

    def explore(self):
        super().explore()
        print(f"{self.name} swims around in their aquarium, what a sight to see!\n")


class BigCat(Mammal):
    def __init__(self, name, species, age, diet=None):
        Mammal.__init__(self, name, species, age, diet)
        self.__strength = 50    # Set starting strength to 50.
        self.__animals_attacked = []    # Save animals as an object to a list.
        self.__attack_count = len(self.get_animals_attacked())

    @property
    def attack_count(self):
        return self.__attack_count

    @property
    def strength(self):
        return self.__strength

    def set_strength (self, value):  # Takes an integer and updates the value for strength.
        if isinstance(value, int):
            self.__strength = max(0, min(self.__strength + value, 100))  # Ensure value is between 0-100.

    def get_animals_attacked(self):    # Returns a list of the animals attacked.
        return self.__animals_attacked

    def cry(self):
        print("Roar!!!")

    def attack(self, opponent):    # This method takes an animal object and launches an attack is the object is of the type BigCat.
        if isinstance(opponent, BigCat):
            self_damage = opponent.get_damage()
            self.set_health(self_damage)
            opponent_damage = self.get_damage()
            opponent.set_health(opponent_damage)
            self.__animals_attacked.append(opponent)
            print(self.__animals_attacked)
        else:
            print(f"{self.name} cannot attack {opponent.name} as they are a {opponent.species}.")

    def get_damage(self):    # Generates a random value and calculates damage based on strength rating.
        roll = random.random()
        damage = - (round((self.__strength * roll), 0))
        return damage

    def respond_to_zookeeper(self):
        super().respond_to_zookeeper()

    def provoke_visitor(self):    # Decreases energy and increases aggression level.
        energy_spent = -20
        aggression_gained = 20
        self.set_aggression(aggression_gained)
        self.set_energy(energy_spent)
        print(f"{self.name} has provoked a visitor at the zoo!\n")

    def eat(self, quantity):
        super().eat(quantity)    # Call parent method to update hunger level.
        strength_gained = 10
        self.set_strength(strength_gained)    # Call set_strength to increase strength level.

    def explore(self):
        super().explore()
        print(f"{self.name} runs around the plains...\n")

class Monkey(Mammal):
    def __init__(self, name, species, age, diet=None):
        Mammal.__init__(self, name, species, age, diet)
        self.__hats_stolen = 0
        self.__bananas_thrown = 0

    @property
    def bananas_thrown(self):
        return self.__bananas_thrown

    @property
    def hats_stolen(self):
        return self.__hats_stolen

    def cry(self):
        print("Give orange me give eat orange me eat orange give me eat orange give me you.\n")

    def respond_to_zookeeper(self):    # Inherits method from parent class.
        enclosure = self.get_enclosure()
        if not enclosure.is_raining:
            super().respond_to_zookeeper()
        else:
            print(f"{self.name} will not interact with zoo staff while it is raining.\n")

    def explore(self):
        enclosure = self.get_enclosure()
        if not enclosure.is_raining:
            super().explore()
            print(f"{self.name} swings from vine to vine!\n")
        else:
            print(f"{self.name} will not explore while it is raining.\n")

    def steal_visitors_hat(self):    # Updates value for happiness and aggression.
        self.__hats_stolen += 1
        happiness_gained = 25
        aggression_gained = 25
        self.set_happiness(happiness_gained)
        self.set_aggression(aggression_gained)
        print(f"{self.name} has stolen a visitors hat!\n")

    def throw_banana(self):    # Updates value for aggression and energy.
        self.__bananas_thrown += 1
        aggression_gained = 10
        energy_spent = -10
        self.set_happiness(aggression_gained)
        self.set_energy(energy_spent)
        print(f"{self.name} has thrown a banana at a visitor!\n")




