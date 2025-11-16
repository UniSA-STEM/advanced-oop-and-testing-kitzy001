""""
File: main.py
Description: This file acts as a space to demonstrate my working program.
Author: Zoe Kittel
ID: 110484404
Username: kitzy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Veterinarian, Zookeeper, AnimalTrainer, Administrator
from animal import Mammal, Reptile, MarineAnimal, BigCat, Monkey
from enclosure import Enclosure, Terrarium, Savannah, African, Aquarium, Jungle
from registry import StaffRegistry, AnimalRegistry, EnclosureRegistry
from exceptions import UnregisteredAnimal, EnclosureCapacityError, RequirementsError


# Setup Registry for Animals, Staff and Enclosures.

staff_reg = StaffRegistry("Zootopia - Staff")
animal_reg = AnimalRegistry("Zootopia - Animals")
enclosure_reg = EnclosureRegistry("Zootopia - Enclosure")

# Initialise some staff members through adding them to the staff directory.

vet = staff_reg.add_new("Val", Veterinarian)
animal_trainer = staff_reg.add_new("Tom", AnimalTrainer)
administrator = staff_reg.add_new("Ally", Administrator)
zookeeper = staff_reg.add_new("Zac", Zookeeper)

# Print staff member to demonstrate str method.

print(vet)

# Initialise some enclosures and add them to the enclosure registry.

jungle_1 = Jungle("Jagged Jungle", 10)
jungle_2 = Jungle("Warped Jungle", 5)
big_cat_savannah = African("Lions den", 3)
big_cat_plains = African("Lions plains", 5)
aquarium = Aquarium("Dolphins Delight", 5)
terrarium = Terrarium("Lizards Hideout", 3)

enclosure_reg.add_new(jungle_1)
enclosure_reg.add_new(jungle_2)
enclosure_reg.add_new(big_cat_savannah)
enclosure_reg.add_new(big_cat_plains)
enclosure_reg.add_new(aquarium)
enclosure_reg.add_new(terrarium)

# Print enclosure to demonstrate str method.

print(jungle_1)

# Initialise some animals and add them to the animal registry.

alex = BigCat("Alex", "lion", 5)
ben = BigCat("Ben", "lion", 5)
marcel = Monkey("Marcel", "monkey", 7)
maxine = Monkey("Maxine", "monkey", 2)
dolly = MarineAnimal("Dolly", "dolphin", 5)
lizzy = Reptile("Lizzy", "lizard", 5)

animal_reg.add_new(alex)
animal_reg.add_new(ben)
animal_reg.add_new(marcel)
animal_reg.add_new(maxine)
animal_reg.add_new(dolly)
animal_reg.add_new(lizzy)

# Print animal to demonstrate str method.

print(alex)

# Print animal registry to demonstrate str method.

print(animal_reg)

# Add animals to the appropriate enclosures.

big_cat_savannah.add_animal(alex)
big_cat_savannah.add_animal(ben)
jungle_1.add_animal(marcel)
jungle_1.add_animal(maxine)
aquarium.add_animal(dolly)
terrarium.add_animal(lizzy)

# Call enclosure display_animal() method to demonstrate animals have been appended to list.

jungle_1.display_animals()

# Call enclosure set_diet_for_all() to update diet for all animals.

jungle_1.set_diet_for_all("bananas")
big_cat_savannah.set_diet_for_all("raw beef")
aquarium.set_diet_for_all("fish")
terrarium.set_diet_for_all("crickets")

# Call staff method generate_staff_report() to generate a report of all staff registered at the zoo.

administrator.generate_staff_report(staff_reg)

# Call staff method to inspect_enclosure(), then call method to clean_enclosure() to set it to clean.

zookeeper.inspect_enclosure(jungle_1)
zookeeper.clean_enclosure(jungle_1)

# Call staff method to update the weather for enclosure to raining, use try except to demonstrate that the
#   argument should be of type Jungle.

try:
    zookeeper.update_jungle_weather(terrarium, True)
    print(f"{terrarium.name} has updated the weather status for {terrarium.name}.\n")
except TypeError as e:
    print (e)

# Corrected call to the method using jungle enclosure.

zookeeper.update_jungle_weather(jungle_1, True)

# Call staff method enrich_animal() to interact with animals, demonstrating that animals of the type Monkey will
#   not interact with a staff member if their enclosure is raining.

zookeeper.enrich_animal(marcel)
animal_trainer.enrich_animal(alex)

# Call BigCat method attack() to launch an attack on another animal, updating the target animals stats.
#   Call animals_attacked() method to retrieve list of animals attacked.

alex.attack(ben)
alex.print_animals_attacked()

# Call some animal methods, some of which unique to the subclass to update various attribute values
#   or print feedback to screen.

alex.explore()
ben.explore()
dolly.explore()
ben.cry()
lizzy.cry()
alex.provoke_visitor()
marcel.throw_banana()
maxine.steal_visitors_hat()

# Call Administrator method to transfer an animal into a new enclosure.

administrator.transfer_animal(marcel, jungle_1, jungle_2)

# Demonstrate trying to transfer an animal to an enclosure they should not belong to, using try/except.

try:
    administrator.transfer_animal(ben, big_cat_savannah, jungle_2)
    print(f"{ben.name} has been transferred!")
except TypeError as e:
    print (e)

# Try except demo. Instantiate an animal, then add them to enclosure without registering them first.
#   Demos custom exception for UnregisteredAnimal.

animal = BigCat("Alex", "lion", 6)
try:
    big_cat_savannah.add_animal(animal)
    print(f"{animal.name} added successfully!")
except UnregisteredAnimal as e:
    print(e)
except EnclosureCapacityError as e:
    print(e)

# Demonstrate staff member running a health report for an animal after it has attacked another, demonstrating
#   an increase in aggression level and rating.

alex.attack(ben)
administrator.generate_single_animal_report(alex)

# Demonstrate a staff of the type Veterinarian healing an animal to increase their health by 30.

print(alex.health)
vet.administer_medication(alex)
print(alex.health)

# Demonstrate a staff of the type Zookeeper trying to feed an animal of the type MarineAnimal without
#   first learning how to swim.

try:
    zookeeper.feed_animal(dolly, 20)
    print(f"{dolly.name} fed successfully!")
except RequirementsError as e:
    print(e)

# Get staff member to learn to swim then re-try feeding the MarineAnimal.

zookeeper.learn_to_swim()
zookeeper.feed_animal(dolly, 20)

# Demonstrate a staff of the type AnimalTrainer to train an animal, thereby reducing its aggression level by -20.

animal_trainer.train_animal(alex)
animal_trainer.train_animal(alex)
vet.administer_medication(alex)
print(alex.aggression)
print(alex.health)

# Animal should now be eligible for transfer.

administrator.transfer_animal(alex, big_cat_savannah, big_cat_plains)

# Demo of unit tests- to run tests in terminal: pytest test_*.py -v.
