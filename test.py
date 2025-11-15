""""
File: test.py
Description: This file holds the unit tests for my program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff, Veterinarian, Zookeeper, AnimalTrainer
from animal import Animal, Mammal, Reptile, MarineAnimal, BigCat, Monkey
from enclosure import Enclosure, Terrarium, Savannah, Australiana, African, Aquarium, Jungle
from registry import Registry, StaffRegistry, AnimalRegistry, EnclosureRegistry
from report import HealthReport, BigCatReport

import pytest

class TestAnimalStats:

    def test_set_health_above_100(self):    # Validates animal health can not exceed 100.
        animal = Mammal()
        animal.set_health(25)
        assert animal.health == 100

    def test_set_health_below_100(self):     # Validates animal health can not go below 0.
        animal = Mammal()
        animal.set_health(-110)
        assert animal.health == 0

    def test_set_aggression_above_100(self):    # Validates animal aggression can not exceed 100.
        animal = Mammal()
        animal.set_aggression(110)
        assert animal.aggression == 100

    def test_set_aggression_below_100(self):    # Validates animal aggression can not go below 0.
        animal = Mammal()
        animal.set_aggression(-25)
        assert animal.aggression == 0

    def test_set_hunger_above_100(self):    # Validates animal hunger can not exceed 100.
        animal = Mammal()
        animal.set_hunger(15)
        assert animal.hunger == 100

    def test_set_hunger_below_100(self):    # Validates animal hunger can not go below 0
        animal = Mammal()
        animal.set_hunger(-15)
        assert animal.hunger == 0

    def test_set_energy_above_100(self):    # Validates animal energy can not exceed 100.
        animal = Mammal()
        animal.set_energy(10)
        assert animal.energy == 100

    def test_set_energy_below_100(self):    # Validates animal energy cannot go below 0.
        animal = Mammal()
        animal.set_energy(-10)
        assert animal.energy == 0

    def test_set_happiness_above_100(self):    # Validates animal happiness can not exceed 100.
        animal = Mammal()
        animal.set_happiness(60)
        assert animal.happiness == 100

    def test_set_happiness_below_100(self):    # Validates animal energy cannot go below 0.
        animal = Mammal()
        animal.set_happiness(-60)
        assert animal.happiness == 0


class TestAnimalMethods:

    def test_respond_to_zookeeper(self, capsys):    # Validates BigCat happiness increases by 5 when calling respond_to_zookeeper.
        animal_1 = BigCat()
        animal_1.respond_to_zookeeper()
        assert animal_1.happiness == 55

        animal_2 = Mammal()
        animal_2.respond_to_zookeeper()
        assert animal_2.happiness == 70

        animal_3 = Monkey
        enclosure = Jungle("Jagged Jungle", 10)
        enclosure.add_animal_to_enclosure(animal_3)
        enclosure.set_is_raining(True)
        animal_3.respond_to_zookeeper()
        captured = capsys.readouterr()
        assert f"{animal_3.name} will not interact with zoo staff while it is raining." in captured.out

    def test_explore(self):
        animal = Monkey()
        animal.explore()
        assert animal.health == 85
        assert animal.happiness == 95
        assert animal.hunger == 80
        assert animal.energy == 80
        assert animal.aggression == 0

    def test_provoke_visitor(self):
        animal = BigCat()
        animal.provoke_visitor()
        assert animal.energy == 80
        assert animal.aggression == 45




