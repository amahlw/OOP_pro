class Plant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def leaf(self, leaves):
        self.leaves = leaves

        print(f" My leaves are: {self.leaves}")

    def color(self, color="green"):
        print(f"When I bloom my {self.leaves} leafs are {color} ")


k = Plant("Lily", "female")
k.leaf("long")
k.color("yellow")
# print(__dict.Plant())
