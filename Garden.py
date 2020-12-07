from Tree import Tree


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

        print(f"welcome to my harvest {self.name}")

    def soil(self):
        pass

    def add_tree(self, name, gender, species, height):
        new_tree = Tree(name, gender, species, height)
        self.plants.append(new_tree)


kin = Garden("joey")
kin.soil()


kin.add_tree("ki", "male", "oak", "98")
print(kin.plants)

# random_value = random.randint(0, self.max_damage)
#         return random_value
# def is_healthy(self):
#     print("The orchid flowers are blooming! 🌸🌸🌸")
