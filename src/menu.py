from constants import *
import pygame
import random
from event_system import event_system
from menu_stable import MenuStable


class Menu():
    def __init__(self):
        event_system.on("set_menu_visible", self.set_visible)
        event_system.on("set_menu_stable_visible", self.set_stable_visible)
        from player.player import main_player
        self.player = main_player.current_wrestler.battle_object
        self.items = self.player.options["Items"]
        self.player_group = pygame.sprite.Group()
        for wrestler in main_player.stable:
            self.player_group.add(wrestler.battle_object)
        self.player.rect.topleft = (0, 0)
        self.index = 0
        self.menu_stable = MenuStable()
        self.is_visible = True
        self.is_stable_visible = False


    def set_visible(self, bool=None):
        if bool:
            self.is_visible = bool
        else:
            self.is_visible = not self.is_visible

    def set_stable_visible(self):
        self.is_stable_visible = not self.is_stable_visible

    def update(self):
        self.player_group.update()
        self.index = self.index % len(self.items)


    def events(self, events):
        pass
    #     action = None
    #     for event in events:
    #         if event.type == pygame.JOYBUTTONDOWN:
    #             if event.button == 0:
    #                 action = "action_button"
    #             elif event.button == 11:
    #                 action = "index_up"
    #             elif event.button == 12:
    #                 action = "index_down"
    #
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_UP:
    #                 action = "index_up"
    #             elif event.key == pygame.K_DOWN:
    #                 action = "index_down"
    #             elif event.key == pygame.K_RETURN:
    #                 action = "enter"
    #             # elif event.key == pygame.K_p:
    #             #     event_system.raise_event("change_to_parent_state")
    #         if action:
    #             getattr(self, action)()

    def draw(self, surface):
        if self.is_visible:
            # player_bo = self.player.current_wrestler.battle_object
            surface.fill((255, 255, 255))
            self.menu_stable.draw(surface)
            # self.player_group.draw(surface)

            # WIDTH, HEIGHT = surface.get_size()
            font_size = 20
            padding = 20
            text_padding = 10
            font = pygame.font.SysFont("Arial", font_size)

            for i, option in enumerate(self.items):
                text = None
                str = ""
                if isinstance(option, dict):
                    if "qty" in option:
                        str = f"{option['name']} - Qty:{option['qty']}"
                    else:
                        str = option['name']
                    text = font.render(str, True, BLACK)
                else:
                    text = font.render(option, True, BLACK)

                surface.blit(text, (text_padding, font_size * i + text_padding * i + text_padding - 2))

            # selection_box = pygame.Rect(0,  0 + font_size * self.index + text_padding * self.index, items_box.width, font_size + padding)
            # pygame.draw.rect(surface, RED, selection_box, 6)


    def draw_scaled(self, sprite, surface):
        scale = 0.5
        scaled_image = pygame.transform.scale(sprite.image, (
            int(sprite.rect.width * scale),
            int(sprite.rect.height * scale)
        ))
        rect = scaled_image.get_rect(topleft=sprite.rect.topleft)
        surface.blit(scaled_image, rect)



    def wrap_text(self, text, max_chars):
        lines = []
        while len(text) > max_chars:
            # Find the last space within limit
            split_index = text.rfind(" ", 0, max_chars)
            if split_index == -1:
                split_index = max_chars  # force break
            lines.append(text[:split_index])
            text = text[split_index:].lstrip()
        lines.append(text)
        return lines


    def index_up(self):
        self.index -= 1


    def index_down(self):
        self.index += 1

    def enter(self):
        print("enter")
