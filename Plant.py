class Plant:
    def __init__(self, name):
        self.name = name

    def leaf(self, leaves):
        self.leaves = leaves

        print(f" My leaves are: {self.leaves}")

    def color(self, color="green"):
        # self.color = color
        print(f"When I bloom my {self.leaves} leafs are {self.color} ")


k = Plant("Lily")
k.leaf("long")
k.color("yellow")
# print(__dict.Plant())
