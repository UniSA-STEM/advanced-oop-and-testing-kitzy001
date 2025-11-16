""""
File: test_*.py
Description: This file holds the unit tests for my program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from staff import Veterinarian, Zookeeper, AnimalTrainer
from animal import  Mammal, Reptile, BigCat, Monkey, MarineAnimal
from enclosure import Terrarium, Jungle
from registry import StaffRegistry, AnimalRegistry, EnclosureRegistry
from exceptions import RequirementsError

class TestAnimalStats:

    def test_set_health_above_100(self):
        """
        Tests animal health cannot exceed 100.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_health(25)
        assert animal.health == 100

    def test_set_health_below_100(self):
        """
        Tests animal health cannot go below 0.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_health(-110)
        assert animal.health == 0

    def test_set_aggression_above_100(self):
        """
        Tests animal aggression cannot exceed 100.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_aggression(110)
        assert animal.aggression == 100

    def test_set_aggression_below_100(self):
        """
        Tests animal aggression cannot go below 0.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_aggression(-25)
        assert animal.aggression == 0

    def test_set_hunger_above_100(self):
        """
        Tests animal hunger cannot exceed 100.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_hunger(15)
        assert animal.hunger == 100

    def test_set_hunger_below_100(self):
        """
        Tests animal hunger cannot go below 0.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_hunger(-110)
        assert animal.hunger == 0

    def test_set_energy_above_100(self):
        """
        Tests animal energy cannot exceed 100.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_energy(10)
        assert animal.energy == 100

    def test_set_energy_below_100(self):
        """
        Tests animal energy cannot go below 0.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_energy(-110)
        assert animal.energy == 0

    def test_set_happiness_above_100(self):
        """
        Tests animal happiness cannot exceed 100.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_happiness(60)
        assert animal.happiness == 100

    def test_set_happiness_below_100(self):
        """
        Tests animal happiness cannot go below 0.
        """
        animal = Mammal("Max", "giraffe", 10)
        animal.set_happiness(-60)
        assert animal.happiness == 0


class TestAnimalMethods:

    def test_respond_to_zookeeper(self, capsys):
        """
        Tests animal response to zookeeper updates relevant attributes accordingly.
        Also tests that the relevant print statement will execute when conditions are met.
        """
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

    def test_explore(self):
        """
        Tests animal explore method to validate the relevant attributes are updated.
        """
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

    def test_provoke_visitor(self):
        """
        Tests animal provoke_visitor method to validate the relevant attributes are updated for instances of BigCat.
        """
        animal = BigCat("Max", "lion", 10)
        animal.provoke_visitor()
        assert animal.energy == 80
        assert animal.aggression == 45

    def test_get_animals_attacked(self):
        """
        Tests get_animals_attacked method to validate the attacked animal is appended to the animals list.
        """
        animal_1 = BigCat("Max", "lion", 10)
        animal_2 = BigCat("Ben", "tiger", 10)
        animal_1.attack(animal_2)
        assert len(animal_1.get_animals_attacked()) == 1

    def test_animal_cannot_attack(self, capsys):
        """
        Tests that an animal of the type BigCat cannot attack another animal if they are not of the type BigCat.
        """
        animal_1 = BigCat("Max", "lion", 10)
        animal_2 = Reptile("Ben", "lizard", 10)
        animal_1.attack(animal_2)
        captured = capsys.readouterr()
        assert f"{animal_1.name} cannot attack {animal_2.name} as they are a {animal_2.species}." in captured.out

class TestStaffMethods:

    def test_administer_medication(self):
        """
        Tests that the administer_medication method updates the animals health attribute accordingly.
        """
        staff = Veterinarian("Val", "S-001")
        animal = BigCat("Max", "lion", 10)
        animal.set_health(-50)
        staff.administer_medication(animal)
        assert animal.health == 75

    def test_train_animal(self):
        """
        Tests that the train_animal method updates the animals aggression attribute accordingly.
        """
        staff = AnimalTrainer("Val", "S-001")
        animal = BigCat("Max", "lion", 10)
        staff.train_animal(animal)
        assert animal.aggression == 5

    def test_enrich_animal(self, capsys):
        """
        Tests that the enrich_animal method updates the animals aggression attribute accordingly, in
        edge cases where the staff member cannot swim and tries to enrich a MarineAnimal.
        """
        staff = AnimalTrainer("Val", "S-001")
        animal = MarineAnimal("Dolly", "dolphin", 5)
        with pytest.raises(RequirementsError):
            staff.enrich_animal(animal)
        staff.learn_to_swim()
        staff.enrich_animal(animal)
        captured = capsys.readouterr()
        assert f"{staff.name} enriched {animal.name}." in captured.out

    def test_clean_enclosure(self):
        """
        Tests that the test_clean_enclosure method updates the enclosures clean attribute accordingly.
        """
        staff = Zookeeper("Val", "S-001")
        enclosure = Jungle("Jagged Jungle", 10)
        enclosure.set_is_clean(False)
        staff.clean_enclosure(enclosure)
        assert enclosure.is_clean is True


