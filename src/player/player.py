from objects.main_entity import MainEntity
import pygame
from constants import *
import constants
import random
from player.movement_handler import MovementHandler
from player.collision_handler import CollisionHandler
from wrestlers.brother import Brother
from wrestlers.clown import Clown
from wrestlers.crawdaddy import Crawdaddy
from event_system import event_system
from player.item_manager import item_manager


class Player(MainEntity):
    def __init__(self):
        event_system.on("player_set_in_menu", self.set_in_menu)
        event_system.on("player_set_in_dialog", self.set_in_dialog)
        event_system.on("player_get_player", self.get_player)
        self.joystick = None
        self.x = 0
        self.y = 0
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        super().__init__(self.x, self.y, self.width, self.height, "manager-Sheet.png")
        self.y_sprite_sheet_index = 0
        self.speed = 7
        self.item_manager = item_manager
        self.movement_handler = MovementHandler(self)
        self.collision_handler = CollisionHandler(self)
        self.stable = [
            Brother(),
            Crawdaddy(),
            Clown(),
            Brother()
        ]
        self.current_wrestler = self.stable[2]
        self.current_wrestler.battle_object.lunge_dir = (1, -1)
        self.dir = 0
        self.collisions = False
        self.action_button_pressed = False
        self.just_loaded_map = False
        self.in_submap = False
        self.leaving_submap = False
        self.prev_cords = ()
        self.spawn_point = ()
        self.in_menu = False
        self.in_dialog = False
        self.in_menu = False


    def get_current_wrestler(self):
        return self.current_wrestler


    def get_player(self, arg=None):
        return self


    def set_in_menu(self, bool):
        self.in_menu = bool


    def set_in_dialog(self, bool):
        self.in_dialog = bool


    def move_to_new_map(self, spawn_point):
        if not self.leaving_submap:
            self.spawn_point = spawn_point
            self.x, self.y = 0, 0
        self.just_loaded_map = True


    def update(self, cam_offset, groups):
        obj_group, door_group, npc_group, map_group = groups
        merged_group = pygame.sprite.Group()
        merged_group.add(obj_group.sprites())
        merged_group.add(npc_group.sprites())

        self.movement_handler.update(merged_group)



        if self.just_loaded_map:
            if self.leaving_submap:
                self.x, self.y = self.prev_cords[1]
                self.rect = self.prev_cords[0]
                self.leaving_submap = False
                self.in_submap = False
            else:
                self.rect.center = self.spawn_point
                self.x = 0
                self.y = 0
            self.just_loaded_map = False
        else:
            # self.movement_handler.key_handler(self.joystick, obj_group)
            self.collision_handler.update(groups)

        self.animate()
        self.rect.x = max(0, min(self.rect.x, GAME_WIDTH  - self.rect.width))
        self.rect.y = max(0, min(self.rect.top, GAME_HEIGHT - self.rect.height))




main_player = Player()
