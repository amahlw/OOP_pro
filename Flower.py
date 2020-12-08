from Plant import Plant


class Flower(Plant):

    def __init__(self, name, gender, petals, buds):
        super().__init__(name, gender)
        self.petals = petals
        self.buds = buds
        print(
            f"I am a {self._name} which is a {self.gender} with {self.petals} petals and {self.buds} buds")

    def leaf(self, leaves):
        self.leaves = leaves

        return (f" My leaves are: {self.leaves}")

    def color(self, color="green"):
        return (f"When I bloom i have {self.leaves} {color} leafs ")

    def is_healthy(self):
        print(f"The flowers are blooming! 🌸🌸🌸")


# ji = Flower("sunflower", "female", "yes", "orange")
# ji.leaf("long")
# ji.color("purple")
# ji.is_healthy()
