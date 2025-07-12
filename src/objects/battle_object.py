from objects.main_entity import MainEntity
import pygame
from constants import *
import os
import random


class BattleObject(MainEntity):

    def __init__(self, x, y, spritesheet, max_frame):
        self.x, self.y = x, y
        self.width = 64 * SCALE
        self.height = 64 * SCALE
        super().__init__(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Goes from src/objects/ → src/
        ASSET_DIR = os.path.join(BASE_DIR, "../assets/images")
        path = os.path.normpath(os.path.join(ASSET_DIR, spritesheet))
        self.spritesheet = pygame.image.load(path).convert_alpha()
        scaled_width, scaled_height = self.spritesheet.get_size()
        self.spritesheet = pygame.transform.scale(self.spritesheet, (scaled_width * SCALE * 2, scaled_height * SCALE * 2))
        self.max_frame = max_frame - 1
        self.animation_speed = 10
        self.y_sprite_sheet_index = 0
        self.orginal_pos_rect = self.rect.copy()
        self.can_shake = False
        self.shake_movement = 5



    # def set_shake(self, bool):
    #     if not self.can_shake and bool:
    #         self.orginal_pos_rect = self.rect.copy()
    #         self.can_shake = bool
    #         return
    #     elif not bool:
    #         self.can_shake = bool
    #         self.rect = self.orginal_pos_rect.copy()
    def set_shake(self, do_shake):
        if not self.can_shake and do_shake:
            self.orginal_pos_rect = self.rect.copy()  # ← COPY, not reference
            self.can_shake = True
        elif not do_shake:
            self.can_shake = False
            self.rect = self.orginal_pos_rect.copy()  # ← COPY again for safety


    def shake(self):
        if self.can_shake:
            x = random.randint(-self.shake_movement, self.shake_movement)
            y = random.randint(-self.shake_movement, self.shake_movement)
            self.rect = self.rect.move(x, y)
