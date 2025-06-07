import main_entity
import pygame
from constants import *
import draw_text

class Block(main_entity.Main_entity):

    def __init__(self, x, y, color=(255, 0, 255)):

        self.draw_text = draw_text.DrawText()
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, "Brother16x16-Sheet.png")
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, cam_offset=0):
        self.update_cam_offset(cam_offset)
        self.draw_text.update_surface(f"x:{self.x}", 24, 0, 0, self.image)
        self.draw_text.update_surface(f"y:{self.y}", 24, 0, 16, self.image)
