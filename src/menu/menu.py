from constants import *
import pygame
import random
from event_system import event_system
from menu.menu_stable import MenuStable
from menu.menu_options import MenuOptions
from menu.menu_status import MenuStatus
from menu.menu_game_options import MenuGameOptions
from menu.menu_items import MenuItems



class Menu():
    def __init__(self):
        event_system.on("set_menu_visible", self.set_visible)
        # event_system.on("set_menu_stable_visible", self.set_stable_visible)
        event_system.on("get_menu_visible", self.get_is_visible)
        event_system.on("menu_index_up", self.index_up)
        event_system.on("menu_index_down", self.index_down)
        event_system.on("menu_action_button", self.action_button)
        event_system.on("menu_back", self.menu_back)


        from player.player import main_player
        self.player = main_player.current_wrestler.battle_object
        # self.items = self.player.options["Items"]
        self.player_group = pygame.sprite.Group()
        for wrestler in main_player.stable:
            self.player_group.add(wrestler.battle_object)
        self.player.rect.topleft = (0, 0)
        self.index = 0

        self.menu_stable = MenuStable()
        self.menu_options_menu = MenuOptions(self)
        self.menu_status  = MenuStatus(self)
        self.menu_game_options = MenuGameOptions(self)
        self.menu_items = MenuItems(self)

        self.is_visible = False
        self.stable_visible = False
        self.status_visible = False
        self.items_visible = False
        self.game_options_visible = False
        self.menu_options_visible = True
        self.menu_options = ["items", "status", "stable", "options", "save_game"]
        self.menu_options_names = ["Items", "Status", "Stable", "Options", "Save Game"]

    def get_is_visible(self):
        return self.is_visible


    def set_visible(self, bool=None):
        print("set vis")
        if bool:
            self.is_visible = bool
        else:
            self.is_visible = not self.is_visible


    # def set_stable_visible(self):
    #     self.stable_visible = not self.stable_visible

    def update(self):
        self.player_group.update()
        self.index = self.index % len(self.menu_options)
        # self.index = self.index % len(self.items)


    def events(self, events):
        self.menu_game_options.events(events)


    def draw(self, surface):
        if self.is_visible:
            if self.menu_options_visible:
                self.menu_options_menu.draw(surface)
            if self.items_visible:
                self.menu_items.draw(surface)
            if self.status_visible:
                self.menu_status.draw(surface)
            if self.stable_visible:
                self.menu_stable.draw(surface)
            if self.game_options_visible:
                self.menu_game_options.draw(surface)


    def set_all_invisible(self):
        self.stable_visible = False
        self.status_visible = False
        self.items_visible = False
        self.game_options_visible = False
        self.menu_options_visible = False


    def index_up(self):
        if self.menu_options_visible:
            self.index -= 1
        elif self.game_options_visible:
            self.menu_game_options.index -= 1
        elif self.items_visible:
            self.menu_items.index -= 1


    def index_down(self):
        if self.menu_options_visible:
            self.index += 1
        elif self.game_options_visible:
            self.menu_game_options.index += 1
        elif self.items_visible:
            self.menu_items.index += 1


    def menu_back(self):
        self.set_all_invisible()
        self.menu_options_visible = True


    def action_button(self):
        menu_map = {
            self.menu_options_visible: self.select_action,
            self.game_options_visible: self.menu_game_options.select_action,
            self.items_visible: self.menu_items.select_action,
            # self.status_visible: self.menu_status.select_action,
            # self.stable_visible: self.menu_stable.select_action,
        }

        for visible, action in menu_map.items():
            if visible:
                action()
                break



    def select_action(self):
        selected_name = self.menu_options[self.index]
        if hasattr(self, selected_name):
            func = getattr(self, selected_name)
            func()
        else:
            print(f"No method named '{selected_name}'")


    def save_game(self):
        print("save_game")


    def items(self):
        self.set_all_invisible()
        self.items_visible = True

    def status(self):
        self.set_all_invisible()
        self.status_visible = True

    def stable(self):
        self.set_all_invisible()
        self.stable_visible = True

    def options(self):
        self.set_all_invisible()
        self.game_options_visible = True
