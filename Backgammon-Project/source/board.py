import math

import pygame
from column import Column
from piece import Piece

class Board :

    BG_COLOR = pygame.image.load("../assets/bg.jpg")
    BTN_COLOR = (0, 255, 0)
    def __init__(self):
        self.triangles = [[],[]]
        self.triangles_bounds = [[],[]]
        self.middle_line_width = 100
        self.columns = []

    def generate_board(self,screen):
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
        self.y = (screen.get_height()/2 - self.triangle_height )/2
        self.x = (screen.get_width() - 12 * self.triangle_width-self.middle_line_width)/2

        for index in range (12):
            if index < 6:
                self.triangles_bounds[0].append(pygame.Rect(self.x + index * self.triangle_width, self.y, self.triangle_width, self.triangle_height))
                self.triangles_bounds[1].append(pygame.Rect(self.x + index * self.triangle_width, self.y+self.triangle_height + 100 , self.triangle_width, self.triangle_height))

            else:
                self.triangles_bounds[0].append(pygame.Rect(self.x + index * self.triangle_width + self.middle_line_width, self.y, self.triangle_width, self.triangle_height))
                self.triangles_bounds[1].append(pygame.Rect(self.x + index * self.triangle_width + self.middle_line_width, self.y+self.triangle_height + 100 , self.triangle_width, self.triangle_height))


        # roll_dice_btn = pygame.Rect(0, 0, 100, 50)
        # pygame.draw.rect(self.screen, self.BTN_COLOR, roll_dice_btn)

    def draw_board(self,screen):
        screen.blit(self.BG_COLOR, (0, 0))
        for index in range(12):
            if index < 6:
                screen.blit(self.triangles[0][index], (self.triangles_bounds[0][index].x, self.triangles_bounds[0][index].y))
                screen.blit(self.triangles[1][index], (self.triangles_bounds[1][index].x, self.triangles_bounds[1][index].y))
            else:
                screen.blit(self.triangles[0][index], (self.triangles_bounds[0][index].x, self.triangles_bounds[0][index].y))
                screen.blit(self.triangles[1][index], (self.triangles_bounds[1][index].x, self.triangles_bounds[1][index].y))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x +6*self.triangle_width +1, 0, self.middle_line_width, screen.get_height()))

    def assign_columns(self):
        for index in range(1,13):
            self.columns.append(Column(self.triangles_bounds[1][abs(12-index)], self.triangle_height))
        for index in range(12):
            self.columns.append(Column(self.triangles_bounds[0][index], self.triangle_height))

    def init_board(self,screen):
        self.generate_board(screen)
        self.draw_board(screen)
        self.assign_columns()

        self.columns[0].column_stack.extend([Piece("black"),Piece("black")])
        self.columns[0].update_piece_bounds(0)
        self.columns[11].column_stack.extend([Piece("black"), Piece("black"), Piece("black"), Piece("black")
                                                 , Piece("black")])
        self.columns[11].update_piece_bounds(11)
        self.columns[16].column_stack.extend([Piece("black"), Piece("black"), Piece("black")])
        self.columns[16].update_piece_bounds(16)
        self.columns[18].column_stack.extend([Piece("black"), Piece("black"), Piece("black"), Piece("black")
                                                 , Piece("black")])
        self.columns[18].update_piece_bounds(18)

        self.columns[23].column_stack.extend([Piece("white"), Piece("white")])
        self.columns[23].update_piece_bounds(23)
        self.columns[12].column_stack.extend([Piece("white"), Piece("white"), Piece("white"), Piece("white")
                                                 ,Piece("white")])
        self.columns[12].update_piece_bounds(12)
        self.columns[7].column_stack.extend([Piece("white"), Piece("white"), Piece("white")])
        self.columns[7].update_piece_bounds(7)
        self.columns[5].column_stack.extend([Piece("white"), Piece("white"), Piece("white"), Piece("white"),
                                             Piece("white")])
        self.columns[5].update_piece_bounds(5)

        self.draw_pieces(screen)

    def draw_pieces(self,screen):
        for column in self.columns:
            for piece in column.column_stack:
                screen.blit(piece.image, (piece.bounds.x, piece.bounds.y))

    def handle_column_click(self, mouse_pos):
        for index, column in enumerate(self.columns):
            if column.bounds.collidepoint(mouse_pos):
                print(f"Clicked on column {index}")
                break

    def move_piece(self, current_column_index, new_column_index,screen):
        removed_piece = []
        piece = self.columns[current_column_index].column_stack.pop()

        if(len(self.columns[new_column_index].column_stack) == 1 and self.columns[new_column_index].column_stack[-1].color != piece.color):
            removed_piece.append(self.columns[new_column_index].column_stack.pop())
        self.columns[new_column_index].column_stack.append(piece)
        self.columns[current_column_index].update_piece_bounds(current_column_index)
        self.columns[new_column_index].update_piece_bounds(new_column_index)
        self.draw_board(screen)
        self.draw_pieces(screen)
        if len(removed_piece) != 0:
            return removed_piece


    def draw_removed_pieces(self,screen,player):
        for index, piece in enumerate(player.removed_pieces):
            if piece.color == "black":
                screen.blit(piece.image, (self.x + 6 * self.triangle_width + self.middle_line_width + 10 + index * piece.bounds.width, 100))
            else:
                screen.blit(piece.image, (self.x + 6 * self.triangle_width + self.middle_line_width + 10 + (index-5) * piece.bounds.width, 200))

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
            if self.columns[new_column_index].column_stack[-1].color == self.columns[current_column_index].column_stack[
                -1].color:
                return True
        else:
            return False

    def validate_player2_move(self, current_column_index, new_column_index, dice_values):

        if current_column_index < new_column_index:
            if len(self.columns[new_column_index].column_stack) == 0:
                return True
            if len(self.columns[new_column_index].column_stack) == 1:
                return True
            if self.columns[new_column_index].column_stack[-1].color == self.columns[current_column_index].column_stack[
                -1].color:
                return True
        else:
            return False

    def validate_move(self, current_column_index, new_column_index, player, dice_values, distance):
        if player.color == "white":
            if distance in dice_values:
                if self.validate_player1_move(current_column_index, new_column_index, dice_values):
                    return True
        if player.color == "black":
            if distance in dice_values:
                if self.validate_player2_move(current_column_index, new_column_index, dice_values):
                    return True
        return False

    def all_in_house(self, player):
        if player.color == "white":
            for index in range(0,6):
                pass
        if player.color == "black":
            for index in range(18,23):
                pass






