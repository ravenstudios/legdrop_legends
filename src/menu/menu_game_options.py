import pygame
from constants import *

class MenuGameOptions():
    def __init__(self, menu):
        self.menu = menu
        self.index = 0
        self.game_options = ["music_level", "sound_level", "battle_speed", "text_speed"]
        self.game_options_names = ["Music Level", "Sound Level", "Battle Speed", "Text Speed"]

    def draw(self, surface):
        self.index = self.index % len(self.game_options)
        WIDTH, HEIGHT = surface.get_size()
        font_size = 30
        padding = 20
        text_padding = 5
        tri_pad = 10
        font = pygame.font.SysFont("Arial", font_size)
        main_w = BLOCK_SIZE * 10 + padding * 3
        main_h = BLOCK_SIZE * len(self.menu.player_group) * 2 + padding * 5
        main_x = WIDTH // 2 - main_w // 2
        main_y = HEIGHT // 2 - main_h // 2

        main_box = pygame.Rect(main_x, main_y, main_w, main_h)
        pygame.draw.rect(surface, (200, 200, 200), main_box)

        menu_options_box = pygame.Rect(main_box.x, main_box.y, font_size * 20, font_size * 5)
        pygame.draw.rect(surface, (0, 0, 200), menu_options_box)
        for i, option in enumerate(self.game_options_names):
            text = font.render(option, True, BLACK)
            y = menu_options_box.y + font_size * i + text_padding * i
            surface.blit(text, (menu_options_box.x + text_padding * 2 + tri_pad, y))
        y = menu_options_box.top + font_size * self.index + text_padding * self.index
        self.draw_triangle(surface, menu_options_box.left + tri_pad + text_padding, y + tri_pad + text_padding)



    def draw_triangle(self, surface, x, y):
        points = [(x, y), (x - 10, y - 10), (x - 10, y + 10)]
        pygame.draw.polygon(surface, (255, 255, 0), points)


    def select_action(self):
        selected_name = self.game_options[self.index]
        # Check if method exists
        if hasattr(self, selected_name):
            func = getattr(self, selected_name)
            func()  # Call the function
        else:
            print(f"No method named '{selected_name}'")



    def music_level(self):
        print("music_level")
    def sound_level(self):
        print("sound_level")
    def battle_speed(self):
        print("battle_speed")
    def text_speed(self):
        print("text_speed")
