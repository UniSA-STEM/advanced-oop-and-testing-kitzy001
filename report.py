"""
File: report.py
Description: This file contains the class HealthReport which demonstrates static methods only.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

class HealthReport:

    @staticmethod
    def print_report(animal):
        return(
            f"*** Health report for {animal.name} ***\n"
            f"Age: {animal.get_age()}\n"
            f"Species: {animal.get_species()}\n"
            f"Hunger: {animal.get_hunger()}\n"
            f"Health status: {animal.health} ({animal.get_health_string()})\n"
        )

class BigCatReport(HealthReport):

    @staticmethod
    def print_report(animal):
        report_str = HealthReport.print_report(animal)
        report_str += (
            f"Animals attacked: {animal.get_animals_attacked()}\n"
            f"Violence rating: {animal.get_violence_rating()}\n"
        )
        return report_str
