"""
File: report.py
Description: This file contains the class HealthReport which demonstrates static methods only.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
import animal
from animal import Animal, BigCat

class HealthReport:

    @staticmethod
    def generate(animal):    # This method returns a string containing animal health details.
        if isinstance(animal, Animal):
            return(
                f"*** Health report for {animal.name} ***\n"
                f"Age: {animal.age}\n"
                f"Species: {animal.species}\n"
                f"Hunger: {animal.hunger}\n"
                f"Health status: {animal.health} ({animal.get_health_string()})\n"
                f"Aggression level: {animal.aggression}\n"
                f"Happiness level: {animal.happiness}\n"
                f"Energy level: {animal.energy}\n"
            )
        else:
            return()

class BigCatReport(HealthReport):

    @staticmethod
    def generate(animal):    # This method calls the parent method and adds a string specific to the object type.
        if isinstance(animal, BigCat):
            report_str = HealthReport.generate(animal)
            report_str += (
                f"Animals attacked: {animal.attack_count}\n"
                f"Aggression level: {"LOW" if animal.attack_count <= 1 else "MEDIUM" if animal.attack_count <= 3 else "HIGH"}\n"
            )
            return report_str
        else:
            return HealthReport.generate(animal)


class MonkeyReport(HealthReport):

    @staticmethod
    def generate(animal):
        if isinstance(animal, Monkey):
            report_str = HealthReport.generate(animal)
            report_str += (
                f"Bananas thrown: {animal.bananas_thrown}\n"
                f"Hats stolen: {animal.hats_stolen}\n"
            )
            return report_str
        else:
            return HealthReport.generate(animal)