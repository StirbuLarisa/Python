import sys
import board
import pygame

if __name__ == '__main__':

    pygame.init()
    board = board.Board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        board.generate_board()
        pygame.display.flip()
