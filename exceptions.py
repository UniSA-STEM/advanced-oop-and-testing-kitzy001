""""
File: exceptions.py
Description: This file contains custom exceptions used in the zoo program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

class UnregisteredAnimal(Exception):

    def __init__(self, animal_name):
        """"
        This exception raises an error when the user tries to add an unregistered animal
        to an enclosure.

        Parameters:
            animal_name(str): The name of the animal.
        """
        super().__init__(f"The animal {animal_name} has no ID. Add {animal_name} to the registry first.")

class EnclosureCapacityError(Exception):

    def __init__(self, enclosure_name):
        """
        This exception raises an error when the user tries to add an animal to an enclosure,
        when the enclosure is already at capacity.

        Parameters:
            enclosure_name(str): The enclosure to add to the registry.
        """
        super().__init__(f"Enclosure '{enclosure_name}' is at capacity, cannot add animal.")