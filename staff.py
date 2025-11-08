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

class Staff(ABC):

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def __str__(self):
        return(
            f"Staff name: {self.__name}\n"
            f"ID: {self.__id}\n"
        )

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class Veterinarian(Staff):
    pass

class Zookeeper(Staff):
    pass

class Administrator(Staff):
    pass

