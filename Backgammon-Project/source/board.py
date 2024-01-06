
import pygame

class Board :

    BG_COLOR = (255, 255, 255)
    def __init__(self):
        self.screen = pygame.display.set_mode((1920,1080))
        self.screen.fill(self.BG_COLOR)
        self.triangles = [[],[]]
        self.middle_line_width = 100

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
                self.screen.blit(self.triangles[0][index], (self.x + index * self.triangle_width, self.y))
                self.screen.blit(self.triangles[1][index], (self.x + index * self.triangle_width, self.y+self.triangle_height + 100 ))
            else:
                self.screen.blit(self.triangles[0][index], (self.x + index * self.triangle_width +self.middle_line_width, self.y))
                self.screen.blit(self.triangles[1][index], (self.x + index * self.triangle_width +self.middle_line_width, self.y+self.triangle_height + 100))

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.x +6*self.triangle_width +1, 0, 100, 1080))


