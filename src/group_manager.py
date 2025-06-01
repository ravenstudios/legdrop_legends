import pygame
from constants import *
import player
import block
import camera
class GroupManager():


    def __init__(self):
        self.player = player.Player()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.blocks_group = pygame.sprite.Group()
        self.camera = camera.Camera()

    def update(self):

        cam_offset = self.camera.update_offset(self.player)
        self.player_group.update(cam_offset)
        self.blocks_group.update(cam_offset)

    def draw(self, surface):
        self.player_group.draw(surface)
        self.blocks_group.draw(surface)
