import pygame

class Piece:

    """
    A piece is a checker that is placed on the board.
    It has the color of the player that it belongs to.

    :ivar color: The color of the piece. It can be either "white" or "black".
    :vartype color: str
    :ivar image: The image of the piece.
    :vartype image: pygame.Surface
    :ivar bounds: The bounds of the piece.
    :vartype bounds: pygame.Rect

    """
    def __init__(self, color):
        self.color = color
        img = pygame.image.load(f"../assets/{self.color}-piece.png")
        self.image = pygame.transform.scale(img, (img.get_width() * 0.4, img.get_height() * 0.4))
        self.bounds = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
