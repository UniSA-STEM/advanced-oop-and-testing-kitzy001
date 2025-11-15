""""
File: test_*.py
Description: This file holds the unit tests for my program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff, Veterinarian, Zookeeper, AnimalTrainer
from animal import Animal, Mammal, Reptile, MarineAnimal, BigCat, Monkey
from enclosure import Enclosure, Terrarium, Savannah, African, Aquarium, Jungle
from registry import Registry, StaffRegistry, AnimalRegistry, EnclosureRegistry
from report import HealthReport, BigCatReport
import pytest

class TestAnimalStats:

    def test_set_health_above_100(self):    # Validates animal health can not exceed 100.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_health(25)
        assert animal.health == 100

    def test_set_health_below_100(self):     # Validates animal health can not go below 0.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_health(-110)
        assert animal.health == 0

    def test_set_aggression_above_100(self):    # Validates animal aggression can not exceed 100.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_aggression(110)
        assert animal.aggression == 100

    def test_set_aggression_below_100(self):    # Validates animal aggression can not go below 0.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_aggression(-25)
        assert animal.aggression == 0

    def test_set_hunger_above_100(self):    # Validates animal hunger can not exceed 100.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_hunger(15)
        assert animal.hunger == 100

    def test_set_hunger_below_100(self):    # Validates animal hunger can not go below 0
        animal = Mammal("Max", "giraffe", 10)
        animal.set_hunger(-110)
        assert animal.hunger == 0

    def test_set_energy_above_100(self):    # Validates animal energy can not exceed 100.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_energy(10)
        assert animal.energy == 100

    def test_set_energy_below_100(self):    # Validates animal energy cannot go below 0.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_energy(-110)
        assert animal.energy == 0

    @staticmethod
    def test_set_happiness_above_100():    # Validates animal happiness can not exceed 100.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_happiness(60)
        assert animal.happiness == 100

    def test_set_happiness_below_100(self):    # Validates animal energy cannot go below 0.
        animal = Mammal("Max", "giraffe", 10)
        animal.set_happiness(-60)
        assert animal.happiness == 0


class TestAnimalMethods:

    def test_respond_to_zookeeper(self, capsys):    # Validates BigCat happiness increases by 5 when calling respond_to_zookeeper.
        animal_1 = BigCat("Max", "lion", 10)
        animal_1.respond_to_zookeeper()
        assert animal_1.happiness == 55

        animal_2 = Mammal("Max", "giraffe", 10)
        animal_2.respond_to_zookeeper()
        assert animal_2.happiness == 70

        animal_3 = Monkey("Max", "chimpanzee", 10)
        enclosure = Jungle("Jagged Jungle", 10)
        animal_registry = AnimalRegistry("Zootopia - Animals")
        animal_registry.add_new(animal_3)
        enclosure.add_animal_to_enclosure(animal_3)
        enclosure.set_is_raining(True)
        animal_3.respond_to_zookeeper()
        captured = capsys.readouterr()
        assert f"{animal_3.name} will not interact with zoo staff while it is raining." in captured.out

    def test_explore(self):    # Validates the relevant attributes are updated when explore() is called.
        animal = Monkey("Max", "chimpanzee", 10)
        enclosure = Jungle("Jagged Jungle", 10)
        animal_registry = AnimalRegistry("Zootopia - Animals")
        animal_registry.add_new(animal)
        enclosure.add_animal_to_enclosure(animal)
        animal.explore()
        assert animal.health == 85
        assert animal.happiness == 95
        assert animal.hunger == 80
        assert animal.energy == 80
        assert animal.aggression == 0

    def test_provoke_visitor(self):    # Validates the relevant attributes are updated when provoke_visitor() is called.
        animal = BigCat("Max", "lion", 10)
        animal.provoke_visitor()
        assert animal.energy == 80
        assert animal.aggression == 45

    def test_get_animals_attacked(self):    # Validates an animal is appended to another animals list of attacked animals.
        animal_1 = BigCat("Max", "lion", 10)
        animal_2 = BigCat("Ben", "tiger", 10)
        animal_1.attack(animal_2)
        assert len(animal_1.get_animals_attacked()) == 1

    def test_animal_cannot_attack(self, capsys):    # Validates an animal cannot be attacked if it is not of the same subclass type.
        animal_1 = BigCat("Max", "lion", 10)
        animal_2 = Reptile("Ben", "lizard", 10)
        animal_1.attack(animal_2)
        captured = capsys.readouterr()
        assert f"{animal_1.name} cannot attack {animal_2.name} as they are a {animal_2.species}." in captured.out

class TestStaffMethods:

    def test_administer_medication(self):    # Validate staff method updates animal health attribute accordingly.
        staff = Veterinarian("Val", "S-001")
        animal = BigCat("Max", "lion", 10)
        animal.set_health(-50)
        staff.administer_medication(animal)
        assert animal.health == 75

    def test_train_animal(self):    # Validate staff method updates animal aggression attribute accordingly.
        staff = AnimalTrainer("Val", "S-001")
        animal = BigCat("Max", "lion", 10)
        staff.train_animal(animal)
        assert animal.aggression == 5

    def test_clean_enclosure(self):    # Validate staff method updates enclosure is_clean attribute accordingly.
        staff = Zookeeper("Val", "S-001")
        enclosure = Jungle("Jagged Jungle", 10)
        enclosure.set_is_clean(False)
        staff.clean_enclosure(enclosure)
        assert enclosure.is_clean is True


class TestEnclosureMethods:

    def test_is_clean(self):
        enclosure = Jungle("Jagged Jungle", 10)
        assert enclosure.is_clean is True
        enclosure.set_is_clean(False)
        assert enclosure.is_clean is False

    def test_decrease_animals_health(self):
        enclosure = Jungle("Jagged Jungle", 10)
        animal_1 = Monkey("Marcel", "chimpanzee", 10)
        animal_2 = Monkey("Gary", "gorilla", 5)
        animal_registry = AnimalRegistry("Zootopia - Animals")
        animal_registry.add_new(animal_1)
        animal_registry.add_new(animal_2)
        enclosure.add_animal_to_enclosure(animal_1)
        enclosure.add_animal_to_enclosure(animal_2)
        enclosure.decrease_animals_health()
        assert animal_1.health == 90
        assert animal_2.health == 90


