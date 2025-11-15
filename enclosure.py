""""
File: enclosure.py
Description: This file contains the animal Enclosure class and relevant subclasses.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Mammal, Reptile, MarineAnimal, BigCat, Monkey
from abc import ABC, abstractmethod
from exceptions import UnregisteredAnimal, EnclosureCapacityError

class Enclosure(ABC):
    """"
    Initialises an instance of the Enclosure class.

    Parameters:
        name (str): The name of the enclosure.
        capacity (int): The capacity of the enclosure.
    """
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        self._id = None
        self._is_full = False
        self._animals = []
        self._is_clean = True

    def __str__(self):
        """"
        This method returns a descriptive string representation of the enclosure.
        """
        return(
            f"Enclosure name: {self.name}\n"
            f"Enclosure ID: {self.id}\n"
            f"Enclosure capacity: {self.capacity}\n"
            f"Number of animals held: {len(self._animals)}\n"
            f"Is currently clean: {self.is_clean}\n"
        )

    @abstractmethod
    def add_animal_to_enclosure(self, animal):
        """"
        This method adds an animal to the enclosure.
        """
        pass

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def capacity(self):
        return self._capacity

    @property
    def is_clean(self):
        return self._is_clean

    @property
    def is_full(self):
        return self._is_full

    def set_id(self, enclosure_id):
        """
        Setter for enclosure ID, called when adding an enclosure to a registry.

        Parameters:
            enclosure_id (str): The ID of the enclosure.
        """
        if isinstance(enclosure_id, str):
            self._id = enclosure_id
        else:
            raise TypeError("Enclosure ID must be of type string.")

    def set_is_clean(self, boolean):
        """
        Setter for is_clean attribute, validates a boolean is being passed through.

        Parameters:
            boolean (bool): True or False.
        """
        if isinstance(boolean, bool):
            self._is_clean = boolean
        else:
            raise TypeError("Must be True or False.")

    def add_animal(self, animal):
        """
        This method adds an animal to the enclosure after validating the enclosure
        is not already full.
        Also raises a custom exception if the animal is not yet registered, or if the enclosure is full.

        Parameters:
            animal (Animal): The animal to add to the enclosure.
        """
        if not self.is_full:
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
            raise EnclosureCapacityError(animal.name)

    def search_for_animal(self, animal_id):
        """
        This method takes an ID and searches for an animal in the enclosure list of animals.
        Returns animal if True.

        Parameters:
            animal_id(str): The ID of the animal.
        """
        for animal in self._animals:
            if animal.id == animal_id:
                return animal
        return None

    def remove_animal(self, animal):
        """
        This method takes an animal as a parameter and calls the search_for_animal() method to determine
        if the animal exists in the enclosure. If the animal is in the enclosure, this method removes the animal.
        This method then checks if the capacity is full and updates the attribute accordingly.

        Parameters:
            animal(Animal): The animal to remove from the enclosure.
        """
        animal_id = animal.get_id()
        is_in_enclosure = self.search_for_animal(animal_id)
        if is_in_enclosure:
            self._animals.remove(animal)
            print(f"Removed {animal.name} from {self._name}.\n")
            if len(self._animals) < self._capacity:
                self._is_full = False
        else:
            print(f"The animal {animal.name} is not in {self._name}.\n")

    def display_animals(self):
        """
        This method prints a descriptive string which displays all animals in the enclosure.
        """
        animal_str = ""
        animals = self._animals
        for animal in animals:
            animal_str += "-----" + str(animal) + "\n"
        if animal_str == "":
            animal_str = "Empty."
        print(animal_str)

    def decrease_animals_health(self):
        """
        This method decreases the health value of all animals in the enclosure by 10.
        """
        for animal in self._animals:
            health_update = -10
            animal.set_health(health_update)

    def check_for_contamination(self):
        """
        This method checks to see if any animal in the enclosure is currently sick, and calls the
        decrease_animals_health() method to decrease all animals health if True.
        """
        if any(animal.is_sick for animal in self._animals):
            animal_decrease = -10
            for animal in self._animals:
                animal.set_health(animal_decrease)
            return True
        return False

class Jungle(Enclosure):

    def __init__(self, name, capacity):
        """"
        Initialises an instance of the Jungle class, subclass of Enclosure class.

        New attribute:
            is_raining(bool): if the jungle enclosure is currently experiencing rain.
        """
        super().__init__(name, capacity)
        self.__is_raining = False

    def __str__(self):
        """
        Adds a descriptive string to the parent method.
        """
        new_str = super().__str__() + "\n"
        new_str += f"Is currently raining: {self.is_raining}.\n"
        return new_str

    @property
    def is_raining(self):
        return self.__is_raining

    def set_is_raining(self, boolean):
        """
        Sets value for the is_raining attribute to True or False.

        Parameters:
            boolean (bool): True or False.
        """
        if isinstance(boolean, bool):
            self.__is_raining = boolean
        else:
            raise TypeError("Must enter True or False")

    def add_animal_to_enclosure(self, animal):
        """
        This method takes an animal and validates it is of the type Monkey.
        If the animal is of the type Monkey, parent method add_animal() is called
        to add the animal to the enclosures list of animals.
        """
        if isinstance(animal, Monkey):
            added = self.add_animal(animal)
            if added:
                print(f"{animal.name} has been added to the enclosure: {self.name}")
        else:
            raise TypeError("Animal must be of type Monkey.")


class Savannah(Enclosure):

    def __init__(self, name, capacity):
        """
        Initialises an instance of the Savannah class, subclass of Enclosure class.
        """
        super().__init__(name, capacity)

    def add_animal_to_enclosure(self, animal):
        """
        This method takes an animal and validates it is of the type Mammal.
        If the animal is of the type Mammal, parent method add_animal() is called
        to add the animal to the enclosures list of animals.
        """
        if isinstance(animal, Mammal):
            added = self.add_animal(animal)
            if added:
                print(f"{animal.name} has been added to the enclosure: {self._name}")
        else:
            raise TypeError("Animal must be of type Mammal.")


class African(Savannah):
    def __init__(self, name, capacity):
        """
        Initialises an instance of the African class, subclass of Savannah class.
        """
        super().__init__(name, capacity)

    def add_animal_to_enclosure(self, animal):
        """
        This method takes an animal and validates it is of the type BigCat.
        If the animal is of the type BigCat, parent method add_animal() is called
        to add the animal to the enclosures list of animals.
        """
        if isinstance(animal, BigCat):
            added = self.add_animal(animal)
            if added:
                print(f"{animal.name} has been added to the enclosure: {self.name}")
        else:
            raise TypeError("Animal must be of type Big Cat.")


class ControlledEnclosure(Enclosure):

    def __init__(self, name, capacity, temperature=20):
        """
        Initialises an instance of the ControlledEnclosure class, subclass of Enclosure class.

        Additional parameters:
            temperature (int): The temperature of the enclosure.
        """
        super().__init__(name, capacity)
        self.__temperature = temperature

    def __str__(self):
        """
        Adds a descriptive string to the parent method.
        """
        new_str = super().__str__() + "\n"
        new_str += f"Temperature: {self.temperature} degrees Celsius\n"
        return new_str

    @property
    def temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        """
        Updates the value for temperature.

        Parameters:
            temperature (int or float): The temperature of the enclosure.
        """
        if isinstance(temperature, int) or isinstance(temperature, float):
            self.__temperature = temperature
        else:
            raise TypeError("Temperature must be of type int or float.")

    def add_animal_to_enclosure(self, animal):
        pass


class Terrarium(ControlledEnclosure):

    def __init__(self, name, capacity, temperature=20):
        """
        Initialises an instance of the Terrarium class, subclass of ControlledEnclosure class.
        """
        super().__init__(name, capacity, temperature)

    def add_animal_to_enclosure(self, animal):
        """
        This method takes an animal and validates it is of the type Reptile.
        If the animal is of the type Reptile, parent method add_animal() is called
        to add the animal to the enclosures list of animals.
        """
        if isinstance(animal, Reptile):
            added = self.add_animal(animal)
            if added:
                print(f"{animal.name} has been added to the enclosure: {self.name}")
        else:
            raise TypeError("Animal must be of type Reptile.")


class Aquarium(ControlledEnclosure):

    def __init__(self, name, capacity, temperature=27):
        """
        Initialises an instance of the Aquarium class, subclass of ControlledEnclosure class.
        """
        super().__init__(name, capacity, temperature)

    def add_animal_to_enclosure(self, animal):
        """
        This method takes an animal and validates it is of the type MarineAnimal.
        If the animal is of the type MarineAnimal, parent method add_animal() is called
        to add the animal to the enclosures list of animals.
        """
        if isinstance(animal, MarineAnimal):
            added = self.add_animal(animal)
            if added:
                print(f"{animal.name} has been added to the enclosure: {self.name}")
        else:
            raise TypeError("Animal must be of type MarineAnimal.")




