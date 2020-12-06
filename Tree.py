from Plant import Plant


class Tree(Plant):

    def __init__(self, name, species, height):
        self.name = name
        self.species = species
        self.height = int(height)

    def greet(self):
        print(
            f"I/m a {self.name} with {self.species} and i stand {self.height}")


ti = Tree("kin", "oak", 10)
ti.greet()
