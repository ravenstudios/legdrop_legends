import pygame
from constants import *
import player
import block
import camera
import npc
import map
import wrestlers.crawdaddy
import wrestlers.clown

class GroupManager():


    def __init__(self, state_manager, joystick=None):
        self.joystick = joystick
        self.map = map.Map("town1.tmx")

        self.map_group, self.obj_group, self.door_group = self.map.load_map()

        self.player = player.Player(self.joystick)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.clown = wrestlers.clown.Clown()
        self.crawdaddy = wrestlers.crawdaddy.Crawdaddy()
        self.npc_group = pygame.sprite.Group()
        # self.npc_group.add(self.crawdaddy, self.clown)
        self.camera = camera.Camera()
        self.state_manager = state_manager

    def load_map(self, map_file):
        print("load map")
        self.map = map.Map(map_file)
        self.map_group, self.obj_group, self.door_group = self.map.load_map()

    def update(self):
        cam_offset = self.camera.update_offset(self.player)
        self.map_group.update(cam_offset)
        self.obj_group.update(cam_offset)
        self.player_group.update(cam_offset, self.obj_group, self.npc_group, self.state_manager, self)
        self.npc_group.update(cam_offset, self.map_group)

    def draw(self, surface):
        self.map_group.draw(surface)
        # self.obj_group.draw(surface)
        self.npc_group.draw(surface)
        self.player_group.draw(surface)
