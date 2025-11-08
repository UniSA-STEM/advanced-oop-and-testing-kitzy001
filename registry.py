"""
File: staff.py
Description: This file contains the class Staff
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
from staff import Staff
import random

class StaffRegistry:    # A class to hold a dictionary of staff members.

    def __init__(self):
        self.__staff_members = {}

    def generate_next_id(self):    # To generate an employee ID based on existing ID sequence.
        if len(self.__staff_members) == 0:
            return "001"
        existing_ids = [int(id) for id in self.__staff_members.keys()]
        new_id = max(existing_ids) + 1
        return "00" + str(new_id)

    def add_new_staff(self, name, class_type=Staff):
        if isinstance(name, str):
            new_id = self.generate_next_id()
            new_staff = class_type(name, new_id)
            self.__staff_members[new_id] = new_staff # Add to dictionary
            return new_staff
        else:
            raise TypeError("Name must be a string")

    def get_staff_list(self):
        return list(self.__staff_members.values())


zoo = StaffRegistry()
zoe = zoo.add_new_staff("Zoe")
tom = zoo.add_new_staff("Tom")
fred = zoo.add_new_staff("Fred")
print(zoe)
print(tom)

print(fred)