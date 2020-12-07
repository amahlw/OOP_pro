import random


class Plant:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def leaf(self, leaves):
        leaves_list = ["long", "short", "wide",
                       "round", "odd", "long_wide", "short_long"]
        self.leaves = leaves
        kj = random.choice(leaves_list)
        # jon = any(leaves_list)
        for i in kj:
            print(i, end="")

    def color(self, color="green"):
        foodz = ["Beez", "Flyz", "Catapillar", "Butterflies"]
        mj = random.choice(foodz)
        for i in mj:
            print(i, end="")


k = Plant("Lily", "female")
k.leaf("long")
k.color("yellow")
# print(__dict.Plant())
