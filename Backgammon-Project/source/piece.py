import pygame

class Piece:
    def __init__(self, color):
        self.color = color
        self.image = pygame.image.load(f"../assets/{self.color}-piece.png")