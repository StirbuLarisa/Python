
class Column:
    """
    A column is a stack of pieces that are placed on the board.
    The column is responsible for keeping track of the pieces that are placed on it.
    It has the bounds of the triangle that it is placed on.

    :ivar column_stack: A list of pieces that are placed on the column.
    :vartype column_stack: list
    :ivar bounds: The bounds of the triangle that the column is placed on.
    :vartype bounds: pygame.Rect
    :ivar height: The height of the column.
    :vartype height: int

    """
    def __init__(self,bounds, height):
        self.column_stack = []
        self.bounds = bounds
        self.height = height


    def update_piece_bounds(self, column_index):

        """
        Updates the bounds of the pieces that are placed on the column.
        :param column_index: The index of the column.
        :return: None
        """

        index = 0
        for piece in self.column_stack:
            if column_index > 12:
                piece.bounds.x = self.bounds.x + (self.bounds.width - piece.bounds.width)/2
                piece.bounds.y = self.bounds.y + index * piece.bounds.height

            else:
                piece.bounds.x = self.bounds.x + (self.bounds.width - piece.bounds.width)/2
                piece.bounds.y = self.bounds.y + self.height - (index+1) * piece.bounds.height
            index += 1

    def is_clicked(self, mouse_pos):
        '''

        Checks if the column is clicked.
        :param mouse_pos: The position of the mouse.
        :type mouse_pos: tuple
        :return: True if the column is clicked, False otherwise.
        :rtype: bool

        '''
        return self.bounds.collidepoint(mouse_pos)
