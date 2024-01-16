

class Player:

    """
    This class represents a player in the game. It is used to keep information about the player.

    :ivar type: The type of the player. It can be either "human" or "computer".
    :vartype type: str
    :ivar color: The color of the player. It can be either "white" or "black".
    :vartype color: str
    :ivar removed_pieces: The pieces that the player have been eaten from the board.
    :vartype removed_pieces: list
    :ivar home_pieces: The number of pieces that the player have in their home.
    :vartype home_pieces: int
    :ivar finished_pieces: The number of pieces that the player have finished.
    :vartype finished_pieces: int

    """
    def __init__(self, type, color):
        self.type = type
        self.color = color
        self.removed_pieces = []
        self.home_pieces = 0
        self.finished_pieces = 0
