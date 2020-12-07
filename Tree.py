from Plant import Plant


class Tree(Plant):

    def __init__(self, name, gender, species, height):
        self.name = name
        self.gender = gender
        self.species = species
        self.height = int(height)

    def greet(self):
        print(
            f"I/m a {self.name} with {self.species} and i stand {self.height}")

            


ti = Tree("kin", "female" "oak")
ti.greet()
