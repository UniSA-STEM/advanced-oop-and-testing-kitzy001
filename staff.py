"""
File: staff.py
Description: This file contains the class Staff for my zoo program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal, BigCat, Monkey
from enclosure import Enclosure, Terrarium, Aquarium, Jungle
from report import HealthReport, BigCatReport, MonkeyReport


class Staff:

    def __init__(self, name, staff_id):
        """"
        Initialises an instance of the Staff class.

        Parameters:
            name (str): The name of the staff member.
            staff_id(str): The id of the staff member.
        """
        self.__name = name
        self.__id = staff_id
        self.__is_working = False
        self.__can_enrich_animal = False
        self.__is_on_leave = False

    def __str__(self):
        """
        Prints a string describing the staff member.
        """
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
    def can_enrich_animal(self):
        return self.__can_enrich_animal

    def enrich_animal(self, animal):
        """
        This method updates the attributes of an animal if the staff member is
        allowed to interact with the animal.

        Parameters:
            animal (Animal): The animal to enrich.
        """
        if isinstance(animal, Animal):
            if self.can_enrich_animal:
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
        """
        Setter for the attribute is_on_leave.

        Parameters:
            boolean (bool): True or False.
        """
        if isinstance(boolean, bool):
            self.__is_on_leave = boolean


class Veterinarian(Staff):

    def __init__(self, name, staff_id, specialisation=None):
        """"
        Initialises an instance of the Veterinarian class, subclass of Staff.

        Additional parameters:
            specialisation (Specialisation): The specialisation of the staff member.
        """
        super().__init__(name, staff_id)
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

    def __init__(self, name, staff_id):
        """"
        Initialises an instance of the AnimalTrainer class, subclass of Staff.
        """
        super().__init__(name, staff_id)
        self.__can_enrich_animal = True

    def train_animal(self, animal):
        if isinstance(animal, Animal):
            aggression_decrease = -20
            animal.set_aggression(aggression_decrease)
            print(f"{self.name} has trained {animal.name}.")


class Zookeeper(Staff):

    def __init__(self, name, staff_id):
        """"
        Initialises an instance of the ZooKeeper class, subclass of Staff.
        """
        super().__init__(name, staff_id)
        self.__can_enrich_animal = True

    def clean_enclosure(self, enclosure):
        """"
        This method takes an enclosure and sets it to clean.

        Parameters:
            enclosure (Enclosure): The enclosure for the staff member to clean.
        """
        if isinstance(enclosure, Enclosure):
            enclosure.set_is_clean(True)
            print(f"{self.name} has cleaned {enclosure.name}.")
        else:
            raise TypeError("Must be of the type Enclosure.")

    def feed_animal(self, animal, units):
        """"
        This method feeds an animal, updating the value for an animals hunger. The value for
        health is also updated by 0.5x the quantity of food.

        Parameters:
            animal (Animal): The animal to update.
            units (int): The units of food to feed to the animal.
        """
        if isinstance(animal, Animal):
            if isinstance(units, int):
                animal.set_hunger(units)
                animal.set_health(units / 2)
                print(f"{self.name} has feed {animal.name}.")
            else:
                raise TypeError("Value must be an integer.")
        else:
            raise TypeError("Must be of the type Animal.")

    def update_enclosure_temp(self, enclosure, temperature):
        """"
        This method updates an enclosures temperature if the enclosure is of the type
        Aquarium or Terrarium.

        Parameters:
            enclosure (Enclosure): The enclosure to update.
            temperature (int or float): The temperature to update.
        """
        if isinstance(enclosure, Terrarium) or isinstance(enclosure, Aquarium):
            enclosure.set_temperature(temperature)
            print(f"{self.name} has updated the temperature for {enclosure.name}.")
        else:
            raise TypeError("Must be of type Terrarium or Aquarium.")

    def update_jungle_weather(self, enclosure, boolean):
        """"
        This method updates the weather status of an enclosure of the type Jungle.

        Parameters:
            enclosure (Enclosure): The enclosure to update.
            boolean (bool): True or False.
        """
        if isinstance(enclosure, Jungle):
            enclosure.set_is_raining(boolean)
            print(f"{self.name} has updated the weather status for {enclosure.name}.")

    def inspect_enclosure(self, enclosure):
        """
        This method inspects an enclosure to see if it is clean, then calls another method to
        decrease animal health if the enclosure is found to not be clean.

        Parameters:
            enclosure (Enclosure): The enclosure to update.
        """
        if isinstance(enclosure, Enclosure):
            if enclosure.is_clean:
                print(f"{self.name} has found {enclosure.name} to be clean.")
            else:
                enclosure.decrease_animals_health()
                print(f"{enclosure.name} is not clean! Animals in {enclosure.name} have lost health.\n")
        else:
            raise TypeError("Must be of type Enclosure.")


class Administrator(Staff):

    def __init__(self, name, staff_id):
        """
        Initialises an instance of the Administrator class, subclass of Staff.
        Sets can_enrich_animal to false as Administrator cannot enrich an animal.
        """
        super().__init__(name, staff_id)
        self.__can_enrich_animal = False

    def generate_single_animal_report(self, animal):
        """
        Takes an animal and generates a statistics report.

        Parameters:
            animal (Animal): The animal to display the report for.
        """
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
        """
        Takes an enclosure and generates a report displaying the animals inside.

        Parameters:
            enclosure(Enclosure): The enclosure to display.
        """
        if isinstance(enclosure, Enclosure):
            print(f"{self.name} printing report...\n")
            print(enclosure, "\n")
            enclosure.display_animals()

    def generate_staff_report(self, registry):
        """
        Takes a staff registry and generates a statistics report.

        Parameters:
            registry(Registry): The staff registry to display.
        """
        from registry import StaffRegistry
        if isinstance(registry, StaffRegistry):
            print(f"{self.name} printing report...\n")
            print(registry, "\n")

    def generate_all_animals_report(self, registry):
        """
        Takes an animal registry and generates a report containing all animals in the zoo.

        Parameters:
            registry(Registry): The animal registry to display.
        """
        from registry import AnimalRegistry
        if isinstance(registry, AnimalRegistry):
            print(f"{self.name} printing report...\n")
            print(registry, "\n")

    def generate_all_enclosure_report(self, registry):
        """
        Takes an animal registry and generates a report containing all enclosures in the zoo.

        Parameters:
            registry(Registry): The enclosure registry to display.
        """
        from registry import EnclosureRegistry
        if isinstance(registry, EnclosureRegistry):
            print(f"{self.name} printing report...\n")
            print(registry, "\n")

    def approve_staff_leave(self, staff):
        """
        Takes a staff member and approves their leave, updating the boolean attribute for
        is_on_leave to True.

        Parameters:
            staff (Staff): The staff member to update.
        """
        if isinstance(staff, Staff):
            staff.is_on_leave = True
            print(f"{self.name} approves leave for {staff.name}.")

    def update_staff_leave(self, staff):
        """
        Takes a staff member and updates the boolean attribute for is_on_leave to False,
        for when they are back from leave.

        Parameters:
            staff (Staff): The staff member to update.
        """
        if isinstance(staff, Staff):
            staff.is_on_leave = False
            print(f"{self.name} ends leave for {staff.name}.")

    def transfer_animal(self, animal, current_enclosure, target_enclosure):
        """
        Takes an animal and transfers it to another enclosure within the zoo. Validates that the
        animal is not sick before transferring it to the new enclosure.

        Parameters:
            animal (Animal): The animal to transfer.
            current_enclosure (Enclosure): The enclosure to transfer from
            target_enclosure (Enclosure): The enclosure to transfer to.
        """
        if not isinstance(animal, Animal):
            raise TypeError("Input must be of the type Animal")
        if not isinstance(current_enclosure, Enclosure):
            raise TypeError("Input must be of the type Enclosure")
        if not isinstance(target_enclosure, Enclosure):
            raise TypeError("Input must be of the type Enclosure")
        if animal.is_sick:
            print(f"Unable to move {animal.name} because they are sick.")
        else:
            current_enclosure.remove_animal(animal)
            target_enclosure.add_animal_to_enclosure(animal)
            print(f"{self.name} successfully transferred {animal.name} to {current_enclosure.name}.")





