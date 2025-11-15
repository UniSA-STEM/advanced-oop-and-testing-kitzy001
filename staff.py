"""
File: staff.py
Description: This file contains the class Staff
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal, Mammal, Reptile, MarineAnimal, BigCat, Monkey
from enclosure import Enclosure, Terrarium, Savannah, Australiana, African, Aquarium
from registry import Registry, StaffRegistry, AnimalRegistry, EnclosureRegistry
from report import HealthReport, BigCatReport, MonkeyReport


class Staff:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__is_working = False
        self.__can_handle_animal = False
        self.__is_on_leave = False

    def __str__(self):
        return(
            f"Staff name: {self.name}\n"
            f"ID: {self.__id}\n"
        )

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def can_handle_animal(self):
        return self.__can_handle_animal

    def enrich_animal(self, animal):
        if isinstance(animal, Animal):
            if self.can_handle_animal:
                happiness_increase = 10
                animal.set_happiness(happiness_increase)
                print(f"{self.name} enriched {animal.name}.")
            else:
                print(f"{self.name} is not able to interact with {animal.name}.")

    def clock_in(self):
        self.__is_working = True

    def clock_out(self):
        self.__is_working = False

    def set_is_on_leave(self, boolean):
        if isinstance(boolean, bool):
            self.__is_on_leave = boolean


class Veterinarian(Staff):

    def __init__(self, name, id, specialisation=None):
        super().__init__(name, id)
        self.__specialisation = specialisation
        self.__can_handle_animal = True

    def get_specialisation(self):
        return self.__specialisation

    def set_specialisation(self, specialisation):    # Set specialisation e.g. Mammal Veterinarian.
        if isinstance(specialisation, str):
            self.__specialisation = specialisation
        else:
            raise TypeError("Specialisation must be a string")

    def perform_health_check(self, animal):
        if isinstance(animal, Animal):
            print(
                f"{self.name} assessing the health of {animal.name}.\n"
                f"Health status: {animal.health} ({animal.check_health()})\n"
            )
        else:
            raise TypeError("Input must be of the type Animal")

    def administer_medication(self, animal):
        if isinstance(animal, Animal):
            health_increase = 25
            animal.set_health(health_increase)
            print(f"{self.name} administering medication to {animal.name}...\n")


class AnimalTrainer(Staff):

    def __init__(self, name, id):
        super().__init__(name, id)

    def train_animal(self, animal):
        if isinstance(animal, Animal):
            aggression_decrease = -20
            animal.set_aggression(aggression_decrease)
            print(f"{self.name} has trained {animal.name}.")


class Zookeeper(Staff):

    def __init__(self, name, id):
        super().__init__(name, id)

    def clean_enclosure(self, enclosure):    # Calls method which sets enclosure attribute is_clean to True.
        if isinstance(enclosure, Enclosure):
            enclosure.set_is_clean()
            print(f"{self.name} has cleaned {enclosure.name}.")
        else:
            raise TypeError("Must be of the type Enclosure.")

    def feed_animal(self, animal, units):    # Updates value for animal health and hunger attributes.
        if isinstance(animal, Animal):
            if isinstance(units, int):
                animal.set_hunger(units)
                animal.set_health(units / 2)    # Increase animal health count by 1/2 units of food given.
                print(f"{self.name} has feed {animal.name}.")
            else:
                raise TypeError("Value must be an integer.")
        else:
            raise TypeError("Must be of the type Animal.")

    def update_enclosure_temp(self, enclosure, temperature):    # Updates temperature for enclosures of type Aquarium or Terrarium.
        if isinstance(enclosure, Terrarium) or isinstance(enclosure, Aquarium):
            enclosure.set_temperature(temperature)
            print(f"{self.name} has updated the temperature for {enclosure.name}.")
        else:
            raise TypeError("Must be of type Terrarium or Aquarium.")

    def inspect_enclosure(self, enclosure):    # Checks if enclosure is set to clean, calls method to update animal health if False.
        if isinstance(enclosure, Enclosure):
            if enclosure.is_clean:
                print(f"{self.name} has found {enclosure.name} to be clean.")
            else:
                enclosure.decrease_animals_health()
                print(f"{enclosure.name} is not clean! Animals in {enclosure.name} have lost health.\n")
        else:
            raise TypeError("Must be of type Enclosure.")


class Administrator(Staff):
    def __init__(self, name, id):
        super().__init__(name, id)

    def generate_single_animal_report(self, animal):    # Takes an animal and generates a stats report.
        if isinstance(animal, Animal):
            print(f"{self.name} printing report...\n")
            if isinstance(animal, BigCat):
                print(BigCatReport.generate(animal))
            elif isinstance(animal, Monkey):
                print(MonkeyReport.generate(animal))
            else:
                print(HealthReport.generate(animal))
        else:
            raise TypeError("Input must be of the type Animal")

    def generate_enclosure_report(self, enclosure):
        if isinstance(enclosure, Enclosure):
            print(f"{self.name} printing report...\n")
            print(enclosure, "\n")
            enclosure.display_animals()

    def generate_staff_report(self, registry):
        if isinstance(registry, StaffRegistry):
            print(f"{self.name} printing report...\n")
            print(registry, "\n")

    def generate_all_animals_report(self, registry):
        if isinstance(registry, AnimalRegistry):
            print(f"{self.name} printing report...\n")
            print(registry, "\n")

    def generate_all_enclosure_report(self, registry):
        if isinstance(registry, EnclosureRegistry):
            print(f"{self.name} printing report...\n")
            print(registry, "\n")

    def approve_staff_leave(self, staff):    # Updates boolean for provided staff member to True.
        if isinstance(staff, Staff):
            staff.is_on_leave = True
            print(f"{self.name} approves leave for {staff.name}.")

    def update_staff_leave(self, staff):    # Updates boolean for provided staff member to False.
        if isinstance(staff, Staff):
            staff.is_on_leave = False
            print(f"{self.name} ends leave for {staff.name}.")

    def transfer_animal(self, animal, current_enclosure, target_enclosure): # Takes an animal and transfers it to a new enclosure.
        if not isinstance(animal, Animal):
            raise TypeError("Input must be of the type Animal")
        if not isinstance(current_enclosure, Enclosure):
            raise TypeError("Input must be of the type Enclosure")
        if not isinstance(target_enclosure, Enclosure):
            raise TypeError("Input must be of the type Enclosure")
        if animal.is_sick:    # Validates whether the animal is sick.
            print(f"Unable to move {animal.name} because they are sick.")
        else:    # If animal is not sick, remove them from existing enclosure and add them to new enclosure.
            current_enclosure.remove_animal(animal)
            target_enclosure.add_animal(animal)
            print(f"{self.name} successfully transferred {animal.name} to {current_enclosure.name}.")





