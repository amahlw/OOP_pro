from Plant import Plant
import random


class Tree(Plant):
    tree_list = ["oaktree", "pinetree", "coconut tree"]
    tree_guest = ["birds", "lizards", "snakes"]

    def __init__(self, name, gender, species, height):
        super().__init__(name, gender)
        self.species = species
        self.height = int(height)

    def tree_type(self):
        tt = random.choice(Tree.tree_list)
        print(tt)

    def tree_family(self):
        tf = random.choice(Tree.tree_guest)
        print(f"This is an anomal who likes to eat me {tf}")


mb = Tree("Shawn", "male", "mjh", 98)
mb.tree_type()
mb.tree_family()
