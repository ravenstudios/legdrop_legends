import pygame
from constants import *
import player
import block
import camera
import npc
import map
class GroupManager():


    def __init__(self):
        self.map = map.Map()
        self.map_group = self.map.tile_group

        self.player = player.Player()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.npc = npc.NPC()
        self.npc_group = pygame.sprite.Group()
        self.npc_group.add(self.npc)

        self.blocks_group = pygame.sprite.Group()

        self.camera = camera.Camera()

    def update(self):

        cam_offset = self.camera.update_offset(self.player)
        self.map_group.update(cam_offset)
        self.blocks_group.update(cam_offset)
        self.player_group.update(cam_offset, self.map_group)
        self.npc_group.update(cam_offset, self.map_group)

    def draw(self, surface):
        self.map_group.draw(surface)

        self.blocks_group.draw(surface)
        self.npc_group.draw(surface)
        self.player_group.draw(surface)
