from objects.main_entity import MainEntity
import pygame
from constants import *

class Block(MainEntity):

    def __init__(self, x, y, w=BLOCK_SIZE, h=BLOCK_SIZE, color=(255, 0, 255)):
        self.x = x
        self.y = y

        self.width = w
        self.height = h
        super().__init__(self.x, self.y, self.width, self.height, "Gym_building.png")

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.animation_speed = 0

    def update(self, cam_offset=0):
        # self.animate()
        self.update_cam_offset(cam_offset)
