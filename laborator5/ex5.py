class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def make_sound(self):
        return "*sunet de mamifer*"

    def give_birth(self):
        return f"{self.name} is giving birth."

class Bird(Animal):
    def __init__(self, name, feather_color):
        super().__init__(name)
        self.feather_color = feather_color

    def make_sound(self):
        return "cip cirip"

    def lay_eggs(self):
        return f"{self.name} is laying eggs in the nest."

class Fish(Animal):
    def __init__(self, name, scale_color):
        super().__init__(name)
        self.scale_color = scale_color

    def make_sound(self):
        return "glugluglu"

    def lay_eggs(self):
        return f"{self.name} is laying eggs underwater."

mammal = Mammal("caine", "maro")
bird = Bird("papagal", "rosu")
fish = Fish("pestisor", "auriu")

print(mammal.make_sound())
print(mammal.give_birth())

print(bird.make_sound())
print(bird.lay_eggs())

print(fish.make_sound())
print(fish.lay_eggs())
