from Tree import Tree
from Plant import Plant
from Flower import Flower
import random


class Garden:

    soil_level = 100

    def __init__(self, name, gender):
        self.name = name,
        # private gender
        self.__gender = gender
        self.plants = []

        print(f"welcome to my harvest {self.name}")

    @ classmethod
    def garden_soil(cls, amount):
        cls.soil_level -= int(amount)

        print(f"My new soil level is {cls.soil_level}")

    def add_tree(self, name, gender, species, height):
        new_tree = Tree(name, gender, species, height)
        self.plants.append(new_tree)

    def plant_kingdom(self):
        kingdom = ["Mosses/Liverworts", "Ferns", "Gymnosperms", "Angiosperms"]
        p_k = random.choice(kingdom)
        print(p_k)

    def is_healthy(self):
        print("This tree is wilting it's leaves... 🍃🍂")


# instances

brian = Garden("ars", "male")
brian.garden_soil(20)
brian.add_tree("ars", "male", " oak", 700)
brian.plant_kingdom()
brian.is_healthy()
