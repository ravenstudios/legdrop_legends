import main_entity
import pygame
from constants import *
import constants
import movement_handler
import player_battle_object
import collision_handler


class Player(main_entity.Main_entity):

    def __init__(self, joystick=None):
        self.joystick = joystick
        self.x = 0
        self.y = 0
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        super().__init__(self.x, self.y, self.width, self.height, "Brother16x16-Sheet.png")
        self.y_sprite_sheet_index = 0
        self.speed = 7
        self.movement_handler = movement_handler.MovementHandler(self)
        self.collision_handler = collision_handler.CollisionHandler(self)
        self.battle_object = player_battle_object.PlayerBattleObject()
        self.dir = 0
        self.collisions = False
        self.action_button_pressed = False
        self.just_loaded_map = False

    def move_to_new_map(self, spawn_point):
        self.rect.center = spawn_point
        self.x, self.y = 0, 0
        self.just_loaded_map = True

    def update(self, cam_offset, obj_group, npc_group, state_manager, group_manager):
        if self.just_loaded_map:
            self.x = 0
            self.y = 0
            self.just_loaded_map = False
        else:
            self.movement_handler.key_handler(self.joystick, obj_group)
            self.collision_handler.update(obj_group, npc_group, state_manager, group_manager)

        self.animate()
        self.rect.x = max(0, min(self.rect.x, GAME_WIDTH  - self.rect.width))
        self.rect.y = max(0, min(self.rect.top, GAME_HEIGHT - self.rect.height))
        # pygame.display.set_caption(f"cam:{cam_offset}  |  X:{self.x}  |  Rect.center.y:{self.rect.top}  |  WORLD:{WORLD_WIDTH}-{WORLD_HEIGHT}  |  Halfscreen:{GAME_WIDTH // 2}")
