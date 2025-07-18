from states.state import State
import pygame
from constants import *
from player.player import main_player
from objects.block import Block
from objects.camera import Camera
from objects.npc import NPC
import map
from wrestlers.crawdaddy import Crawdaddy
from wrestlers.clown import Clown
from wrestlers.brother import Brother
import dialog_display
from menu import menu
from npcs.nurse import Nurse


class InsideState(State):
    def __init__(self, event_system, joystick=None):
        self.joystick = joystick
        self.event_system = event_system
        self.event_system.on("load_map", self.load_map)
        self.dialog_display = dialog_display.DialogDisplay(self.event_system)
        self.dialog_display_group = pygame.sprite.Group()
        self.dialog_display_group.add(self.dialog_display)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(main_player)
        self.map_group = pygame.sprite.Group()
        self.obj_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        self.npc_group = pygame.sprite.Group()
        # self.npc_group.add(Crawdaddy(), Clown(), Brother(), Nurse())
        self.camera = Camera(self.event_system)
        self.map = map.Map()
        # self.load_map("clinic.tmx")
        self.groups = [self.obj_group, self.door_group, self.npc_group, self.map_group]
        self.state_name = "world"
        self.menu = menu.Menu()
        self.song = "town.mp3"



    def events(self, events):
        pass
        # self.dialog_display.events(events)

    def update(self):
        cam_offset = self.camera.update_offset(main_player)
        self.map_group.update(cam_offset)
        self.obj_group.update(cam_offset)
        self.player_group.update(cam_offset, self.groups)
        self.npc_group.update(cam_offset, self.map_group)
        self.door_group.update(cam_offset)
        self.dialog_display.update()
        self.menu.update()


    def draw(self, surface):
        self.map_group.draw(surface)
        self.npc_group.draw(surface)
        self.player_group.draw(surface)
        if self.dialog_display.is_visible:
            self.dialog_display_group.draw(surface)
        if self.menu.is_visible:
            self.menu.draw(surface)


    def load_map(self, map_file):
        self.map_group, self.obj_group, self.door_group, spawn_point, self.npc_group = self.map.load_map(map_file)
        main_player.move_to_new_map(spawn_point)
        self.groups = [self.obj_group, self.door_group, self.npc_group, self.map_group]
