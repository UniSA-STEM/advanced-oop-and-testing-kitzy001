""""
File: enclosure.py
Description: This file contains the animal Enclosure class and relevant subclasses.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal, Mammal, Reptile, MarineAnimal, BigCat, Monkey
from abc import ABC, abstractmethod

class Enclosure(ABC):

    def __init__(self, name, capacity, id=None, is_full=False):
        self.__name = name
        self.__capacity = capacity
        self.__id = id
        self.__is_full = is_full
        self.__animals = []

    def __str__(self):    # Returns a string of enclosure details.
        return(
            f"Enclosure name: {self.__name}\n"
            f"Enclosure ID: {self.__id}\n"
            f"Enclosure capacity: {self.__capacity}\n"
            f"Number of animals held: {len(self.__animals)}\n"
        )

    def set_name(self, name):    # Setter for overriding the Enclosure name if needed..
        if isinstance(name, str):
            self.__name = name

    def set_id(self, id):    # Setter for enclosure ID, called when adding enclosure to registry.
        if isinstance(id, str):
            self.__id = id
        else:
            raise TypeError("Enclosure ID must be of type string.")

    def get_animals(self):
        return self.__animals

    def display_animals(self):
        animal_str = ""  # Create string to display animals
        animals = self.get_animals()
        for animal in animals:
            animal_str += "-----" + str(animal) + "\n"
        if animal_str == "":    # If no animals, set animal string to empty.
            animal_str = "Empty."
        return animal_str

    @abstractmethod
    def add_animal_to_enclosure(self, animal):
        pass

    def search_for_animal(self, animal_id):
        for animal in self.__animals:
            if animal.id == animal_id:
                return animal
        return None

    def remove_animal_from_enclosure(self, animal):
        id = animal.get_id()
        is_in_enclosure = self.search_for_animal(id)
        if is_in_enclosure:
            self.__animals.remove(animal)
            print(f"Removed {animal.name} from {self.__name}.\n")
        else:
            print(f"The animal {animal.get_name()} is not in {self.__name}.\n")


class Terrarium(Enclosure):    # To hold reptiles.
    def __init__(self, name, capacity, humidity, is_full=False):
        super().__init__(name, capacity, is_full=is_full)
        self.__humidity = humidity

    def __str__(self):
        new_str = super().__str__() + "\n"
        new_str += f"Humidity: {self.__humidity}\n"

    def set_humidity(self, humidity):    # Setter for humidity level.
        if isinstance(humidity, int) or isinstance(humidity, float):
            self.__humidity = humidity

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, Reptile):
            self.__animals.append(animal)
            print(f"{animal.name} has been added to the enclosure: {self.__name}")
        else:
            raise TypeError("Animal must be of type Reptile.")


class Savannah(Enclosure):    # To hold mammals.
    def __init__(self, name, capacity, is_full=False):
        super().__init__(name, capacity, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, Mammal):
            self.__animals.append(animal)
            print(f"{animal.name} has been added to the enclosure: {self.__name}")
        else:
            raise TypeError("Animal must be of type Mammal.")


class Australiana(Savannah):    # To hold Australian animals.
    def __init__(self, name, capacity, is_full=False):
        super().__init__(name, capacity, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, Mammal):
            self.__animals.append(animal)
            print(f"{animal.name} has been added to the enclosure: {self.__name}")
        else:
            raise TypeError("Animal must be of type Mammal.")

class African(Savannah):    # To hold African animals.
    def __init__(self, name, capacity, is_full=False):
        super().__init__(name, capacity, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, Mammal):
            self.__animals.append(animal)
            print(f"{animal.name} has been added to the enclosure: {self.__name}")
        else:
            raise TypeError("Animal must be of type Mammal.")
