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

    def __init__(self, name, species, age, diet=None):
        """"
        Initialises an instance of the Animal class.

        Parameters:
        name (str): The name of the animal.
            species (str): The species of the animal.
            age (int): The age of the animal.
            diet (str, optional): Type of food the animal eats.
        """
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
        """"
        This method returns a descriptive string representation of the animal.
        """
        return(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"ID: {self.id if self.id is not None else "Not registered yet"}\n"
            f"Diet: {self.__diet if self.__diet is not None else "Not yet set"}\n"
            f"Health status: {self.health} ({self.check_health()})\n"
        )

    @abstractmethod
    def cry(self):
        """
        This method defines the unique sound the animal makes.
        """
        pass

    @abstractmethod
    def respond_to_zookeeper(self):
        """
        This method defines how the animal responds to a zookeeper.
        """
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
        from enclosure import Enclosure
        if isinstance(enclosure, Enclosure):
            self.__enclosure = enclosure
        else:
            raise TypeError("Enclosure must be of type Enclosure.")

    def set_id(self, new_id):    # Setter for animal ID, called when adding animal to registry.
        if isinstance(new_id, str):
            self.__id = new_id
        else:
            raise TypeError("ID must be of type string.")

    def check_health(self):
        """
        This method returns a descriptive string for the animal's health status.
        This method also sets the is_sick attribute to True if health is low.
        """
        if self.health >= 95:
            health_str = "excellent"
        elif self.health >= 75:
            health_str = "healthy"
        elif self.health >= 40:
            health_str = "average"
        elif self.health >= 25:
            health_str = "unhealthy"
            self.__is_sick = True
        else:
            health_str = "critical"
            self.__is_sick = True
        return health_str

    def set_health(self, value):
        """
        This method updates the health value of the animal, validating that
        the value for health does not exceed 0-100.

        Parameters:
            value (int): Amount to add to current value for self.health.
        """
        if isinstance(value, int):
            new_health = self.__health + value
            self.__health = max(0, min(new_health, 100))
        else:
            raise TypeError("Health must be of type int.")

    def set_hunger(self, value):
        """
        This method updates the hunger value of the animal, validating that
        the value for hunger does not exceed 0-100.

        Parameters:
            value (int): Amount to add to current value for self.hunger.
        """
        if isinstance(value, int):
            new_hunger = self.__hunger + value
            self.__hunger = max(0, min(new_hunger, 100))
        else:
            raise TypeError("Hunger must be of type int.")

    def set_energy(self, value):
        """
        This method updates the energy value of the animal, validating that
        the value for energy does not exceed 0-100.

        Parameters:
            value (int): Amount to add to current value for self.energy.
        """
        if isinstance(value, int):
            new_energy = self.__energy + value
            self.__energy = max(0, min(new_energy, 100))
        else:
            raise TypeError("Energy must be of type int.")

    def set_happiness(self, value):
        """
        This method updates the happiness value of the animal, validating that
        the value for happiness does not exceed 0-100.

        Parameters:
            value (int): Amount to add to current value for self.happiness.
        """
        if isinstance(value, int):
            new_happiness = self.__happiness + value
            self.__happiness = max(0, min(new_happiness, 100))
        else:
            raise TypeError("Happiness must be of type int.")

    def set_aggression(self, value):
        """
        This method updates the aggression value of the animal, validating that
        the value for aggression does not exceed 0-100.

        Parameters:
            value (int): Amount to add to current value for self.aggression.
        """
        if isinstance(value, int):
            new_aggression = self.__aggression + value
            self.__aggression = max(0, min(new_aggression, 100))
        else:
            raise TypeError("Aggression must be of type int.")

    def set_diet(self, diet):
        """
        This method updates the diet attribute of the animal, validating that
        the entry is a string.

        Parameters:
            diet (str): String to describe diet e.g. "fish"
        """
        if isinstance(diet, str):
            self.__diet = diet
        else:
            raise TypeError("Diet must be a string")

    def eat(self, quantity):
        """
        This method validates the animals diet has been set and updates the animals
        hunger value based on the quantity provided.
        Also prints feedback to screen where no diet has been set.

        Parameters:
            quantity (int): Units of food.
        """
        if self.__diet is not None:
            print(f"Eating {quantity} {self.__diet}...\n")
            self.set_hunger(quantity)
        else:
            print(f"No diet set for {self.name}. Please set a diet.\n")

    def sleep(self):
        """
        This method updates the value for the animals energy and health level as
        the animal has slept.
        """
        energy_increase = 50
        health_increase = 10
        self.set_energy(energy_increase)
        self.set_health(health_increase)

    def explore(self):
        """
        This method updates the value for the animals energy, happiness, aggression,
        hunger and health level as the animal has explored.
        """
        energy_spent = -20
        happiness_gained = 20
        aggression_decrease = -20
        hunger_change = -20
        health_change = -15
        self.set_energy(energy_spent)
        self.set_happiness(happiness_gained)
        self.set_aggression(aggression_decrease)
        self.set_hunger(hunger_change)
        self.set_health(health_change)

    def fit_for_transfer(self):
        """"
        This method checks to see if an animal is fit for enclosure transfer, based on their sickness
        or behaviour, and returns a boolean value of true or false.
        """
        if self.is_sick or self.aggression >= 30:
            return False
        else:
            return True


