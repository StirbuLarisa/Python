import random
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

    def init_game(self, mode):
        """
        Initializes the game. It chose the type of the second player based on the mode. It also initializes the board.
        :param mode: The mode of the game. It can be either "pvp" (2 players) or "pvc" (player vs computer).
        :type mode: str
        :return: None
        """
        self.board.init_board(self.screen)
        self.player1 = Player("human", "white")
        if mode == "pvp":
            self.player2 = Player("human", "black")
        else:
            self.player2 = Player("pc", "black")

    def main_menu(self):
        """
        The main menu loop. It draws the main menu and handles the user's clicks. It returns the next state of the game.
        The player can choose to play the game or to quit the game. If the player chooses to play the game, the game
        will enter the mode selection loop, where the player can choose the game mode.

        :return: The next state of the game.
        :rtype: str
        """
        rect_width, rect_height = 550, 500
        transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        transparent_surface.fill((255, 255, 255, 150))
        while True:
            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(transparent_surface,
                             (self.screen.get_width() // 2 - 250, self.screen.get_height() // 4 - 50))
            self.draw_text("Backgammon", self.screen.get_width() // 2 - 200, self.screen.get_height() // 4, (0, 0, 0),
                           self.title_font)

            play_button = pygame.Rect(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 - 30, 100, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), play_button)
            self.draw_text("Play", self.screen.get_width() // 2 - 26, self.screen.get_height() // 2 - 20,
                           (255, 255, 255), self.font)

            quit_button = pygame.Rect(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 + 30, 100, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), quit_button)
            self.draw_text("Quit", self.screen.get_width() // 2 - 26, self.screen.get_height() // 2 + 42,
                           (255, 255, 255), self.font)

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
        """
        The game loop. It draws the board, the pieces and the removed pieces. It has the logic for both human and
        computer players. It also handles the player's clicks.
        It checks if the player can move. If the player cannot move, it changes the current player.
        It checks if the player can put a piece back on board. If not, it changes the current player.
        It checks if the player is the winner. If the player is the winner, it draws the winner.
        In case of a computer player it rolls the dice, computes all possible moves and chooses a random move.

        :return:
        """
        current_player = self.player1
        selected_column = None
        possible_moves = []

        while True:
            for event in pygame.event.get():

                can_be_removed = False
                if len(self.dice_values) == 0:
                    self.draw_roll_dice_button(current_player.color)

                # this part is the logic for the computer player
                if current_player.type == "pc":
                    self.roll_dice(current_player.color)
                    pygame.time.delay(1000)
                    self.draw_dice(current_player.color)
                    pygame.display.flip()

                    while self.dice_values:

                        if current_player.removed_pieces:
                            selected_column = 0
                            possible_moves = self.board.compute_possible_moves(current_player, self.dice_values,
                                                                               selected_column)
                            if len(possible_moves) == 0:
                                selected_column = None
                                break
                            move_index = random.randint(0, len(possible_moves) - 1)
                            move = possible_moves[move_index]
                            self.handle_move(current_player, move, selected_column)
                            selected_column = None
                            continue

                        can_move, possible_indices = self.check_if_player_cannot_move(current_player)

                        if not can_move:
                            current_player = self.reset_current_player(current_player)
                            break

                        move_index = random.randint(0, len(possible_indices) - 1)
                        move = possible_indices[move_index]

                        if move[0] != move[1]:
                            self.handle_move(current_player, move[1], move[0])
                        else:
                            self.finish_piece(current_player, move[0])

                        if self.is_winner(current_player):
                            self.draw_winner(current_player)
                            pygame.display.flip()
                        else:
                            self.board.draw_board(self.screen)
                            self.board.draw_pieces(self.screen)
                            self.board.draw_removed_pieces(self.screen, self.player1)
                            self.board.draw_removed_pieces(self.screen, self.player2)
                            self.draw_dice(current_player.color)
                            pygame.display.flip()
                            pygame.time.delay(1000)
                    current_player = self.reset_current_player(current_player)
                    break

                # this part is the logic for the human player
                # it checks if the player can go back on board
                if current_player.removed_pieces != [] and selected_column is None:
                    if current_player.color == "white":
                        selected_column = 25
                    else:
                        selected_column = 0

                    if self.dice_values != []:
                        possible_moves = self.board.compute_possible_moves(current_player, self.dice_values,
                                                                           selected_column)
                        self.board.draw_possible_moves(self.screen, possible_moves)

                # the eaten piece cannot be put back on board and the player has to change
                if not possible_moves and len(self.dice_values) != 0 and current_player.removed_pieces != []:
                    self.draw_dice(current_player.color)
                    pygame.display.flip()
                    time.sleep(2)
                    current_player = self.change_player(current_player)
                    self.board.draw_board(self.screen)
                    self.board.draw_pieces(self.screen)
                    self.board.draw_removed_pieces(self.screen, self.player1)
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
                        if len(self.dice_values) == 0:
                            self.roll_dice(current_player.color)
                            self.draw_dice(current_player.color)
                            pygame.display.flip()

                            can_move, possible_indices = self.check_if_player_cannot_move(current_player)
                            if can_move == False:
                                current_player = self.reset_current_player(current_player)
                                selected_column = None
                                break

                            if selected_column is not None:
                                possible_moves = self.board.compute_possible_moves(current_player, self.dice_values,
                                                                                   selected_column)
                                self.board.draw_possible_moves(self.screen, possible_moves)
                            break

                    # this part is the main logic for the human player
                    # it checks if there are dice values left
                    elif len(self.dice_values) != 0:

                        if self.check_if_can_remove_piece(selected_column, current_player, self.dice_values):
                            can_be_removed = True

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
                                        self.board.draw_possible_moves(self.screen, possible_moves)

                                        if self.check_if_can_remove_piece(selected_column, current_player,
                                                                          self.dice_values):
                                            can_be_removed = True
                                            break

                                        if possible_moves == [] and can_be_removed is False:
                                            print("Invalid move")
                                            selected_column = None
                                            break

                                    elif selected_column is not None:
                                        # if the player can remove a piece
                                        if possible_moves == [] and can_be_removed is True:

                                            self.finish_piece(current_player, selected_column)

                                            can_move, possible_indices = self.check_if_player_cannot_move(
                                                current_player)
                                            if len(self.dice_values) != 0 and can_move == False:
                                                current_player = self.reset_current_player(current_player)
                                                selected_column = None
                                                break
                                            selected_column = None

                                            if self.is_winner(current_player):
                                                self.draw_winner(current_player)

                                            if self.dice_values == []:
                                                current_player = self.change_player(current_player)
                                                break
                                            else:
                                                self.draw_dice(current_player.color)
                                                pygame.display.flip()

                                        elif possible_moves == []:
                                            print("Invalid move")
                                            selected_column = None
                                            break

                                        # the player can move OR finish a piece
                                        elif possible_moves != [] and can_be_removed is True:
                                            # move
                                            if index in possible_moves:
                                                possible_moves, selected_column = self.handle_move(current_player,
                                                                                                   index,
                                                                                                   selected_column)

                                                can_move, possible_indices = self.check_if_player_cannot_move(
                                                    current_player)
                                                if len(self.dice_values) != 0 and not can_move :
                                                    current_player = self.reset_current_player(current_player)
                                                    selected_column = None
                                                    break

                                                if len(self.dice_values) == 0:
                                                    self.board.draw_board(self.screen)
                                                    self.board.draw_pieces(self.screen)
                                                    current_player = self.change_player(current_player)
                                                    self.board.draw_removed_pieces(self.screen, self.player1)
                                                    self.board.draw_removed_pieces(self.screen, self.player2)
                                                    break

                                            # finish piece
                                            elif index == selected_column:
                                                self.finish_piece(current_player, selected_column)

                                                can_move, possible_indices = self.check_if_player_cannot_move(
                                                    current_player)
                                                if len(self.dice_values) != 0 and can_move == False:
                                                    current_player = self.reset_current_player(current_player)
                                                    selected_column = None
                                                    break
                                                selected_column = None

                                                if self.is_winner(current_player):
                                                    self.draw_winner(current_player)

                                                if self.dice_values == []:
                                                    current_player = self.change_player(current_player)
                                                    break

                                                else:
                                                    self.draw_dice(current_player.color)
                                                    pygame.display.flip()

                                        # the player can only move
                                        elif index in possible_moves:
                                            possible_moves, selected_column = self.handle_move(current_player, index,
                                                                                               selected_column)

                                            can_move, possible_indices = self.check_if_player_cannot_move(
                                                current_player)
                                            if len(self.dice_values) != 0 and not can_move:
                                                current_player = self.reset_current_player(current_player)
                                                selected_column = None
                                                break

                                            if len(self.dice_values) == 0:
                                                self.board.draw_board(self.screen)
                                                self.board.draw_pieces(self.screen)
                                                current_player = self.change_player(current_player)
                                                self.board.draw_removed_pieces(self.screen, self.player1)
                                                self.board.draw_removed_pieces(self.screen, self.player2)
                                                break

            pygame.display.flip()

    def reset_current_player(self, current_player):
        """
        Resets the current player. It draws the board and the pieces and resets the dice values. It also changes the
        current player.
        :param current_player: The current player.
        :type current_player: Player
        :return: The new current player.
        :rtype: Player
        """
        time.sleep(3)
        current_player = self.change_player(current_player)
        self.board.draw_board(self.screen)
        self.board.draw_pieces(self.screen)
        self.board.draw_removed_pieces(self.screen, self.player1)
        self.board.draw_removed_pieces(self.screen, self.player2)
        self.dice_values = []
        return current_player

    def check_if_player_cannot_move(self, current_player, current_column=None):
        """
        Checks if the player can move. If the player can move, it returns True and the possible indices. If the player
        cannot move, it returns False and None. Possible indices is a list of tuples. Each tuple contains the index of
        the column from which the piece can be moved and the index of the column to which the piece can be moved.
        If the player can remove a piece, the first index of the tuple is 0 if the player is white and 25 if the player
        is black. The second index is the index of the column from which the piece can be removed.
        It checks if the player can remove a piece first. If the player cannot remove a piece, it checks if the player
        can move a piece from the board. If the player cannot move a piece from the board, it checks if the player can
        move a piece from the house. If the player cannot move a piece from the house, it returns False and None.

        :param current_player: The current player.
        :type current_player: Player
        :param current_column: The index of the column from which the piece can be moved.
        :type current_column: int
        :return: True if the player can move, False otherwise. Possible indices if the player can move, None otherwise.
        :rtype: tuple
        """
        can_move = False
        possible_indices = []

        if self.all_in_house(current_player):
            if current_player.color == "white":
                for index in range(1, 7):
                    if not self.board.current_column_is_empty(index):
                        if self.check_if_can_remove_piece(index, current_player, self.dice_values):
                            possible_indices.append((index, index))
                            can_move = True
            else:
                for index in range(19, 25):
                    if not self.board.current_column_is_empty(index):
                        if self.check_if_can_remove_piece(index, current_player, self.dice_values):
                            possible_indices.append((index, index))
                            can_move = True

        for index in range(1, len(self.board.columns) - 1):
            if self.board.current_column_is_empty(index) == False:
                if self.board.columns[index].column_stack[0].color == current_player.color:
                    possible_moves = self.board.compute_possible_moves(current_player, self.dice_values, index)
                    if possible_moves != []:
                        can_move = True
                        for move in possible_moves:
                            possible_indices.append((index, move))

        if can_move == False:
            return False, None
        else:
            return True, possible_indices

    def handle_move(self, current_player, index, selected_column):
        """
        Handles the move of the piece. It moves the piece from the selected column to the index column. It also removes
        the piece if the piece is eaten. It returns the possible moves and the selected column.
        :param current_player: The current player.
        :type current_player: Player
        :param index: The index of the column to which the piece is moved.
        :type index: int
        :param selected_column: The index of the column from which the piece is moved.
        :type selected_column: int
        :return: The possible moves and the selected column.
        :rtype: tuple (list, int or None)
        """
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
        return possible_moves, selected_column

    def finish_piece(self, current_player, selected_column):
        """
        Finishes the piece. It removes the piece from the house, from the selected column and updates the dice values.
        It also draws the board and the pieces.

        :param current_player: The player that finished the piece.
        :type current_player: Player
        :param selected_column: The index of the column from which the piece is removed.
        :type selected_column: int
        :return: None
        """
        current_player.finished_pieces += 1
        self.board.columns[selected_column].column_stack.pop()
        self.board.draw_board(self.screen)
        self.board.draw_pieces(self.screen)
        self.board.draw_removed_pieces(self.screen, self.player1)
        self.board.draw_removed_pieces(self.screen, self.player2)
        if current_player.color == "white":
            if selected_column in self.dice_values:
                self.dice_values.remove(selected_column)
            else:
                self.dice_values.remove(max(self.dice_values))
        else:
            if 25 - selected_column in self.dice_values:
                self.dice_values.remove(25 - selected_column)
            else:
                self.dice_values.remove(max(self.dice_values))

    def change_player(self, current_player):
        """
        Changes the current player.
        :param current_player: The current player.
        :type current_player: Player
        :return: The new current player.
        :rtype: Player
        """
        if current_player == self.player1:
            current_player = self.player2
        else:
            current_player = self.player1
        return current_player

    def draw_text(self, text, x, y, color, txt_font):
        """
        Draws the text on the screen.
        :param text: The text to be drawn.
        :type text: str
        :param x: The x coordinate of the text.
        :type x: int
        :param y: The y coordinate of the text.
        :type y: int
        :param color: The color of the text.
        :type color: tuple
        :param txt_font: The font of the text.
        :type txt_font: pygame.font.Font
        :return: None
        """
        text_surface = txt_font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def mode_selection(self):
        """
        The mode selection loop. It draws the mode selection menu and handles the user's clicks. It returns the next
        state of the game (the actual game) and the selected mode.
        :return: The next state of the game and the selected mode.
        :rtype: tuple (str, str)
        """
        rect_width, rect_height = 780, 500
        transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        transparent_surface.fill((255, 255, 255, 150))
        while True:
            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(transparent_surface,
                             (self.screen.get_width() // 2 - 400, self.screen.get_height() // 4 - 50))
            self.draw_text("Select Game Mode", self.screen.get_width() // 2 - 330, self.screen.get_height() // 4,
                           (0, 0, 0), self.title_font)

            pvp_button = pygame.Rect(self.screen.get_width() // 2 - 130, self.screen.get_height() // 2 - 26, 270, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), pvp_button)
            self.draw_text("Player vs Player", self.screen.get_width() // 2 - 90, self.screen.get_height() // 2 - 17,
                           (255, 255, 255), self.font)

            pvc_button = pygame.Rect(self.screen.get_width() // 2 - 130, self.screen.get_height() // 2 + 35, 270, 50)
            pygame.draw.rect(self.screen, (0, 0, 0), pvc_button)
            self.draw_text("Player vs Computer", self.screen.get_width() // 2 - 111, self.screen.get_height() // 2 + 45,
                           (255, 255, 255), self.font)

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
        """
        Draws the roll dice button.
        :param player_color: The color of the player.
        :type player_color: str
        :return: None
        """

        self.roll_dice_button = pygame.image.load("../assets/roll-dice.png")
        self.roll_dice_button_rect = self.roll_dice_button.get_rect()
        if player_color == "black":
            self.roll_dice_button_rect.x = 1700
        else:
            self.roll_dice_button_rect.x = 100
        self.roll_dice_button_rect.y = self.screen.get_height() / 2 - self.roll_dice_button.get_height() / 2
        self.screen.blit(self.roll_dice_button, (self.roll_dice_button_rect.x, self.roll_dice_button_rect.y))

    def roll_dice_button_is_clicked(self, mouse_pos):
        """
        Checks if the roll dice button is clicked.
        :param mouse_pos: The position of the mouse.
        :type mouse_pos: tuple
        :return: True if the roll dice button is clicked, False otherwise.
        :rtype: bool
        """
        return self.roll_dice_button_rect.collidepoint(mouse_pos)

    def roll_dice(self, player_color):
        """
        Rolls the dice and updates the dice values. It also draws the dice.
        :param player_color: The color of the player.
        :type player_color: str
        :return: None
        """
        self.dice1.roll()
        self.dice2.roll()
        if self.dice1.value == self.dice2.value:
            self.dice_values.extend([self.dice1.value, self.dice1.value, self.dice1.value, self.dice1.value])
        else:
            self.dice_values.append(self.dice1.value)
            self.dice_values.append(self.dice2.value)
        self.draw_dice(player_color)

    def draw_dice(self, player_color):
        """
        Draws the dice.
        :param player_color: The color of the player.
        :type player_color: str
        :return: None
        """

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

    def all_in_house(self, player):
        """
        Checks if all the pieces of the player are in the house. It checks if all the pieces of the same color are in
        their home.
        False.
        :param player: The player.
        :type player: Player
        :return: True if all the pieces of the player are in the house, False otherwise.
        :rtype: bool
        """
        if player.color == "white":
            for column in self.board.columns[7:24]:
                if len(column.column_stack) != 0 and column.column_stack[-1].color == "white":
                    return False
        else:
            for column in self.board.columns[1:19]:
                if len(column.column_stack) != 0 and column.column_stack[-1].color == "black":
                    return False
        if len(player.removed_pieces) == 0:
            return True
        else:
            return False

    def check_if_can_remove_piece(self, current_column, player, dice_values):
        """
        Checks if the player can remove a piece from the board.
        It checks if all pieces are in house. It checks if the current column has a piece that can be removed.
        It also checks the case when on the column corresponding to the dice is empty and the player has pieces on the
        columns after the dice, it can remove the one that is after.

        :param current_column: The index of the column from which the piece can be removed.
        :type current_column: int
        :param player: The player.
        :type player: Player
        :param dice_values: The values of the dice.
        :type dice_values: list
        :return: True if the player can remove a piece, False otherwise.
        :rtype: bool
        """
        can_remove = True
        if current_column is None:
            return False
        for dice in dice_values:
            if self.all_in_house(player):
                if player.color == "white":
                    if current_column == dice:
                        if self.board.current_column_is_empty(dice) == False:
                            if self.board.columns[dice].column_stack[0].color == "white" and len(
                                    self.board.columns[dice].column_stack) != 0:
                                return True
                    elif current_column < dice:
                        for index in range(current_column + 1, 7):
                            if self.board.current_column_is_empty(index) == False:
                                if self.board.columns[index].column_stack[0].color != "black":
                                    can_remove = False
                        if can_remove == True:
                            return can_remove
                else:
                    if current_column == 25 - dice:
                        if self.board.current_column_is_empty(25 - dice) == False:
                            if self.board.columns[25 - dice].column_stack[0].color == "black" and len(
                                    self.board.columns[25 - dice].column_stack) != 0:
                                return True
                    elif current_column > 25 - dice:
                        for index in range(19, current_column):
                            if self.board.current_column_is_empty(index) == False:
                                if self.board.columns[index].column_stack[0].color != "white":
                                    can_remove = False
                        if can_remove == True:
                            return can_remove
        return False

    def is_winner(self, player):
        """
        Checks if the player is the winner.
        :param player: The player.
        :type player: Player
        :return: True if the player is the winner, False otherwise.
        :rtype: bool
        """
        if player.finished_pieces == 15:
            return True
        else:
            return False

    def draw_winner(self, player):
        """
        Draws the winner on the screen.
        :param player: The player that won
        :type player: Player
        :return: None
        """
        rect = pygame.Rect(self.screen.get_width() / 2 - self.screen.get_width() / 4,
                           self.screen.get_height() / 2 - self.screen.get_height() / 8, self.screen.get_width() / 2,
                           self.screen.get_height() / 4)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        self.draw_text(f"{player.color} player won!", rect.x + 160, rect.y + 80, (0, 0, 0), self.title_font)
        pygame.display.flip()
        time.sleep(8)
        pygame.quit()
        sys.exit()
