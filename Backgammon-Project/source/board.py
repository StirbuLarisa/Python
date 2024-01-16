import math

import pygame
from column import Column
from piece import Piece


class Board:
    """
    The board is the main component of the game.
    It is responsible for keeping track of the pieces that are placed on it.
    It also validates the moves that are made by the players, and computes the possible moves for each player.
    It
    """

    BG_COLOR = pygame.image.load("../assets/bg.jpg")
    BTN_COLOR = (0, 255, 0)

    def __init__(self):
        self.triangles = [[], []]
        self.triangles_bounds = [[], []]
        self.middle_line_width = 100
        self.columns = []

    def generate_board(self, screen):
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

        self.columns.append(Column(pygame.Rect(0, 0, 0, 0), 0))
        for index in range(1, 13):
            self.columns.append(Column(self.triangles_bounds[1][abs(12 - index)], self.triangle_height))
        for index in range(12):
            self.columns.append(Column(self.triangles_bounds[0][index], self.triangle_height))
        self.columns.append(Column(pygame.Rect(0, 0, 0, 0), 0))

    def init_board(self, screen):
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
        for index in range(1, len(self.columns) - 1):
            for piece in self.columns[index].column_stack:
                screen.blit(piece.image, (piece.bounds.x, piece.bounds.y))

    def handle_column_click(self, mouse_pos):

        for index in range(1, len(self.columns) - 1):
            if self.columns[index].bounds.collidepoint(mouse_pos):
                print(f"Clicked on column {index}")
                break

    def move_piece(self, current_column_index, new_column_index, screen):
        removed_piece = None
        piece = self.columns[current_column_index].column_stack.pop()

        if (len(self.columns[new_column_index].column_stack) == 1 and self.columns[new_column_index].column_stack[
            -1].color != piece.color):
            removed_piece = self.columns[new_column_index].column_stack.pop()
        self.columns[new_column_index].column_stack.append(piece)
        self.columns[current_column_index].update_piece_bounds(current_column_index)
        self.columns[new_column_index].update_piece_bounds(new_column_index)
        self.draw_board(screen)
        self.draw_pieces(screen)
        if removed_piece is not None:
            return removed_piece

    def current_column_is_empty(self, current_column_index):
        if len(self.columns[current_column_index].column_stack) == 0:
            return True
        else:
            return False

    def validate_player1_move(self, current_column_index, new_column_index, dice_values):

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
        for index in possible_moves:
            pygame.draw.rect(screen, (0, 255, 0), self.columns[index].bounds)
