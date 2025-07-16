from constants import *
import pygame
import random
from event_system import event_system
from menu_stable import MenuStable


class Menu():
    def __init__(self):
        event_system.on("set_menu_visible", self.set_visible)
        event_system.on("set_menu_stable_visible", self.set_stable_visible)
        event_system.on("get_menu_visible", self.get_is_visible)
        from player.player import main_player
        self.player = main_player.current_wrestler.battle_object
        # self.items = self.player.options["Items"]
        self.player_group = pygame.sprite.Group()
        for wrestler in main_player.stable:
            self.player_group.add(wrestler.battle_object)
        self.player.rect.topleft = (0, 0)
        self.index = 0
        self.menu_stable = MenuStable()
        self.is_visible = True
        self.is_stable_visible = True
        self.menu_options = ["Items", "Stable", "Options"]

    def get_is_visible(self):
        return self.is_visible


    def set_visible(self, bool=None):
        if bool:
            self.is_visible = bool
        else:
            self.is_visible = not self.is_visible


    def set_stable_visible(self):
        self.is_stable_visible = not self.is_stable_visible

    def update(self):
        self.player_group.update()
        # self.index = self.index % len(self.items)


    def events(self, events):
        pass


    def draw(self, surface):
        if self.is_visible:


            WIDTH, HEIGHT = surface.get_size()
            font_size = 20
            padding = 20
            text_padding = 10
            font = pygame.font.SysFont("Arial", font_size)

            main_w = BLOCK_SIZE * 10 + padding * 3
            main_h = BLOCK_SIZE * len(self.player_group) * 2 + padding * 5
            main_x = WIDTH // 2 - main_w // 2
            main_y = HEIGHT // 2 - main_h // 2

            main_box = pygame.Rect(main_x, main_y, main_w, main_h)
            pygame.draw.rect(surface, (200, 200, 200), main_box)

            menu_options_box = pygame.Rect(main_box.x, main_box.y, font_size * 20, font_size * 50)
            for i, option in enumerate(self.menu_options):
                text = font.render(option, True, BLACK)
                surface.blit(text, (menu_options_box.x, menu_options_box.y + font_size * i))

            if self.is_stable_visible:
                self.menu_stable.draw(surface)


    def index_up(self):
        self.index -= 1


    def index_down(self):
        self.index += 1

    def enter(self):
        print("enter")
