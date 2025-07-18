from objects.main_entity import MainEntity
import pygame
from constants import *
import random
import battle
import state_manager

class NPC(MainEntity):

    def __init__(self, x, y, spritesheet):
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        super().__init__(x, y, self.width, self.height, spritesheet)
        self.y_sprite_sheet_index = 0
        self.speed = 1
        self.dir = 0

        self.frame_count = 0
        self.trigger_frame = random.randint(50, 300)

    #
    # def change_state(self, state_manager, player):
    #     state_manager.current_state = battle.Battle(player, self.battle_object)


    def update(self, cam_offset=None, map_group=None):
        self.frame_count += 1

        if self.frame_count > self.trigger_frame:
            self.frame_count = 0
            self.dir = random.randint(0, 3)


        # self.move()
        self.animate()
        self.update_cam_offset(cam_offset)

    def move(self):
        if self.dir == 1:
            self.y_sprite_sheet_index = 1
            self.y -= self.speed

        if self.dir == 2:
            self.y_sprite_sheet_index = 2
            self.x += self.speed

        if self.dir == 3:
            self.y_sprite_sheet_index = 3
            self.x -= self.speed

        if self.dir == 0:
            self.y_sprite_sheet_index = 0
            self.y += self.speed

        self.x = max(0, min(self.x, WORLD_WIDTH  - self.width))
        self.y = max(0, min(self.y, WORLD_HEIGHT - self.height))
