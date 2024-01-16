import random
import pygame


class Dice:

    """
    This class represents a die in the game. It is used to keep information about the dice and to roll it.

    :ivar dice_rect: The rectangle of the die.
    :vartype dice_rect: pygame.Rect
    :ivar face: The face of the die.
    :vartype face: pygame.Surface
    :ivar sides: The number of sides of the die.
    :vartype sides: int
    :ivar value: The value of the die.
    :vartype value: int

    """
    def __init__(self):
        self.dice_rect = None
        self.face = None
        self.sides = 6
        self.value = 1

    def roll(self):

        """
        Rolls the die and updates its value.
        :return: None
        """
        self.value = random.randint(1, self.sides)
        self.face = pygame.image.load(f"../assets/dice-face-{self.value}.png")
        self.face = pygame.transform.scale(self.face, (self.face.get_width() * 0.2, self.face.get_height() * 0.2))
        self.dice_rect = self.face.get_rect()
