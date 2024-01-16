import math

import pygame
from column import Column
from piece import Piece


class Board:
    """
    The board is the main component of the game.
    It is responsible for keeping track of the pieces that are placed on it.
    It also validates the moves that are made by the players, and computes the possible moves for each player.
    It draws the board and the pieces on the screen.

    :ivar x: The x coordinate of the board.
    :vartype x: int
    :ivar y: The y coordinate of the board.
    :vartype y: int
    :ivar triangle_height: The height of the triangle corresponding to the column.
    :vartype triangle_height: int
    :ivar triangle_width: The width of the triangle corresponding to the column.
    :vartype triangle_width: int
    :ivar triangles: A list of lists of the triangles that are placed on the board.
    :vartype triangles: list
    :ivar triangles_bounds: A list of lists of the bounds of the triangles that are placed on the board.
    :vartype triangles_bounds: list
    :ivar middle_line_width: The width of the middle line that separates the board.
    :vartype middle_line_width: int
    :ivar columns: A list of columns that are placed on the board.
    :vartype columns: list
    
    """

    BG_COLOR = pygame.image.load("../assets/bg.jpg")
    BTN_COLOR = (0, 255, 0)

    def __init__(self):
        self.x = None
        self.y = None
        self.triangle_height = None
        self.triangle_width = None
        self.triangles = [[], []]
        self.triangles_bounds = [[], []]
        self.middle_line_width = 100
        self.columns = []

    def generate_board(self, screen):
        """
        Generates the board. It creates the triangles and init the bounds of the triangles.
        :param screen: The screen of the game.
        :type screen: pygame.Surface
        :return: None
        """
        up_light_triangle = pygame.image.load("../assets/light-up-row-triangle.png")
        up_dark_triangle = pygame.image.load("../assets/dark-up-row-triangle.png")
        down_light_triangle = pygame.image.load("../assets/light-down-row-triangle.png")
        down_dark_triangle = pygame.image.load("../assets/dark-down-row-triangle.png")
        for row in range(2):
            for col in range(12):
                if row == 0:
                    if col % 2 == 0:
                        self.triangles[row].append(pygame.transform.scale(up_dark_triangle, (
                            up_dark_triangle.get_width() * 0.4, up_dark_triangle.get_height() * 0.4)))
                    else:
                        self.triangles[row].append(pygame.transform.scale(up_light_triangle, (
                            up_light_triangle.get_width() * 0.4, up_light_triangle.get_height() * 0.4)))
                if row == 1:
                    if col % 2 == 0:
                        self.triangles[row].append(pygame.transform.scale(down_light_triangle, (
                            down_light_triangle.get_width() * 0.4, down_light_triangle.get_height() * 0.4)))
                    else:
                        self.triangles[row].append(pygame.transform.scale(down_dark_triangle, (
                            down_dark_triangle.get_width() * 0.4, down_dark_triangle.get_height() * 0.4)))

        self.triangle_width = self.triangles[0][0].get_width()
        self.triangle_height = self.triangles[0][0].get_height()
        self.y = (screen.get_height() / 2 - self.triangle_height) / 2
        self.x = (screen.get_width() - 12 * self.triangle_width - self.middle_line_width) / 2

        for index in range(12):
            if index < 6:
                self.triangles_bounds[0].append(
                    pygame.Rect(self.x + index * self.triangle_width, self.y, self.triangle_width,
                                self.triangle_height))
                self.triangles_bounds[1].append(
                    pygame.Rect(self.x + index * self.triangle_width, self.y + self.triangle_height + 100,
                                self.triangle_width, self.triangle_height))

            else:
                self.triangles_bounds[0].append(
                    pygame.Rect(self.x + index * self.triangle_width + self.middle_line_width, self.y,
                                self.triangle_width, self.triangle_height))
                self.triangles_bounds[1].append(
                    pygame.Rect(self.x + index * self.triangle_width + self.middle_line_width,
                                self.y + self.triangle_height + 100, self.triangle_width, self.triangle_height))

    def draw_board(self, screen):
        """
        Draws the board on the screen.
        :param screen: The screen of the game.
        :type screen: pygame.Surface
        :return: None
        """
        screen.blit(self.BG_COLOR, (0, 0))
        for index in range(12):
            if index < 6:
                screen.blit(self.triangles[0][index],
                            (self.triangles_bounds[0][index].x, self.triangles_bounds[0][index].y))
                screen.blit(self.triangles[1][index],
                            (self.triangles_bounds[1][index].x, self.triangles_bounds[1][index].y))
            else:
                screen.blit(self.triangles[0][index],
                            (self.triangles_bounds[0][index].x, self.triangles_bounds[0][index].y))
                screen.blit(self.triangles[1][index],
                            (self.triangles_bounds[1][index].x, self.triangles_bounds[1][index].y))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x + 6 * self.triangle_width + 1, 0, self.middle_line_width,
                                                        screen.get_height()))

    def assign_columns(self):
        """
        Assigns the columns to the board.
        :return: None
        """

        self.columns.append(Column(pygame.Rect(0, 0, 0, 0), 0))
        for index in range(1, 13):
            self.columns.append(Column(self.triangles_bounds[1][abs(12 - index)], self.triangle_height))
        for index in range(12):
            self.columns.append(Column(self.triangles_bounds[0][index], self.triangle_height))
        self.columns.append(Column(pygame.Rect(0, 0, 0, 0), 0))

    def init_board(self, screen):
        """
        Initializes the board. It generates the board, draws it on the screen and assigns the columns to the board.
        It also draws the pieces on the screen.
        :param screen: The screen of the game.
        :type screen: pygame.Surface
        :return: None
        """
        self.generate_board(screen)
        self.draw_board(screen)
        self.assign_columns()

        var = None
        print(var)

        for index in range(len(self.columns)):
            print(f"Column {index} has {self.columns[index].bounds} bounds")

        self.columns[1].column_stack.extend([Piece("black"), Piece("black")])
        self.columns[1].update_piece_bounds(1)
        self.columns[12].column_stack.extend([Piece("black"), Piece("black"), Piece("black"), Piece("black")
                                                 , Piece("black")])
        self.columns[12].update_piece_bounds(12)
        self.columns[17].column_stack.extend([Piece("black"), Piece("black"), Piece("black")])
        self.columns[17].update_piece_bounds(17)
        self.columns[19].column_stack.extend([Piece("black"), Piece("black"), Piece("black"), Piece("black")
                                                 , Piece("black")])
        self.columns[19].update_piece_bounds(19)

        self.columns[24].column_stack.extend([Piece("white"), Piece("white")])
        self.columns[24].update_piece_bounds(24)
        self.columns[13].column_stack.extend([Piece("white"), Piece("white"), Piece("white"), Piece("white")
                                                 , Piece("white")])
        self.columns[13].update_piece_bounds(13)
        self.columns[8].column_stack.extend([Piece("white"), Piece("white"), Piece("white")])
        self.columns[8].update_piece_bounds(8)
        self.columns[6].column_stack.extend([Piece("white"), Piece("white"), Piece("white"), Piece("white"),
                                             Piece("white")])
        self.columns[6].update_piece_bounds(6)

        self.draw_pieces(screen)

    def draw_pieces(self, screen):
        """
        Draws the pieces on the screen.
        :param screen: The screen of the game.
        :type screen: pygame.Surface
        :return: None
        """
        for index in range(1, len(self.columns) - 1):
            for piece in self.columns[index].column_stack:
                screen.blit(piece.image, (piece.bounds.x, piece.bounds.y))

    def handle_column_click(self, mouse_pos):
        """
        Handles the click on a column.
        :param mouse_pos: The position of the mouse.
        :type mouse_pos: tuple
        :return:
        """

        for index in range(1, len(self.columns) - 1):
            if self.columns[index].bounds.collidepoint(mouse_pos):
                print(f"Clicked on column {index}")
                break

    def move_piece(self, current_column_index, new_column_index, screen):
        """
        Moves a piece from a column to another column. It also updates the bounds of the pieces that are placed.
        It changes the column that the piece belongs to. It adds the piece to the new column and removes it from the
        current column. It checks if a piece is removed from the board and treats it accordingly.
        :param current_column_index: The index of the column that the piece is currently placed on.
        :type current_column_index: int
        :param new_column_index: The index of the column that the piece will be placed on.
        :type new_column_index: int
        :param screen: The screen of the game.
        :return: The piece that is removed from the board (if it is removed)
        :rtype: Piece or None
        """
        removed_piece = None
        piece = self.columns[current_column_index].column_stack.pop()

        if (len(self.columns[new_column_index].column_stack) == 1 and 
                self.columns[new_column_index].column_stack[-1].color != piece.color):
            removed_piece = self.columns[new_column_index].column_stack.pop()
        self.columns[new_column_index].column_stack.append(piece)
        self.columns[current_column_index].update_piece_bounds(current_column_index)
        self.columns[new_column_index].update_piece_bounds(new_column_index)
        self.draw_board(screen)
        self.draw_pieces(screen)
        if removed_piece is not None:
            return removed_piece

    def current_column_is_empty(self, current_column_index):
        """
        Checks if the current column is empty.
        :param current_column_index: The index of the current column.
        :type current_column_index: int
        :return: True if the current column is empty, False otherwise.
        :rtype: bool
        """
        if len(self.columns[current_column_index].column_stack) == 0:
            return True
        else:
            return False

    def validate_player1_move(self, current_column_index, new_column_index, dice_values):
        """
        Validates the move of player 1. It checks if the move is valid, that the move is done in clockwise direction.
        :param current_column_index: The index of the column that the piece is currently placed on.
        :type current_column_index: int
        :param new_column_index: The index of the column that the piece will be placed on.
        :type new_column_index: int
        :return: True if the move is valid, False otherwise.
        :rtype: bool
        """

        if current_column_index > new_column_index:
            if len(self.columns[new_column_index].column_stack) == 0:
                return True
            if len(self.columns[new_column_index].column_stack) == 1:
                return True
            if (self.columns[new_column_index].column_stack[-1].color ==
                    self.columns[current_column_index].column_stack[-1].color):
                return True
        else:
            return False

    def validate_player2_move(self, current_column_index, new_column_index, dice_values):
        """
        Validates the move of player 2. It checks if the move is valid, that the move is done in anti-clockwise direction.
        :param current_column_index: The index of the column that the piece is currently placed on.
        :type current_column_index: int
        :param new_column_index: The index of the column that the piece will be placed on.
        :type new_column_index: int
        :return: True if the move is valid, False otherwise.
        :rtype: bool
        """
        if current_column_index < new_column_index:
            if len(self.columns[new_column_index].column_stack) == 0:
                return True
            if len(self.columns[new_column_index].column_stack) == 1:
                return True
            if (self.columns[new_column_index].column_stack[-1].color ==
                    self.columns[current_column_index].column_stack[-1].color):
                return True
        else:
            return False

    def validate_move(self, current_column_index, new_column_index, player, dice_values, distance):
        """
        Validates the move. It checks if the move is valid. This function is used to validate the moves of both players.
        :param current_column_index: The index of the column that the piece is currently placed on.
        :type current_column_index: int
        :param new_column_index: The index of the column that the piece will be placed on.
        :type new_column_index: int
        :param player: The player that makes the move.
        :type player: Player
        :param dice_values: The values of the dice.
        :type dice_values: list
        :param distance: The distance between the current column and the new column.
        :type distance: int
        :return: True if the move is valid, False otherwise.
        :rtype: bool
        """
        if self.current_column_is_empty(
                current_column_index) and current_column_index != 0 and current_column_index != 25:
            return False
        if player.color == "white":
            if distance in dice_values:
                if self.validate_player1_move(current_column_index, new_column_index, dice_values):
                    return True
        if player.color == "black":
            if distance in dice_values:
                if self.validate_player2_move(current_column_index, new_column_index, dice_values):
                    return True
        return False

    def draw_removed_pieces(self, screen, player):
        """
        Draws the pieces that are removed from the board, the player's eaten pieces.
        :param screen: The screen of the game.
        :type screen: pygame.Surface
        :param player: The player whose pieces are eaten from the board.
        :type player: Player
        :return: None
        """
        index = 0
        for piece in player.removed_pieces:
            img = pygame.transform.scale(piece.image, (piece.image.get_width() * 0.7, piece.image.get_height() * 0.7))
            if player.color == "black":
                screen.blit(img, (
                    (self.x + 6 * self.triangle_width + 1) + self.middle_line_width / 2 - img.get_width() / 2,
                    screen.get_height() / 2 - piece.bounds.height - index * img.get_height()))
            else:
                screen.blit(img, (
                    (self.x + 6 * self.triangle_width + 1) + self.middle_line_width / 2 - img.get_width() / 2,
                    screen.get_height() / 2 + index * img.get_height()))
            index += 1

    def compute_possible_moves(self, player, dice_values, current_column_index=None):
        """
        Computes the possible moves for a player. It checks if the player has pieces that are eaten from the board.
        If the player has pieces that are eaten from the board, it computes the possible moves for the player to
        place the pieces on the board. If the player has no pieces that are eaten from the board, it computes the
        possible moves for the player to move the pieces on the board.

        :param player: The player whose possible moves are computed.
        :type player: Player
        :param dice_values: The values of the dice.
        :type dice_values: list
        :param current_column_index: The index of the column that the piece is currently placed on.
        :type current_column_index: int
        :return: A list of the possible moves.
        :rtype: list
        """
        possible_moves = []

        if len(player.removed_pieces) == 0:
            for index in range(1, 25):
                if self.validate_move(current_column_index, index, player, dice_values,
                                      abs(current_column_index - index)):
                    possible_moves.append(index)
        else:
            if player.color == "white":
                for index in range(19, 25):
                    if self.validate_move(25, index, player, dice_values, abs(25 - index)):
                        possible_moves.append(index)
            if player.color == "black":
                for index in range(1, 7):
                    if self.validate_move(0, index, player, dice_values, index):
                        possible_moves.append(index)
        return possible_moves

    def draw_possible_moves(self, screen, possible_moves):
        """
        Draws the possible moves on the screen. It draws a green rectangle near the column that the piece can be placed on.
        :param screen: The screen of the game.
        :type screen: pygame.Surface
        :param possible_moves: A list of the possible moves.
        :type possible_moves: list
        :return: None
        """
        for index in possible_moves:

            if index < 13:
                rect = pygame.Rect(self.columns[index].bounds.x,
                                   self.columns[index].bounds.y + self.columns[index].bounds.height + 10,
                                   self.columns[index].bounds.width, 7)
                pygame.draw.rect(screen, (0, 255, 0), rect)
            else:
                rect = pygame.Rect(self.columns[index].bounds.x,
                                   self.columns[index].bounds.y  - 10,
                                   self.columns[index].bounds.width, 7)
                pygame.draw.rect(screen, (0, 255, 0), rect)

