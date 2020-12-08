from Plant import Plant


class Tree(Plant):

    def __init__(self, name, gender, species, height):
        self.name = name
        self.gender = gender
        self.species = species
        self.height = int(height)

    def greet(self):
        pass
