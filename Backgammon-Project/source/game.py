import sys
import time

import pygame

from player import Player
from dice import Dice


class Game:
    """
    This class is responsible for most of the game logic.
    It initializes the game, draws the board, handles the player's clicks, etc.
    It also handles the game's menu loop.

    :ivar screen: The screen on which the menu and the game is drawn.
    :vartype screen: pygame.Surface
    :ivar board: The board on which the game is played.
    :vartype board: Board
    :ivar player1: The first player. Always white, always human.
    :vartype player1: Player
    :ivar player2: The second player. Always black, can be human or computer.
    :vartype player2: Player
    :ivar dice1: The first dice.
    :vartype dice1: Dice
    :ivar dice2: The second dice.
    :vartype dice2: Dice
    :ivar roll_dice_button: The button that rolls the dice.
    :vartype roll_dice_button: pygame.Surface
    :ivar roll_dice_button_rect: The rectangle that contains the roll_dice_button.
    :vartype roll_dice_button_rect: pygame.Rect
    :ivar dice_values: The values of the dice.
    :vartype dice_values: list
    :ivar font: The font used for the text.
    :vartype font: pygame.font.Font
    :ivar title_font: The font used for the title.
    :vartype title_font: pygame.font.Font
    :ivar menu_background: The background image of the menu.
    :vartype menu_background: pygame.Surface
    """

    def __init__(self, board):
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Backgammon")
        self.board = board
        self.player1 = None
        self.player2 = None
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.roll_dice_button = None
        self.roll_dice_button_rect = None
        self.dice_values = []
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 100)
        self.menu_background = pygame.image.load("../assets/wallpaper_menu.jpg")


    def init_game(self):
        self.board.init_board(self.screen)
        self.player1 = Player("human", "white")
        self.player2 = Player("human", "black")

    def main_menu(self):
        rect_width, rect_height = 550, 500
        transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        transparent_surface.fill((255, 255, 255, 150))
        while True:
            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(transparent_surface, (self.screen.get_width() // 2 - 250, self.screen.get_height() // 4 - 50))
            self.draw_text("Backgammon", self.screen.get_width() // 2 - 200, self.screen.get_height() // 4, (0, 0, 0), self.title_font)

            play_button = pygame.Rect(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 - 30, 100, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), play_button)
            self.draw_text("Play", self.screen.get_width() // 2 - 26, self.screen.get_height() // 2 - 20, (255,255,255), self.font)

            quit_button = pygame.Rect(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 + 30, 100, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), quit_button)
            self.draw_text("Quit", self.screen.get_width() // 2 - 26 , self.screen.get_height() // 2 + 42, (255,255,255),self.font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if play_button.collidepoint(event.pos):
                        return "mode_selection"
                    elif quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                pygame.display.flip()

    def play(self):
        current_player = self.player1

        selected_column = None
        possible_moves = []
        while True:
            for event in pygame.event.get():

                can_be_removed = False
                if len(self.dice_values) == 0:
                    self.draw_roll_dice_button(current_player.color)

                if self.all_in_house(current_player):
                    print(f"all in house {current_player.color}")
                    for dice in self.dice_values:
                        if current_player.color == "white":
                            if not self.board.current_column_is_empty(dice):
                                if self.board.columns[dice].column_stack[0].color == "white" and len(self.board.columns[dice].column_stack) != 0:
                                    can_be_removed = True
                                    break
                        else:
                            if not self.board.current_column_is_empty(25-dice):
                                if self.board.columns[25-dice].column_stack[0].color == "black" and len(self.board.columns[25-dice].column_stack) != 0:
                                    can_be_removed = True
                                    break
                    can_be_removed = False
                    print(can_be_removed)

                    ##break

                if current_player.removed_pieces != [] and selected_column is None:
                    if (current_player.color == "white"):
                        selected_column = 25
                    else:
                        selected_column = 0

                    if self.dice_values != []:
                        possible_moves = self.board.compute_possible_moves(current_player, self.dice_values,
                                                                           selected_column)
                        print(possible_moves)
                        self.board.draw_possible_moves(self.screen, possible_moves)



                if not possible_moves and len(self.dice_values) != 0 and current_player.removed_pieces != []:
                    print("schimbam jucatorul cand are piesa removed blocata")
                    self.draw_dice(current_player.color)
                    time.sleep(3)
                    if current_player == self.player1:
                        current_player = self.player2
                        self.board.draw_board(self.screen)
                        self.board.draw_pieces(self.screen)
                        self.board.draw_removed_pieces(self.screen, self.player1)
                        self.dice_values = []
                        selected_column = None
                        break
                    else:
                        current_player = self.player1
                        self.board.draw_board(self.screen)
                        self.board.draw_pieces(self.screen)
                        self.board.draw_removed_pieces(self.screen, self.player2)
                        self.dice_values = []
                        selected_column = None
                        break

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.board.handle_column_click(mouse_pos)

                    if self.roll_dice_button_is_clicked(mouse_pos):
                        self.roll_dice(current_player.color)
                        print(self.dice_values)
                        if (selected_column is not None):
                            possible_moves = self.board.compute_possible_moves(current_player, self.dice_values,
                                                                               selected_column)
                            print(possible_moves)
                            self.board.draw_possible_moves(self.screen, possible_moves)
                        break

                    elif len(self.dice_values) != 0:

                        if (can_be_removed and selected_column is not None):
                            for index in range(1,len(self.board.columns)-1):
                                if self.board.columns[index].is_clicked(mouse_pos):
                                    if current_player.color == "white":
                                        if index in self.dice_values:
                                            self.board.columns[index].column_stack.pop()
                                            self.board.draw_board(self.screen)
                                            self.board.draw_pieces(self.screen)
                                            current_player.finished_pieces += 1
                                            self.draw_dice(current_player.color)
                                            self.dice_values = []
                                            selected_column = None
                                            break
                                    else:
                                        if 25-index in self.dice_values:
                                            self.board.columns[index].column_stack.pop()
                                            self.board.draw_board(self.screen)
                                            self.board.draw_pieces(self.screen)
                                            current_player.finished_pieces += 1
                                            self.draw_dice(current_player.color)
                                            self.dice_values = []
                                            selected_column = None
                                            break
                            break

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
                                    if selected_column is None and can_be_removed:
                                        print(can_be_removed)
                                        selected_column = index
                                        break
                                    elif selected_column is None:
                                        selected_column = index
                                        possible_moves = self.board.compute_possible_moves(current_player,
                                                                                           self.dice_values,
                                                                                           selected_column)
                                        print(possible_moves)
                                        self.board.draw_possible_moves(self.screen, possible_moves)
                                        if (possible_moves == [] ):
                                            print("Invalid move")
                                            selected_column = None
                                            break
                                    elif selected_column is not None:
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


    def draw_text(self,text, x, y, color,txt_font):
        text_surface = txt_font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def mode_selection(self):
        rect_width, rect_height = 780, 500
        transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        transparent_surface.fill((255, 255, 255, 150))
        while True:
            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(transparent_surface, (self.screen.get_width() // 2 - 400, self.screen.get_height() // 4 - 50))
            self.draw_text("Select Game Mode", self.screen.get_width() // 2 - 330, self.screen.get_height() // 4, (0, 0, 0), self.title_font)

            pvp_button = pygame.Rect(self.screen.get_width() // 2 - 130, self.screen.get_height() // 2 - 26, 270, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), pvp_button)
            self.draw_text("Player vs Player", self.screen.get_width() // 2 - 90, self.screen.get_height() // 2 - 17, (255,255,255), self.font)

            pvc_button = pygame.Rect(self.screen.get_width() // 2 - 130, self.screen.get_height() // 2 + 35, 270, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), pvc_button)
            self.draw_text("Player vs Computer", self.screen.get_width() // 2 - 111, self.screen.get_height() // 2 + 45, (255,255,255),self.font)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if pvp_button.collidepoint(event.pos):
                        return "game_play", "pvp"
                    elif pvc_button.collidepoint(event.pos):
                        return "game_play", "pvc"

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

    def all_in_house(self, player):
        if player.color == "white":
            for column in self.board.columns[7:24]:
                if len(column.column_stack) != 0 and column.column_stack[-1].color == "white":
                    return False
        else:
            for column in self.board.columns[1:19]:
                if len(column.column_stack) != 0 and column.column_stack[-1].color == "black":
                    return False
        if(len(player.removed_pieces) == 0):
            return True
        else:
            return False
