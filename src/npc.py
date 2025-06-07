import main_entity
import pygame
from constants import *
import random
import collision_handler

class NPC(main_entity.Main_entity):

    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        super().__init__(self.x, self.y, self.width, self.height, "manager-Sheet.png")
        self.y_sprite_sheet_index = 0
        self.speed = 1
        self.dir = 0
        self.collision_handler = collision_handler.CollisionHandler(self)

        self.frame_count = 0
        self.trigger_frame = random.randint(50, 300)


    def update(self, cam_offset, map_group):
        self.frame_count += 1

        if self.frame_count > self.trigger_frame:
            self.frame_count = 0
            self.dir = random.randint(0, 3)


        self.move()
        self.collision_handler.update(map_group)
        self.animate()
        self.update_cam_offset(cam_offset)
        print(self.rect)

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
