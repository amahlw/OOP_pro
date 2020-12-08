from Plant import Plant
import random


class Flower(Plant):
    flow_types = ["annuals", "perennials", "biennial"]
    shade_level = ["light", "partial", "dense", "full"]

    def __init__(self, name, gender, petals, buds):
        super().__init__(name, gender)
        self.petals = petals
        self.buds = buds
        print(
            f"I am a {self._name} which is a {self.gender} with {self.petals} petals and {self.buds} buds")

    def leaf(self, leaves):
        self.leaves = leaves
        leafy = random.choice(Flower.flow_types)
        print(leafy)

        return (f" My leaves are: {self.leaves}")

    def color(self, color="green"):
        colour = random.choice(Flower.shade_level)
        print(colour)
        return (f"When I bloom i have {self.leaves} {color} leafs ")

    def is_healthy(self):
        print(f"The flowers are blooming! 🌸🌸🌸")


ji = Flower("sunflower", "female", "yes", "orange")
ji.leaf("long")
ji.color("purple")
ji.is_healthy()
