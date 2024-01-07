import math

import pygame
from column import Column
from piece import Piece

class Board :

    BG_COLOR = (255, 255, 255)
    BTN_COLOR = (0, 255, 0)
    def __init__(self):
        self.screen = pygame.display.set_mode((1920,1080))
        self.screen.fill(self.BG_COLOR)
        self.triangles = [[],[]]
        self.triangles_bounds = [[],[]]
        self.middle_line_width = 100
        self.columns = []

    def generate_board(self):
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
        self.y = (self.screen.get_height()/2 - self.triangle_height )/2
        self.x = (self.screen.get_width() - 12 * self.triangle_width-self.middle_line_width)/2

        for index in range (12):
            if index < 6:
                self.triangles_bounds[0].append(pygame.Rect(self.x + index * self.triangle_width, self.y, self.triangle_width, self.triangle_height))
                self.triangles_bounds[1].append(pygame.Rect(self.x + index * self.triangle_width, self.y+self.triangle_height + 100 , self.triangle_width, self.triangle_height))

            else:
                self.triangles_bounds[0].append(pygame.Rect(self.x + index * self.triangle_width + self.middle_line_width, self.y, self.triangle_width, self.triangle_height))
                self.triangles_bounds[1].append(pygame.Rect(self.x + index * self.triangle_width + self.middle_line_width, self.y+self.triangle_height + 100 , self.triangle_width, self.triangle_height))


        # roll_dice_btn = pygame.Rect(0, 0, 100, 50)
        # pygame.draw.rect(self.screen, self.BTN_COLOR, roll_dice_btn)

    def draw_board(self):
        self.screen.fill(self.BG_COLOR)
        for index in range(12):
            if index < 6:
                self.screen.blit(self.triangles[0][index], (self.triangles_bounds[0][index].x, self.triangles_bounds[0][index].y))
                self.screen.blit(self.triangles[1][index], (self.triangles_bounds[1][index].x, self.triangles_bounds[1][index].y))
            else:
                self.screen.blit(self.triangles[0][index], (self.triangles_bounds[0][index].x, self.triangles_bounds[0][index].y))
                self.screen.blit(self.triangles[1][index], (self.triangles_bounds[1][index].x, self.triangles_bounds[1][index].y))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.x +6*self.triangle_width +1, 0, self.middle_line_width, self.screen.get_height()))

    def assign_columns(self):
        for index in range(1,13):
            self.columns.append(Column(self.triangles_bounds[1][abs(12-index)], self.triangle_height))
        for index in range(12):
            self.columns.append(Column(self.triangles_bounds[0][index], self.triangle_height))

    def init_game(self):
        self.generate_board()
        self.draw_board()
        self.assign_columns()

        self.columns[0].column_stack.extend([Piece("black"),Piece("black")])
        self.columns[0].update_piece_bounds(0)
        self.columns[11].column_stack.extend([Piece("black"), Piece("black"), Piece("black"), Piece("black"), Piece("black")])
        self.columns[11].update_piece_bounds(11)
        self.columns[16].column_stack.extend([Piece("black"), Piece("black"), Piece("black")])
        self.columns[16].update_piece_bounds(16)
        self.columns[18].column_stack.extend([Piece("black"), Piece("black"), Piece("black"), Piece("black"), Piece("black")])
        self.columns[18].update_piece_bounds(18)

        self.columns[23].column_stack.extend([Piece("white"), Piece("white")])
        self.columns[23].update_piece_bounds(23)
        self.columns[12].column_stack.extend([Piece("white"), Piece("white"), Piece("white"), Piece("white"),Piece("white")])
        self.columns[12].update_piece_bounds(12)
        self.columns[7].column_stack.extend([Piece("white"), Piece("white"), Piece("white")])
        self.columns[7].update_piece_bounds(7)
        self.columns[5].column_stack.extend([Piece("white"), Piece("white"), Piece("white"), Piece("white"),
                                             Piece("white")])
        self.columns[5].update_piece_bounds(5)

        self.draw_pieces()


    def draw_pieces(self):
        for column in self.columns:
            for piece in column.column_stack:
                self.screen.blit(piece.image, (piece.bounds.x, piece.bounds.y))
    def handle_column_click(self, mouse_pos):
        for index, column in enumerate(self.columns):
            if column.bounds.collidepoint(mouse_pos):
                print(f"Clicked on column {index}")
                break

    def move_piece(self, current_column_index, new_column_index):
        print(self.columns[current_column_index].column_stack)
        piece = self.columns[current_column_index].column_stack.pop()
        print(self.columns[current_column_index].column_stack)
        self.columns[new_column_index].column_stack.append(piece)
        self.columns[current_column_index].update_piece_bounds(current_column_index)
        self.columns[new_column_index].update_piece_bounds(new_column_index)
        self.draw_board()
        self.draw_pieces()


