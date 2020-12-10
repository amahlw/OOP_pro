import random


class Plant():
    leaves_list = ["long", "short", "wide",
                   "round", "odd", "long_wide", "short_long"]
    foodz = ["Beez", "Flyz", "Catapillar", "Butterflies"]

    # ex
    # don't forget to add class att 1 or 2

    # make class methods to use in methods as well

    def __init__(self, name, gender):
        # private ex __  protected ex: _
        # also explain why att are pub,priv,prot

        self._name = name
        self.gender = gender


# instance methods

    def leaf(self):

        # self.leaves = leaves
        kj = random.choice(Plant.leaves_list)
        print(kj)

    def color(self, color="green"):

        mj = random.choice(Plant.foodz)
        print(mj)


#  instantiate

tony = Plant("lily", 30)
tony.leaf()
tony.color()