class Mammal(Animal):

    def __init__(self, name, species, age, diet=None, habitat=None):
        """"
        Initialises an instance of the Mammal class, subclass of Animal class.

        Additional parameters:
            habitat (str) : name of the animal's habitat.
        """
        super().__init__(name, species, age, diet)
        self.__habitat = habitat

    @property
    def habitat(self):
        return self.__habitat

    def set_habitat(self, habitat):
        """
        This method updates the value for the animals habitat attribute.

        Parameters:
            habitat (str): name of the animal's habitat.
        """
        if isinstance(habitat, str):
            self.__habitat = habitat
        else:
            raise TypeError("Habitat must be of type string.")

    def cry(self):
        print("Mammal noises...\n")

    def respond_to_zookeeper(self):
        """
        This method updates the animal attribute values based on the Mammal class nature,
        when the animal has interacted with a zookeeper.
        """
        if self.aggression == 0:
            happiness_gained = 20
        elif self.aggression <= 50:
            happiness_gained = 5
        else:
            happiness_gained = -20
        self.set_happiness(happiness_gained)
        return True


class Reptile(Animal):

    def __init__(self, name, species, age, diet=None):
        """"
        Initialises an instance of the Reptile class, subclass of Animal class.
        """
        Animal.__init__(self, name, species, age, diet)
        self.set_aggression(25)
        self.__egg_count = 0

    def cry(self):
        print("Hiss...\n")

    def respond_to_zookeeper(self):
        """
        This method updates the animal attribute values based on the Reptile class nature,
        when the animal has interacted with a zookeeper.
        """
        if self.aggression == 0:
            happiness_gained = 50
        elif self.aggression <= 50:
            happiness_gained = 10
        else:
            happiness_gained = - 40
        self.set_happiness(happiness_gained)
        return True

    def lay_egg(self):
        """
        This method increases the animals egg count value by 1.
        """
        self.__egg_count += 1

    def bathe_in_sun(self):
        """
        This method updates the animal attribute values for happiness and
        aggression after the animal has bathed in the sun.
        """
        happiness_gained = 20
        aggression_decrease = -20
        self.set_happiness(happiness_gained)
        self.set_aggression(aggression_decrease)

    def explore(self):
        """
        This method adds a descriptive string to the parent method.
        """
        super().explore()
        print(f"{self.name} explores their terrarium and finds a new hiding place!\n")


class MarineAnimal(Animal):

    def __init__(self, name, species, age, diet=None):
        """"
        Initialises an instance of the MarineAnimal class, subclass of Animal class.
        """
        Animal.__init__(self, name, species, age, diet)

    def cry(self):
        print("Underwater noises....\n")

    def respond_to_zookeeper(self):
        """
        This method updates the animal attribute values based on the MarineAnimal class nature,
        when the animal has interacted with a zookeeper.
        """
        if self.aggression == 0:
            happiness_gained = 10
        elif self.aggression <= 50:
            happiness_gained = 0
        else:
            happiness_gained = -50
        self.set_happiness(happiness_gained)
        return True

    def swim_with_trainer(self):
        """
        This method updates the animal attribute values for happiness and energy
        after the animal has swum with an animal trainer.
        """
        happiness_gained = 30
        energy_spent = -30
        self.set_happiness(happiness_gained)
        self.set_energy(energy_spent)

    def explore(self):
        """
        This method adds a descriptive string to the parent method.
        """
        super().explore()
        print(f"{self.name} swims around in their aquarium, what a sight to see!\n")


