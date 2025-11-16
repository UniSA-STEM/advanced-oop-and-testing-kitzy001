"""
File: staff.py
Description: This file contains the class Staff for my zoo program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal, BigCat, Monkey, MarineAnimal
from enclosure import Enclosure, Terrarium, Aquarium, Jungle
from report import HealthReport, BigCatReport, MonkeyReport
from exceptions import RequirementsError

class Staff:

    def __init__(self, name, staff_id):
        """
        Initialises an instance of the Staff class.

        Parameters:
            name (str): The name of the staff member.
            staff_id(str): The id of the staff member.
        """
        self._name = name
        self._id = staff_id
        self._is_working = False
        self._can_enrich_animal = False
        self._is_on_leave = False
        self._can_swim = False

    def __str__(self):
        """
        Prints a string describing the staff member.
        """
        return(
            f"Staff name: {self.name}\n"
            f"ID: {self._id}\n"
            f"Specialisation: {self.__class__.__name__}\n"
        )

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def can_enrich_animal(self):
        return self._can_enrich_animal

    @property
    def can_swim(self):
        return self._can_swim

    def enrich_animal(self, animal):
        """
        This method updates the attributes of an animal if the staff member is
        allowed to interact with the animal.

        Parameters:
            animal (Animal): The animal to enrich.
        """
        if isinstance(animal, Animal):
            if isinstance(animal, MarineAnimal) and not self.can_swim:
                raise RequirementsError(self.name)
            if self.can_enrich_animal:
                interacted = animal.respond_to_zookeeper()
                if interacted is True:
                    print(f"{self.name} enriched {animal.name}.\n")
            else:
                print(f"{self.name} is not able to interact with {animal.name} due to their role.\n")
        else:
            raise ValueError("Animal must be of type Animal.\n")

    def clock_in(self):
        self._is_working = True

    def clock_out(self):
        self._is_working = False

    def set_is_on_leave(self, boolean):
        """
        Setter for the attribute is_on_leave.

        Parameters:
            boolean (bool): True or False.
        """
        if isinstance(boolean, bool):
            self._is_on_leave = boolean
        else:
            raise ValueError("Must enter True or False.\n")

    def learn_to_swim(self):
        self._can_swim = True

class Veterinarian(Staff):

    def __init__(self, name, staff_id, skill_level=0):
        """"
        Initialises an instance of the Veterinarian class, subclass of Staff.

        Additional parameters:
            skill_level (int): The skill level of the veterinarian
        """
        super().__init__(name, staff_id)
        self.__skill_level = skill_level
        self._can_handle_animal = True

    @property
    def skill_level(self):
        return self.__skill_level

    def increase_skill_level(self):
        """"
        This method increases the value for the staff members skill level by 1.
        """
        self.__skill_level += 1

    def perform_health_check(self, animal):
        """"
        This method takes an animal and performs a health check on them, printing the
        results to the screen. This increases the staffs skill level by 1. Also Validates that the
        staff member can swim if the animal of the type MarineAnimal before performing the action.
        """
        if isinstance(animal, Animal):
            if isinstance(animal, MarineAnimal) and not self.can_swim:
                raise RequirementsError(self.name)
            print(
                f"{self.name} assessing the health of {animal.name}.\n"
                f"Health status: {animal.health} ({animal.check_health()})\n"
            )
            self.increase_skill_level()
        else:
            raise TypeError("Input must be of the type Animal.\n")

    def administer_medication(self, animal):
        """"
        This method takes an animal and updates the health value. Increases staff skill level by 1.
        Also validates that the staff member can swim, if the animal is of the type MarineAnimal,
        before performing the action.
        """
        if isinstance(animal, Animal):
            if isinstance(animal, MarineAnimal) and not self.can_swim:
                raise RequirementsError(self.name)
            health_increase = 30
            animal.set_health(health_increase)
            print(f"{self.name} administering medication to {animal.name}...\n")
            self.increase_skill_level()
        else:
            raise TypeError("Input must be of the type Animal.\n")


class AnimalTrainer(Staff):

    def __init__(self, name, staff_id):
        """
        Initialises an instance of the AnimalTrainer class, subclass of Staff.
        """
        super().__init__(name, staff_id)
        self._can_enrich_animal = True

    def train_animal(self, animal):
        """"
        This method takes an animal, validates it is of the type Animal, and trains the animal,
        decreasing their aggression level by 20.
        Also validates if the staff member can swim, if the animal is of the instance MarineAnimal,
        raises an exception if the staff member cannot swim.

        Parameters:
            animal (Animal): The animal to train.
        """
        if isinstance(animal, Animal):
            if isinstance(animal, MarineAnimal) and not self.can_swim:
                raise RequirementsError(self.name)
            else:
                aggression_decrease = -20
                animal.set_aggression(aggression_decrease)
                print(f"{self.name} has trained {animal.name}.\n")
        else:
            raise TypeError("Input must be of the type Animal.\n")


class Zookeeper(Staff):

    def __init__(self, name, staff_id):
        """"
        Initialises an instance of the ZooKeeper class, subclass of Staff.
        """
        super().__init__(name, staff_id)
        self._can_enrich_animal = True

    def clean_enclosure(self, enclosure):
        """"
        This method takes an enclosure and sets it to clean.
        Validates that user can swim if the enclosure is of the type Aquarium.

        Parameters:
            enclosure (Enclosure): The enclosure for the staff member to clean.
        """
        if isinstance(enclosure, Enclosure):
            if isinstance(enclosure, Aquarium) and not self.can_swim:
                raise RequirementsError(self.name)
            else:
                enclosure.set_is_clean(True)
                print(f"{self.name} has cleaned {enclosure.name}.\n")
        else:
            raise TypeError("Must be of the type Enclosure.\n")

    def feed_animal(self, animal, units):
        """"
        This method feeds an animal, updating the value for an animals hunger. The value for
        health is also updated by 0.5x the quantity of food.
        Validates that staff member can swim before performing the action, if the animal is of
        the type MarineAnimal.

        Parameters:
            animal (Animal): The animal to update.
            units (int): The units of food to feed to the animal.
        """
        if isinstance(animal, Animal):
            if isinstance(animal, MarineAnimal) and not self.can_swim:
                raise RequirementsError(self.name)
            if isinstance(units, int):
                animal.set_hunger(units)
                animal.set_health(int(units / 2))
                print(f"{self.name} has feed {animal.name}.\n")
            else:
                raise TypeError("Value must be an integer.\n")
        else:
            raise TypeError("Must be of the type Animal.\n")

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
            print(f"{self.name} has updated the temperature for {enclosure.name}.\n")
        else:
            raise TypeError("Must be of type Terrarium or Aquarium.\n")

    def update_jungle_weather(self, enclosure, boolean):
        """"
        This method updates the weather status of an enclosure of the type Jungle.

        Parameters:
            enclosure (Enclosure): The enclosure to update.
            boolean (bool): True or False.
        """
        if isinstance(enclosure, Jungle):
            enclosure.set_is_raining(boolean)
            print(f"{self.name} has updated the weather status for {enclosure.name}.\n")
        else:
            raise TypeError("Must be of type Jungle.\n")

    def inspect_enclosure(self, enclosure):
        """
        This method inspects an enclosure to see if it is clean, then calls another method to
        decrease animal health if the enclosure is found to not be clean.
        Validates that staff member can swim before performing the action, if the enclosure is of
        the type Aquarium.

        Parameters:
            enclosure (Enclosure): The enclosure to update.
        """
        if isinstance(enclosure, Enclosure):
            if isinstance(enclosure, Aquarium) and not self.can_swim:
                raise RequirementsError(self.name)
            if enclosure.is_clean:
                 print(f"{self.name} has found {enclosure.name} to be clean.\n")
            else:
                enclosure.decrease_animals_health()
                print(f"{enclosure.name} is not clean! Animals in {enclosure.name} have lost health as a result.\n")
        else:
            raise TypeError("Must be of type Enclosure.\n")


class Administrator(Staff):

    def __init__(self, name, staff_id):
        """
        Initialises an instance of the Administrator class, subclass of Staff.
        Sets can_enrich_animal to false as Administrator cannot enrich an animal.
        """
        super().__init__(name, staff_id)
        self._can_enrich_animal = False

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
            raise TypeError("Input must be of the type Animal.\n")

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
        else:
            raise TypeError("Input must be of the type Enclosure.\n")

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
        else:
            raise TypeError("Input must be of the type StaffRegistry.\n")

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
        else:
            raise TypeError("Input must be of the type AnimalRegistry.\n")

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
        else:
            raise TypeError("Input must be of the type EnclosureRegistry.\n")

    def approve_staff_leave(self, staff):
        """
        Takes a staff member and approves their leave, updating the boolean attribute for
        is_on_leave to True.

        Parameters:
            staff (Staff): The staff member to update.
        """
        if isinstance(staff, Staff):
            staff.is_on_leave = True
            print(f"{self.name} approves leave for {staff.name}.\n")
        else:
            raise TypeError("Input must be of the type Staff.\n")

    def update_staff_leave(self, staff):
        """
        Takes a staff member and updates the boolean attribute for is_on_leave to False,
        for when they are back from leave.

        Parameters:
            staff (Staff): The staff member to update.
        """
        if isinstance(staff, Staff):
            staff.is_on_leave = False
            print(f"{self.name} ends leave for {staff.name}.\n")
        else:
            raise TypeError("Input must be of the type Staff.\n")

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
            raise TypeError("Input must be of the type Animal.\n")
        if not isinstance(current_enclosure, Enclosure):
            raise TypeError("Input must be of the type Enclosure.\n")
        if not isinstance(target_enclosure, Enclosure):
            raise TypeError("Input must be of the type Enclosure.\n")
        if animal.fit_for_transfer() is False:
            print(f"Unable to move {animal.name} due to their health and/or behaviour. Run a report for more info.\n")
        else:
            current_enclosure.remove_animal(animal)
            target_enclosure.add_animal_to_enclosure(animal)
            print(f"{self.name} successfully transferred {animal.name} to {target_enclosure.name}.\n")






