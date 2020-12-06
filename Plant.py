class Plant:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def leaf(self, leaves):
        self.leaves = leaves

        print(f" My leaves are: {self.leaves}")

    def color(self, color="green"):
        print(f"When I bloom my {self.leaves} leafs are {color} ")
        food = ["rice", "meat", "bread"]

        for i in range(3):
            print(food[i], end=" "),


k = Plant("Lily", "female")
k.leaf("long")
k.color("yellow")
# print(__dict.Plant())
