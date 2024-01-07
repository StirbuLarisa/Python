import random
import pygame

class Dice:
    def __init__(self):
        self.sides = 6
        self.value = 1

    def roll(self):

        self.value = random.randint(1, self.sides)
        self.face = pygame.image.load(f"../assets/dice-face-{self.value}.png")
        self.face = pygame.transform.scale(self.face, (self.face.get_width() * 0.2, self.face.get_height() * 0.2))
        self.dice_rect = self.face.get_rect()
