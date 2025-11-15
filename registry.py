"""
File: staff.py
Description: This file contains the class Registry, and it's child classes
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

from enclosure import Enclosure
from staff import Staff, Veterinarian, Zookeeper, AnimalTrainer
from animal import Animal, Mammal, Reptile, MarineAnimal, BigCat, Monkey

class Registry(ABC):

    def __init__(self, registry_name):
        self.__registry_name = registry_name
        self._members = {}

    def __str__(self):
        return(
            f"Registry name: {self.__registry_name}\n"
            f"Items in directory:\n"
            f"{self.get_members_string()}\n"
        )

    def get_members_string(self):
        if self._members:
            return(
                "------\n"
                + "------\n".join(str(member) for member in self._members.values())
                + "------\n"
            )
        else:
            return "No registered items"

    def generate_next_id(self):    # To generate an ID based on existing ID sequence.
        if len(self._members) == 0:
            return "001"
        existing_ids = [int(id) for id in self._members.keys()]
        new_id = max(existing_ids) + 1
        return "00" + str(new_id)

    def search_for_item(self, id):
        for member in self._members.values():
            if member.id == id:
                return member
        return None

    @abstractmethod
    def add_new(self, name):
        pass


class StaffRegistry(Registry):    # A class to hold a dictionary of staff members.

    def __init__(self, registry_name):
        super().__init__(registry_name)

    def add_new(self, name, class_type=Staff):    # Instantiates a new staff member and adds to the directory.
        if isinstance(name, str):
            new_id = self.generate_next_id()
            new_staff = class_type(name, "S-" + new_id)
            self._members[new_id] = new_staff
            return new_staff
        else:
            raise TypeError("Staff name must be a string")


class AnimalRegistry(Registry):
    def __init__(self, registry_name):
        super().__init__(registry_name)

    def add_new(self, name):    # Adds a pre-established animal object to the directory.
        if isinstance(name, Animal):
            new_id = self.generate_next_id()
            name.set_id("A-" + new_id)
            self._members[new_id] = name
        else:
            raise TypeError("Animal must be of object Animal.")


class EnclosureRegistry(Registry):
    def __init__(self, registry_name):
        super().__init__(registry_name)

    def add_new(self, enclosure):
        if isinstance(enclosure, Enclosure):
            new_id = self.generate_next_id()
            enclosure.set_id("E-" + new_id)
            self._members[new_id] = enclosure
        else:
            raise TypeError("Enclosure must be of object Enclosure.")