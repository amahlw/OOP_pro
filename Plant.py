import random


class Plant:

    # ex

    # make class methods to use in methods as well

    def __init__(self, name, gender):
        # private ex __  protected ex: _
        # also explain why att are pub,priv,prot

        self._name = name
        self.gender = gender

    def leaf(self, leaves):
        leaves_list = ["long", "short", "wide",
                       "round", "odd", "long_wide", "short_long"]
        self.leaves = leaves
        kj = random.choice(leaves_list)
        # jon = any(leaves_list)
        print(kj)

    def color(self, color="green"):
        foodz = ["Beez", "Flyz", "Catapillar", "Butterflies"]
        mj = random.choice(foodz)
        print(mj)


#  instantiate
k = Plant("Lily", "female")
k.leaf("long")
k.color("yellow")
# print(__dict.Plant())
