from Plant import Plant
import random


class Tree(Plant):
    tree_list = ["oaktree", "pinetree", "coconut tree"]
    tree_guest = ["birds", "lizards", "snakes"]

    def __init__(self, name, gender, species, height):
        self.name = name
        self.gender = gender
        self.species = species
        self.height = int(height)

    def tree_type(self):
        tt = random.choice(Tree.tree_list)
        print(tt)

    def tree_family(self):
        tf = random.choice(Tree.tree_guest)
        print(tf)


mb = Tree("Shawn", "male", "mjh", 98)
mb.tree_type()
mb.tree_family()
