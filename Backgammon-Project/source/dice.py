import random
import pygame

class Dice:
    def __init__(self):
        self.sides = 6
        self.value = 1

    def roll(self):
        self.value = random.randint(1, self.sides)
        dice_face = pygame.image.load(f"../assets/dice-face-{self.value}.png")
        self.face = pygame.transform.scale(dice_face, (dice_face.get_width() * 0.5, dice_face.get_height() * 0.5))
