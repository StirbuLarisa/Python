import sys
import time

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

        selected_column = None
        possible_moves = []
        while True:
            for event in pygame.event.get():
                if len(self.dice_values) == 0:
                    self.draw_roll_dice_button(current_player.color)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.board.handle_column_click(mouse_pos)

                    if self.roll_dice_button_is_clicked(mouse_pos):
                        self.roll_dice(current_player.color)
                        print(self.dice_values)
                        if current_player.removed_pieces:
                            if len(self.dice_values) == 0:
                                break
                            if (current_player.color == "white"):
                                selected_column = 25
                            else:
                                selected_column = 0
                            possible_moves = self.board.compute_possible_moves(current_player, self.dice_values,
                                                                               selected_column)
                            print(possible_moves)
                            self.board.draw_possible_moves(self.screen, possible_moves)
                            if not possible_moves and len(self.dice_values) != 0:
                                time.sleep(3)
                                if current_player == self.player1:
                                    current_player = self.player2
                                    self.board.draw_board(self.screen)
                                    self.board.draw_pieces(self.screen)
                                    self.board.draw_removed_pieces(self.screen, self.player1)
                                    self.dice_values = []
                                    break
                                else:
                                    current_player = self.player1
                                    self.board.draw_board(self.screen)
                                    self.board.draw_pieces(self.screen)
                                    self.board.draw_removed_pieces(self.screen, self.player2)
                                    self.dice_values = []
                                    break
                        break

                    if current_player.removed_pieces != [] and selected_column is None:
                        if len(self.dice_values) == 0:
                            break
                        if (current_player.color == "white"):
                            selected_column = 25
                        else:
                            selected_column = 0
                        possible_moves = self.board.compute_possible_moves(current_player, self.dice_values,
                                                                           selected_column)
                        print(possible_moves)
                        self.board.draw_possible_moves(self.screen, possible_moves)

                    if not possible_moves and len(self.dice_values) != 0 and current_player.removed_pieces != []:
                        time.sleep(3)
                        if current_player == self.player1:
                            current_player = self.player2
                            self.board.draw_board(self.screen)
                            self.board.draw_pieces(self.screen)
                            self.board.draw_removed_pieces(self.screen, self.player1)
                            break
                        else:
                            current_player = self.player1
                            self.board.draw_board(self.screen)
                            self.board.draw_pieces(self.screen)
                            self.board.draw_removed_pieces(self.screen, self.player2)
                            break

                    elif len(self.dice_values) != 0:
                        for index in range(1, len(self.board.columns) - 1):
                            if self.board.columns[index].is_clicked(mouse_pos):

                                if selected_column is None and len(
                                        self.board.columns[index].column_stack) != 0 and current_player.color != \
                                        self.board.columns[index].column_stack[-1].color:
                                    print("Invalid move")
                                    break

                                if selected_column is None and len(self.board.columns[index].column_stack) == 0:
                                    print("Invalid move")
                                    break

                                else:
                                    if selected_column is None:
                                        selected_column = index
                                        possible_moves = self.board.compute_possible_moves(current_player,
                                                                                           self.dice_values,
                                                                                           selected_column)
                                        print(possible_moves)
                                        self.board.draw_possible_moves(self.screen, possible_moves)
                                        if (possible_moves == []):
                                            print("Invalid move")
                                            selected_column = None
                                            break
                                    else:
                                        if (possible_moves == []):
                                            print("Invalid move")
                                            selected_column = None
                                            break
                                        elif index in possible_moves:
                                            print("in move")
                                            removed = self.board.move_piece(selected_column, index, self.screen)
                                            self.draw_dice(current_player.color)
                                            self.dice_values.remove(abs(selected_column - index))
                                            possible_moves = []

                                            selected_column = None
                                            self.board.draw_pieces(self.screen)

                                            if removed is not None:
                                                if current_player == self.player1:
                                                    self.player2.removed_pieces.append(removed)
                                                    self.board.columns[0].column_stack = self.player2.removed_pieces
                                                else:
                                                    self.player1.removed_pieces.append(removed)
                                                    self.board.columns[25].column_stack = self.player1.removed_pieces

                                            self.board.draw_removed_pieces(self.screen, self.player1)
                                            self.board.draw_removed_pieces(self.screen, self.player2)

                                            if len(self.dice_values) == 0:
                                                self.board.draw_board(self.screen)
                                                self.board.draw_pieces(self.screen)
                                                self.board.draw_removed_pieces(self.screen, current_player)
                                                if current_player == self.player1:
                                                    current_player = self.player2
                                                    self.board.draw_removed_pieces(self.screen, current_player)
                                                    break
                                                else:
                                                    current_player = self.player1
                                                    self.board.draw_removed_pieces(self.screen, current_player)
                                                    break


            pygame.display.flip()

    def draw_roll_dice_button(self, player_color):

        self.roll_dice_button = pygame.image.load("../assets/roll-dice.png")
        self.roll_dice_button_rect = self.roll_dice_button.get_rect()
        if (player_color == "black"):
            self.roll_dice_button_rect.x = 1700
        else:
            self.roll_dice_button_rect.x = 100
        self.roll_dice_button_rect.y = self.screen.get_height() / 2 - self.roll_dice_button.get_height() / 2
        self.screen.blit(self.roll_dice_button, (self.roll_dice_button_rect.x, self.roll_dice_button_rect.y))

    def roll_dice_button_is_clicked(self, mouse_pos):
        return self.roll_dice_button_rect.collidepoint(mouse_pos)

    def roll_dice(self, player_color):

        self.dice1.roll()
        self.dice2.roll()
        if self.dice1.value == self.dice2.value:
            self.dice_values.extend([self.dice1.value, self.dice1.value, self.dice1.value, self.dice1.value])
        else:
            self.dice_values.append(self.dice1.value)
            self.dice_values.append(self.dice2.value)
        self.draw_dice(player_color)

    def draw_dice(self, player_color):

        if player_color == "black":
            self.dice1.dice_rect.x = 1700
            self.dice2.dice_rect.x = 1800

        else:
            self.dice1.dice_rect.x = 100
            self.dice2.dice_rect.x = 200

        self.dice1.dice_rect.y = self.screen.get_height() / 2 - self.dice1.face.get_height() / 2
        self.dice2.dice_rect.y = self.screen.get_height() / 2 - self.dice2.face.get_height() / 2
        self.screen.blit(self.dice1.face, (self.dice1.dice_rect.x, self.dice1.dice_rect.y))
        self.screen.blit(self.dice2.face, (self.dice2.dice_rect.x, self.dice2.dice_rect.y))

    def put_piece_back_into_play(self, player):

        posible_moves = self.board.compute_possible_moves(player, self.dice_values)
        if posible_moves is not None:
            self.board.draw_possible_moves(self.screen, posible_moves)
        else:
            self.board.draw_board(self.screen)
            self.board.draw_pieces(self.screen)
            self.board.draw_removed_pieces(self.screen, player)
