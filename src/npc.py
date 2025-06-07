import main_entity
import pygame
from constants import *
import random

class NPC(main_entity.Main_entity):

    def __init__(self):
        self.x = 300
        self.y = 300
        super().__init__(self.x, self.y, "Brother16x16-Sheet.png")
        self.y_sprite_sheet_index = 0
        self.speed = 1
        self.dir = 0

        self.frame_count = 0
        self.trigger_frame = random.randint(50, 300)


    def update(self, cam_offset):
        self.frame_count += 1

        if self.frame_count > self.trigger_frame:
            self.frame_count = 0
            self.dir = random.randint(0, 3)


        self.move()
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

        self.rect.x = max(0, min(self.rect.x, WORLD_WIDTH  - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, WORLD_HEIGHT - self.rect.height))
