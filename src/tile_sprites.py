import pygame
from constants import *
class TileSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        scaled_width, scaled_height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (scaled_width * 4, scaled_height * 4))

        self.x = x  * 4
        self.y = y  * 4
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE



        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)



    def update(self, cam_offset=None):
        if cam_offset:
            self.rect.x = self.x + cam_offset[0]
            self.rect.y = self.y + cam_offset[1]
