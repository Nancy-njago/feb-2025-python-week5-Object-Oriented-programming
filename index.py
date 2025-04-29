# Base class
class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def describe(self):
        print(f"This is a {self.color} {self.name}. It tastes {self.taste}.")

    def eat(self):
        print(f"You take a bite of the {self.name}. Yum!")


# Inherited class
class CitrusFruit(Fruit):
    def __init__(self, name, color, taste, vitamin_c_content):
        super().__init__(name, color, taste)
        self.vitamin_c_content = vitamin_c_content  # extra attribute

    def describe(self):
        print(f"This is a {self.color} {self.name}. It's rich in Vitamin C ({self.vitamin_c_content}mg) and tastes {self.taste}!")

    def squeeze(self):
        print(f"You squeeze the {self.name} and get some refreshing juice!")


# Example usage
apple = Fruit("Apple", "Red", "sweet and crisp")
orange = CitrusFruit("Orange", "Orange", "sweet and tangy", 70)

apple.describe()
apple.eat()

print()

orange.describe()
orange.squeeze()

# Polymorphism Challenge (with Fruits and their Action)
# Base class
class Fruit:
    def prepare(self):
        print("Preparing the fruit...")

# Derived classes
class Apple(Fruit):
    def prepare(self):
        print("Slice the apple into pieces. 🍎")

class Banana(Fruit):
    def prepare(self):
        print("Peel the banana before eating. 🍌")

class Grape(Fruit):
    def prepare(self):
        print("Wash the grapes thoroughly. 🍇")


# Example usage
fruits = [Apple(), Banana(), Grape()]

for fruit in fruits:
    fruit.prepare()
