import pygame

class Piece:
    def __init__(self, color):
        self.color = color
        img = pygame.image.load(f"../assets/{self.color}-piece.png")
        self.image = pygame.transform.scale(img, (img.get_width() * 0.4, img.get_height() * 0.4))
        self.bounds = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
