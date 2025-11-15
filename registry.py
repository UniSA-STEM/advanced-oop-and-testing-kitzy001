"""
File: registry.py
Description: This file contains the class Registry, and it's child classes.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

from enclosure import Enclosure
from animal import Animal
from staff import Staff

class Registry(ABC):

    def __init__(self, registry_name):
        """"
        Initialises an instance of the Registry class.

        Parameters:
            registry_name (str): The name of the registry.
        """
        self.__registry_name = registry_name
        self._members = {}

    def __str__(self):
        """"
        Returns a string representation of the registry.
        """
        return(
            f"Registry name: {self.__registry_name}\n"
            f"Items in directory:\n"
            f"{self.get_members_string()}\n"
        )

    @property
    def members(self):
        return self._members

    def get_members_string(self):
        """"
        Returns a string displaying all the members of the registry.
        """
        if self._members:
            return(
                "------\n"
                + "------\n".join(str(member) for member in self._members.values())
                + "------\n"
            )
        else:
            return "No registered items"

    def generate_next_id(self):
        """
        This method generates an ID, using the members set{} to generate the next ID in the sequence.
        """
        if len(self._members) == 0:
            return "001"
        existing_ids = [int(iden) for iden in self._members.keys()]
        new_id = max(existing_ids) + 1
        return "00" + str(new_id)

    def search_for_item(self, iden):
        """
        This method takes an ID and searches to see if the ID exists in the registry.
        Returns the member if found, None otherwise.
        """
        for member in self._members.values():
            if member.id == iden:
                return member
        return None

    @abstractmethod
    def add_new(self, name):
        pass


class StaffRegistry(Registry):

    def __init__(self, registry_name):
        super().__init__(registry_name)

    def add_new(self, name, class_type=Staff):
        """
        Instantiates a new instance of the Staff class and adds it to the registry.
        Parameters:
            name (str): The name of the staff member.
            class_type(type): The class type of the staff member e.g. Veterinarian.
        """
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

    def add_new(self, name):
        """
        Takes an already initialised animal and adds it to the registry, generating an ID
        and updating the animal attribute for ID.

        Parameters:
            name (Animal): The animal to add to the registry.
        """
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
        """
        Takes an already initialised enclosure and adds it to the registry, generating an ID
        and updating the enclosure attribute for ID.

        Parameters:
            enclosure(Enclosure): The enclosure to add to the registry.
        """
        if isinstance(enclosure, Enclosure):
            new_id = self.generate_next_id()
            enclosure.set_id("E-" + new_id)
            self._members[new_id] = enclosure
        else:
            raise TypeError("Enclosure must be of object Enclosure.")