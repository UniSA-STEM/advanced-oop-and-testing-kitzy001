""""
File: exceptions.py
Description: This file contains custom exceptions used in the zoo program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

class UnregisteredAnimal(Exception):    # Custom exception to raise when adding an unregistered animal to enclosure.
    def __init__(self, animal_name):
        super().__init__(f"The animal {animal_name} has no ID. Add {animal_name} to the registry first.")