class BigCat(Mammal):

    def __init__(self, name, species, age, diet=None):
        """"
        Initialises an instance of the BigCat class, subclass of Mammal class.

        Additional attributes:
            strength(str): initialised to 50.
            animals_attacked(list): initialised to empty.
            attack_count(int): number of animals attacked.
        """
        Mammal.__init__(self, name, species, age, diet)
        self.__strength = 50
        self.__animals_attacked = []
        self.set_aggression(25)

    @property
    def attack_count(self):
        return len(self.__animals_attacked)

    @property
    def strength(self):
        return self.__strength

    def set_strength (self, value):
        """
        This method updates the strength value of the animal, validating that
        the value for strength does not exceed 0-100.

        Parameters:
            value (int): Amount to add to current value for self.strength.
        """
        if isinstance(value, int):
            new_strength = self.__strength + value
            self.__strength = max(0, min(new_strength, 100))
        else:
            raise ValueError("Strength must be an integer.")

    def get_animals_attacked(self):
        """
        This method returns a list of the animals this animal has attacked.
        """
        return self.__animals_attacked

    def print_animals_attacked(self):
        """
        This method prints a list of the animals this animal has attacked.
        """
        animals = self.get_animals_attacked()
        print(f"Animals attacked by {self.name}:")
        for animal in animals:
            print(animal.name)
        print()

    def cry(self):
        print("Roar!!!\n")

    def attack(self, opponent):
        """
        This method takes an animal as an opponent and launches an attack, calling get_damage()
        to decrease the health value of both the opponent and the animal (self).
        Also validates the opponent provided is of the type BigCat.

        Parameters:
            opponent(BigCat)
        """
        if isinstance(opponent, BigCat):
            self_damage = opponent.get_damage()
            self.set_health(int(self_damage))
            opponent_damage = self.get_damage()
            opponent.set_health(int(opponent_damage))
            print(f"{self.name} attacks {opponent.name}! {opponent.name} loses {opponent_damage} health.\n")
            self.__animals_attacked.append(opponent)
            self.set_aggression(10)
        else:
            print(f"{self.name} cannot attack {opponent.name} as they are a {opponent.species}.")

    def get_damage(self):
        """
        This method uses the random library to generate a random value and calculate
        damage based on the animals strength rating, then returns damage value.
        """
        roll = random.random()
        damage = - (round((self.__strength * roll), 0))
        return damage

    def respond_to_zookeeper(self):
        super().respond_to_zookeeper()
        return True

    def provoke_visitor(self):
        """
        This method updates the values for energy and aggression when the animal
        has provoked a visitor of the zoo.
        Also prints feedback to the screen advising of the event.
        """
        energy_spent = -20
        aggression_gained = 20
        self.set_aggression(aggression_gained)
        self.set_energy(energy_spent)
        print(f"{self.name} has provoked a visitor at the zoo!\n")

    def eat(self, quantity):
        """
        This method calls the parent method and adds to the animals strength rating in addition.
        """
        super().eat(quantity)
        strength_gained = 10
        self.set_strength(strength_gained)

    def explore(self):
        """
        This method adds a descriptive string to the parent method.
        """
        super().explore()
        print(f"{self.name} runs around the plains...\n")


class Monkey(Mammal):

    def __init__(self, name, species, age, diet=None):
        """"
        Initialises an instance of the Monkey class, subclass of Mammal class.
        """
        Mammal.__init__(self, name, species, age, diet)
        self.set_happiness(25)
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

    def respond_to_zookeeper(self):
        """
        This method updates the animal attribute values based on the Monkey class nature,
        when the animal has interacted with a zookeeper.
        """
        enclosure = self.get_enclosure()
        if enclosure is not None:
            if not enclosure.is_raining:
                super().respond_to_zookeeper()
                return True
            else:
                print(f"{self.name} will not interact with zoo staff while it is raining.\n")
                return False
        return None

    def explore(self):
        """
        This method checks that the enclosure is not currently raining and then adds a descriptive
        string to the parent method. Provides feedback to screen if enclosure is raining.
        """
        enclosure = self.get_enclosure()
        if not enclosure.is_raining:
            super().explore()
            print(f"{self.name} swings from vine to vine!\n")
        else:
            print(f"{self.name} will not explore while it is raining.\n")

    def steal_visitors_hat(self):
        """
        This method updates the attributes for hats_stolen, happiness and aggression when
        the animal steals a zoo visitors hat. Also prints feedback to screen.
        """
        self.__hats_stolen += 1
        happiness_gained = 25
        aggression_gained = 25
        self.set_happiness(happiness_gained)
        self.set_aggression(aggression_gained)
        print(f"{self.name} has stolen a visitors hat!\n")

    def throw_banana(self):
        """
        This method updates the attributes bananas_thrown, aggression and energy when
        the animal throws a banana at a zoo visitor. Also prints feedback to screen.
        """
        self.__bananas_thrown += 1
        aggression_gained = 10
        energy_spent = -10
        self.set_happiness(aggression_gained)
        self.set_energy(energy_spent)
        print(f"{self.name} has thrown a banana at a visitor!\n")




