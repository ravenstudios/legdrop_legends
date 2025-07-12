from objects.main_entity import MainEntity
import pygame
from constants import *
import constants
from player.movement_handler import MovementHandler
from player.player_battle_object import PlayerBattleObject
from player.collision_handler import CollisionHandler
from wrestlers import brother
from event_system import event_system


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
        super().__init__(self.x, self.y, self.width, self.height, "Brother16x16-Sheet.png")
        self.y_sprite_sheet_index = 0
        self.speed = 7
        self.movement_handler = MovementHandler(self)
        self.collision_handler = CollisionHandler(self)
        self.current_wrestler = brother.Brother(50, 300)
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
            self.movement_handler.key_handler(self.joystick, obj_group)
            self.collision_handler.update(groups)

        self.animate()
        self.rect.x = max(0, min(self.rect.x, GAME_WIDTH  - self.rect.width))
        self.rect.y = max(0, min(self.rect.top, GAME_HEIGHT - self.rect.height))
        # pygame.display.set_caption(f"cam:{cam_offset} Rect.center.y:{self.rect}  |  WORLD:{WORLD_WIDTH}-{WORLD_HEIGHT}  |  Halfscreen:{GAME_WIDTH // 2}")
main_player = Player()
