from Plant import Plant


class Flower(Plant):
    def __init__(self, name, type, petals, buds):
        super().__init__(name, type)
        self.petals = petals
        self.buds = buds
        print(
            f"I am a {self.name} which is a {self.type} with {self.petals} petals and {self.buds} buds")

    def leaf(self, leaves):
        self.leaves = leaves

        return (f" My leaves are: {self.leaves}")

    def color(self, color="green"):
        return (f"When I bloom i have {self.leaves} {color} leafs ")


ji = Flower("sunflower", "female", "yes", "orange")
ji.leaf("long")
ji.color("purple")
