import main_entity
import pygame
from constants import *

class Door(main_entity.Main_entity):

    def __init__(self, x, y, w, h, map_file, is_exit):
        self.x = x
        self.y = y
        self.is_exit = is_exit
        self.width = w
        self.height = h
        super().__init__(self.x, self.y, self.width, self.height, "Gym_building.png")

        self.image = pygame.Surface([self.width, self.height])
        # self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.animation_speed = 0
        self.map_file = map_file
    def update(self, cam_offset=0):

        # self.animate()
        self.update_cam_offset(cam_offset)
        # print(self.rect)
