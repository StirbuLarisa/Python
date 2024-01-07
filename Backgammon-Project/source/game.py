import sys

import pygame

from player import Player
from dice import Dice

class Game:
    def __init__(self, board):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.board = board
        self.player1 = None
        self.player2 = None
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.roll_dice_button = None
        self.roll_dice_button_rect = None
        self.dice_values = []

    def init_game(self):
        self.board.init_board(self.screen)
        self.player1 = Player("human", "white")
        self.player2 = Player("human", "black")

    def play(self):
        current_player = self.player1
        self.draw_roll_dice_button()

        selected_column = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.board.handle_column_click(mouse_pos)

                    if self.roll_dice_button_is_clicked(mouse_pos):
                        self.roll_dice()
                        print(self.dice_values)
                    else:

                        for index, column in enumerate(self.board.columns):
                            if column.is_clicked(mouse_pos):
                                if selected_column is None:

                                    if self.board.current_column_is_empty(index):
                                        print("Invalid move")
                                        break
                                    else:
                                        if current_player.color != column.column_stack[0].color:
                                            print("Invalid move")
                                            break
                                        else:
                                            selected_column = index
                                else:
                                    distance = abs(selected_column - index)
                                    if self.board.validate_move(selected_column, index, current_player, self.dice_values,distance):
                                        removed = self.board.move_piece(selected_column, index, self.screen)
                                        self.dice_values.remove(distance)
                                        selected_column = None
                                        self.board.draw_pieces(self.screen)
                                        if removed is not None:
                                            if current_player == self.player1:
                                                self.player2.removed_pieces.append(removed)
                                            else:
                                                self.player1.removed_pieces.append(removed)
                                            print(self.player1.color)
                                            print(self.player1.removed_pieces)
                                            print(self.player2.color)
                                            print(self.player2.removed_pieces)

                                        if len(self.dice_values) == 0:
                                            if current_player == self.player1:
                                                current_player = self.player2
                                            else:
                                                current_player = self.player1

                                    else:
                                        selected_column = None
                                        print("Invalid move")
                                        break



            pygame.display.flip()

    def draw_roll_dice_button(self):
        self.roll_dice_button = pygame.image.load("../assets/roll-dice.png")
        self.roll_dice_button_rect = self.roll_dice_button.get_rect()
        self.roll_dice_button_rect.x = 100
        self.roll_dice_button_rect.y = self.screen.get_height()/2 - self.roll_dice_button.get_height()/2
        self.screen.blit(self.roll_dice_button, (self.roll_dice_button_rect.x, self.roll_dice_button_rect.y))


    def roll_dice_button_is_clicked(self, mouse_pos):
        return self.roll_dice_button_rect.collidepoint(mouse_pos)

    def roll_dice(self):
        self.dice1.roll()
        self.dice2.roll()
        if self.dice1.value == self.dice2.value:
            self.dice_values.extend([self.dice1.value, self.dice1.value, self.dice1.value, self.dice1.value])
        else:
            self.dice_values.append(self.dice1.value)
            self.dice_values.append(self.dice2.value)
        self.draw_dice()

    def draw_dice(self):
        self.dice1.dice_rect.x = 100
        self.dice1.dice_rect.y = self.screen.get_height()/2 - self.dice1.face.get_height()/2
        self.dice2.dice_rect.x = 200
        self.dice2.dice_rect.y = self.screen.get_height()/2 - self.dice2.face.get_height()/2
        self.screen.blit(self.dice1.face, (self.dice1.dice_rect.x, self.dice1.dice_rect.y))
        self.screen.blit(self.dice2.face, (self.dice2.dice_rect.x, self.dice2.dice_rect.y))