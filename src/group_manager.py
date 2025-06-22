import pygame
from constants import *
import player
import block
import camera
import npc
import map
import wrestlers.crawdaddy
import wrestlers.clown
import dialog_display
class GroupManager():


    def __init__(self, state_manager, event_system, joystick=None):
        self.joystick = joystick
        self.event_system = event_system

        self.dialog_display = dialog_display.DialogDisplay(self.event_system)
        self.dialog_display_group = pygame.sprite.Group()
        self.dialog_display_group.add(self.dialog_display)


        self.player = player.Player(self.event_system, self.joystick)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.clown = wrestlers.clown.Clown(self.event_system)
        self.crawdaddy = wrestlers.crawdaddy.Crawdaddy(self.event_system)
        self.npc_group = pygame.sprite.Group()
        self.npc_group.add(self.crawdaddy, self.clown)
        self.camera = camera.Camera(self.event_system)
        self.state_manager = state_manager
        self.map = map.Map()
        self.load_map("town1.tmx")


    def load_map(self, map_file):
        self.map_group, self.obj_group, self.door_group, spawn_point = self.map.load_map(map_file)
        self.player.move_to_new_map(spawn_point)

    def update(self):
        cam_offset = self.camera.update_offset(self.player)
        self.map_group.update(cam_offset)
        self.obj_group.update(cam_offset)
        self.player_group.update(cam_offset, self.obj_group, self.npc_group, self.state_manager, self)
        self.npc_group.update(cam_offset, self.map_group)
        self.door_group.update(cam_offset)
        # self.dialog_display.update_text("this is a test")

    def draw(self, surface):
        self.map_group.draw(surface)
        # self.obj_group.draw(surface)
        self.npc_group.draw(surface)
        self.player_group.draw(surface)
        if self.dialog_display.is_visible:
            self.dialog_display_group.draw(surface)
        # self.door_group.draw(surface)
        # self.obj_group.draw(surface)
