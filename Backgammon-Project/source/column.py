
class Column:
    def __init__(self,bounds, height):
        self.column_stack = []
        self.bounds = bounds
        self.height = height


    def update_piece_bounds(self, column_index):
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
        return self.bounds.collidepoint(mouse_pos)
