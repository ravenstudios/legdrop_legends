import main_entity
import pygame
from constants import *
import os

class EnemyBattleObject(main_entity.Main_entity):

    def __init__(self, x, y, spritesheet, max_frame):
        self.x, self.y = x, y
        self.width = 64 * SCALE
        self.height = 64 * SCALE
        super().__init__(self.x, self.y, self.width, self.height)

        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(os.path.dirname(__file__), BASE_DIR, "assets", "images", spritesheet)
        self.spritesheet = pygame.image.load(path).convert_alpha()
        scaled_width, scaled_height = self.spritesheet.get_size()
        self.spritesheet = pygame.transform.scale(self.spritesheet, (scaled_width * SCALE * 2, scaled_height * SCALE * 2))

        self.max_frame = max_frame - 1
        self.animation_speed = 10
        self.y_sprite_sheet_index = 0

        self.hp = 0
        self.mp = 0
        self.max_hp = 0
        self.max_mp = 0

        self.options = {
            "Attacks": [
                {"name": "", "dmg": 0, "cost": 0, "type":"attack", "message":""},
                {"name": "Back"}
            ],
            "Items": [
                {"name": "", "hp": 0, "type":"restore_hp", "message":""},
                {"name": "", "mp": 0, "type":"restore_mp", "message":""},
                {"name": ""}
            ],
            "Powder": [
                {"name": "Powder", "mp": 0, "type":"restore_mp", "message":""},
                {"name": "Back"},
            ],
            "Tag Partner": [
                {"name": "Tag Partner", "type":"tag", "message":"Player tagged"},
                {"name": "Back"},

            ],

        }
