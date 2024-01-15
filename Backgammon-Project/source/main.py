import sys
import board
import pygame
from game import Game
from player import Player
from board import Board

if __name__ == '__main__':

    pygame.init()
    board = Board()
    game = Game(board)

    current_screen = "main_menu"

    while True:
        if current_screen == "main_menu":
            current_screen = game.main_menu()
        elif current_screen == "mode_selection":
            current_screen, selected_mode = game.mode_selection()
            if current_screen == "game_play":
                game.init_game(selected_mode)
                game.play()