class TestEnclosureMethods:

    def test_is_clean(self):
        """
        Tests that the is_clean method updates the enclosures clean attribute accordingly.
        """
        enclosure = Jungle("Jagged Jungle", 10)
        assert enclosure.is_clean is True
        enclosure.set_is_clean(False)
        assert enclosure.is_clean is False

    def test_decrease_animals_health(self):
        """
        Tests that the decrease_animals_health method updates the enclosure's animals' health attribute accordingly.
        """
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

    def test_check_for_contamination(self):
        """
        Tests that the check_for_contamination method returns True when one animal in an enclosure is sick.
        """
        enclosure = Jungle("Jagged Jungle", 10)
        animal = Monkey("Marcel", "chimpanzee", 10)
        animal_registry = AnimalRegistry("Zootopia - Animals")
        animal_registry.add_new(animal)
        enclosure.add_animal_to_enclosure(animal)
        animal.set_health(-75)
        animal.check_health()
        assert enclosure.check_for_contamination() is True

    def test_add_animal_to_enclosure(self, capsys):
        """
        Tests that add_animal_to_enclosure correctly adds an animal to an enclosure once
        they have been registered with an ID.
        """
        enclosure = Terrarium("Lizard Terrarium", 10)
        animal = Reptile("Lizzy", "lizard", 10)
        animal_registry = AnimalRegistry("Zootopia - Animals")
        animal_registry.add_new(animal)
        enclosure.add_animal_to_enclosure(animal)
        captured = capsys.readouterr()
        assert f"{animal.name} has been added to the enclosure: {enclosure.name}" in captured.out

    def test_set_temperature(self):
        """
        Tests that the method set_temperature correctly sets the enclosure's temperature attribute accordingly.
        """
        enclosure = Terrarium("Lizard Terrarium", 10)
        enclosure.set_temperature(30)
        assert enclosure.temperature == 30

    def test_search_for_animal(self):
        """
        Tests that the search_for_animal method correctly returns an animal if it exists in the
        enclosure's animal list, or none otherwise.
        """
        enclosure = Jungle("Jagged Jungle", 10)
        animal = Monkey("Marcel", "chimpanzee", 10)
        animal_registry = AnimalRegistry("Zootopia - Animals")
        animal_registry.add_new(animal)
        enclosure.add_animal_to_enclosure(animal)
        assert enclosure.search_for_animal("A-001") is not None
        assert enclosure.search_for_animal("A-002") is None

class TestRegistryMethods:

    def test_add_to_enclosure_registry(self):
        """
        Tests that the add_to_enclosure_registry method correctly adds an enclosure to the zoo's registry.
        """
        enclosure_registry = EnclosureRegistry("Zootopia - Enclosures")
        enclosure = Jungle("Jagged Jungle", 10)
        enclosure_registry.add_new(enclosure)
        assert enclosure_registry.members is not None

    def test_add_to_staff_registry(self):
        """
        Tests that the add_to_staff_registry method correctly adds a staff member to the zoo's registry.
        """
        staff_registry = StaffRegistry("Zootopia - Staff")
        staff_registry.add_new("Val", Veterinarian)
        assert staff_registry.members is not None

    def test_add_to_animal_registry(self):
        """
        Tests that the add_to_animal_registry method correctly adds an animal to the zoo's registry.
        """
        animal_registry = AnimalRegistry("Zootopia - Animals")
        animal = Reptile("Lizzy", "lizard", 10)
        animal_registry.add_new(animal)
        assert animal_registry.members is not None