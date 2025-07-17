import pygame
from constants import *

class MenuStatus():
    def __init__(self, menu):
        self.menu = menu


    def draw(self, surface):
        WIDTH, HEIGHT = surface.get_size()
        font_size = 30
        padding = 20
        text_padding = 5
        font = pygame.font.SysFont("Arial", font_size)

        main_w = BLOCK_SIZE * 10 + padding * 3
        main_h = BLOCK_SIZE * len(self.menu.player_group) * 2 + padding * 5
        main_x = WIDTH // 2 - main_w // 2
        main_y = HEIGHT // 2 - main_h // 2

        main_box = pygame.Rect(main_x, main_y, main_w, main_h)
        pygame.draw.rect(surface, (200, 200, 200), main_box)

        menu_options_box = pygame.Rect(main_box.x, main_box.y, font_size * 20, font_size * 5)
        pygame.draw.rect(surface, (0, 0, 200), menu_options_box)
        for i, option in enumerate(self.menu.menu_options):
            text = font.render(option, True, BLACK)
            y = menu_options_box.y + font_size * i + text_padding * i
            surface.blit(text, (menu_options_box.x + text_padding * 2, y))

        y = menu_options_box.top + font_size * self.menu.index + text_padding * self.menu.index
        selection_box = pygame.Rect(menu_options_box.left, y, font_size * 4 + text_padding, font_size  + text_padding * 2)
        pygame.draw.rect(surface, (255, 255, 255), selection_box, 3)
