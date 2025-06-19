import main_entity
import pygame
from constants import *
import os

class EnemyBattleObject(main_entity.Main_entity):

    def __init__(self):
        self.x, self.y = 500, 50


        # Set width and height to 90x61
        self.width = 64 * SCALE * 2
        self.height = 64 * SCALE * 2
        super().__init__(self.x, self.y, self.width, self.height, "Brother64x64-Sheet.png")
        # Recreate the image with the correct dimensions
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha()  # Ensure transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        # Load and scale the spritesheet to fit within 90x61
        path = os.path.join(os.path.dirname(__file__), "..", "assets/images/Brother64x64-Sheet.png")
        self.spritesheet = pygame.image.load(path).convert_alpha()
        scaled_width, scaled_height = self.spritesheet.get_size()
        self.spritesheet = pygame.transform.scale(self.spritesheet, (scaled_width * SCALE * 2, scaled_height * SCALE * 2))

        # Set animation parameters
        self.max_frame = 34
        self.animation_speed = 10

        self.y_sprite_sheet_index = 0
        self.hp = 50
        self.mp = 30
        self.max_hp = 75
        self.max_mp = 50
        self.img_path = "d"
        self.moves = [
                {
                    "name": "Chop",
                    "dmg": 5,
                },
                {
                    "name": "Kick",
                    "dmg": 5,
                }

            ]
