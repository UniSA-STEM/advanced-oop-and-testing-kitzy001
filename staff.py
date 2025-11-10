"""
File: staff.py
Description: This file contains the class Staff
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
import random

from animal import Animal, Mammal, Reptile, MarineAnimal, BigCat, Monkey
from enclosure import Enclosure, Terrarium, Savannah, Australiana, African, Aquarium
from report import HealthReport, BigCatReport


class Staff:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def __str__(self):
        return(
            f"Staff name: {self.name}\n"
            f"ID: {self.__id}\n"
        )

    @property
    def name(self):
        return self.__name

    def get_id(self):
        return self.__id


class Veterinarian(Staff):

    def __init__(self, name, id, specialisation=None):
        super().__init__(name, id)
        self.__specialisation = specialisation

    def get_specialisation(self):
        return self.__specialisation

    def set_specialisation(self, specialisation):    # Set specialisation e.g. Mammal Veterinarian.
        if isinstance(specialisation, str):
            self.__specialisation = specialisation
        else:
            raise TypeError("Specialisation must be a string")

    def perform_health_check(self, animal):
        if isinstance (animal, Animal):
            print(f"{self.name} printing report...\n")
            if isinstance(animal, BigCat):
                print(BigCatReport.print_report(animal))
            else:
                print(HealthReport.print_report(animal))


class Zookeeper(Staff):

    def __init__(self, name, id):
        super().__init__(name, id)

    def clean_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            enclosure.clean_enclosure()


class Administrator(Staff):

    def __init__(self, name, id):
        super().__init__(name, id)

