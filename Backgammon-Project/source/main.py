import sys
import board
import pygame

if __name__ == '__main__':

    pygame.init()
    board = board.Board()
    board.init_game()
    selected_column = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                board.handle_column_click(mouse_pos)

                for index, column in enumerate(board.columns):
                    if column.is_clicked(mouse_pos):
                        if selected_column == None:
                            selected_column = index
                        else:
                            board.move_piece(selected_column, index)
                            selected_column = None
                            board.draw_pieces()

        pygame.display.flip()
