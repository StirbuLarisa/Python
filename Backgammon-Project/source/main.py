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
    game.init_game()
    game.play()

