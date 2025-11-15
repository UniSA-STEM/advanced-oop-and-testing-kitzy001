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
from exceptions import UnregisteredAnimal

class Enclosure(ABC):

    def __init__(self, name, capacity, id=None, is_full=False):
        self._name = name
        self._capacity = capacity
        self._id = id
        self._is_full = is_full
        self._animals = []
        self._is_clean = True

    def __str__(self):    # Returns a string of enclosure details.
        return(
            f"Enclosure name: {self._name}\n"
            f"Enclosure ID: {self._id}\n"
            f"Enclosure capacity: {self._capacity}\n"
            f"Number of animals held: {len(self._animals)}\n"
            f"Is currently clean: {self._is_clean}\n"
        )

    @abstractmethod
    def add_animal_to_enclosure(self, animal):
        pass

    @property
    def name(self):
        return self._name

    @property
    def is_clean(self):
        return self._is_clean

    def set_id(self, id):    # Setter for enclosure ID, called when adding enclosure to registry.
        if isinstance(id, str):
            self._id = id
        else:
            raise TypeError("Enclosure ID must be of type string.")

    def set_is_clean(self):    # Sets attribute for is_clean to True.
        self._is_clean = True

    def add_animal(self, animal):    # Validates there is capacity in enclosure and adds animal.
        if self._is_full == False:
            if animal.id is not None:
                self._animals.append(animal)
                animal.set_enclosure(self)
                self._is_clean = False
                if len(self._animals) == self._capacity:
                    self._is_full = True
                return True
            else:
                raise UnregisteredAnimal(animal.name)
        else:
            raise ValueError("Enclosure is already at capacity.")

    def search_for_animal(self, animal_id):    # Returns animal if animal found in enclosure list.
        for animal in self._animals:
            if animal.id == animal_id:
                return animal
        return None

    def remove_animal(self, animal):    # Removes animal if found in enclosure list.
        id = animal.get_id()
        is_in_enclosure = self.search_for_animal(id)
        if is_in_enclosure:
            self._animals.remove(animal)
            print(f"Removed {animal.name} from {self._name}.\n")
            if len(self._animals) < self._capacity:    # Check for enclosure capacity after removal.
                self._is_full = False
        else:
            print(f"The animal {animal.get_name()} is not in {self._name}.\n")

    def display_animals(self):    # Prints a string which displays animals in enclosure.
        animal_str = ""
        animals = self._animals
        for animal in animals:
            animal_str += "-----" + str(animal) + "\n"
        if animal_str == "":    # If no animals, set animal string to empty.
            animal_str = "Empty."
        print(animal_str)

    def decrease_animals_health(self):    # Decreases the health value for all animals in the enclosure.
        for animal in self._animals:
            health_update = -10
            animal.set_health(health_update)


class ControlledEnclosure(Enclosure):    # An enclosure that can have its temperature controlled.
    def __init__(self, name, capacity, temperature, is_full=False):
        super().__init__(name, capacity, id=None, is_full=is_full)
        self.__temperature = temperature

    def __str__(self):
        new_str = super().__str__() + "\n"
        new_str += f"Temperature: {self.__temperature}\n"
        return new_str

    @property
    def temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):    # Setter for temperature.
        if isinstance(temperature, int) or isinstance(temperature, float):
            self.__temperature = temperature

    def add_animal_to_enclosure(self, animal):
        pass


class Savannah(Enclosure):    # Class to hold mammals.
    def __init__(self, name, capacity, is_full=False):
        super().__init__(name, capacity, id=None, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, Mammal):
            added = self.add_animal(animal)    # Call parent method to add to enclosure list.
            if added:
                print(f"{animal.name} has been added to the enclosure: {self._name}")
        else:
            raise TypeError("Animal must be of type Mammal.")


class Australiana(Savannah):    # Class to hold Australian animals.
    def __init__(self, name, capacity, is_full=False):
        super().__init__(name, capacity, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
            if isinstance(animal, Mammal):
                added = self.add_animal(animal)    # Call parent method to add to enclosure list.
                if added:
                    print(f"{animal.name} has been added to the enclosure: {self._name}")
            else:
                raise TypeError("Animal must be of type Mammal.")


class African(Savannah):    # Class to hold African animals.
    def __init__(self, name, capacity, is_full=False):
        super().__init__(name, capacity, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, Mammal):
            added = self.add_animal(animal)    # Call parent method to add to enclosure list.
            if added:
                print(f"{animal.name} has been added to the enclosure: {self._name}")
        else:
            raise TypeError("Animal must be of type Mammal.")


class Terrarium(ControlledEnclosure):    # Class to hold reptiles.
    def __init__(self, name, capacity, temperature=20, is_full=False):
        super().__init__(name, capacity, temperature, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, Reptile):
            added = self.add_animal(animal)    # Call parent method to add to enclosure list.
            if added:
                print(f"{animal.name} has been added to the enclosure: {self._name}")
        else:
            raise TypeError("Animal must be of type Reptile.")


class Aquarium(ControlledEnclosure):    # Class to hold marine animals.
    def __init__(self, name, capacity, temperature=27, is_full=False):
        super().__init__(name, capacity, temperature, is_full=is_full)

    def add_animal_to_enclosure(self, animal):
        if isinstance(animal, MarineAnimal):
            added = self.add_animal(animal)    # Call parent method to add to enclosure list.
            if added:
                print(f"{animal.name} has been added to the enclosure: {self._name}")
        else:
            raise TypeError("Animal must be of type MarineAnimal.")




