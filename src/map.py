import pygame
import pytmx
import os


import json
import pygame
import block
import door
import csv
from constants import *
import constants
from tile_sprites import TileSprite

class Map:
    def __init__(self, tmx_file):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/maps", tmx_file)
        self.tmx_data = pytmx.load_pygame(path)

        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight
        constants.WORLD_WIDTH = self.tmx_data.width * BLOCK_SIZE
        constants.WORLD_HEIGHT = self.tmx_data.height * BLOCK_SIZE
        self.tile_group = pygame.sprite.Group()
        self.obj_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        # Convert the generator to a list so it can be reused
        self.visible_layers = list(self.tmx_data.visible_layers)


    # def draw(self, surface):
    #     for layer in self.tmx_data.visible_layers:
    #         if isinstance(layer, pytmx.TiledTileLayer):
    #             for x, y, gid in layer:
    #                 tile = self.tmx_data.get_tile_image_by_gid(gid)
    #                 print(f"gid:{gid}")
    #                 if tile:
    #                     surface.blit(tile, (x * self.tile_width, y * self.tile_height))
    def load_map(self):
        for layer in self.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    if gid == 0:
                        continue  # skip empty tile

                    tile_props = self.tmx_data.get_tile_properties_by_gid(gid)

                    if tile_props and tile_props.get("block"):
                        self.obj_group.add(block.Block(x * BLOCK_SIZE, y * BLOCK_SIZE))
                    if tile_props and tile_props.get("door") and tile_props.get("map"):
                        print("good")
                        self.door_group.add(block.Block(x * BLOCK_SIZE, y * BLOCK_SIZE, map=tile_props.get("map")))
                    image = self.tmx_data.get_tile_image_by_gid(gid)
                    if image:
                        tile = TileSprite(image, x * self.tile_width, y * self.tile_height)
                        self.tile_group.add(tile)
        # for obj in self.tmx_data.objects:
        #     if obj.type == "door":
        #
        #         self.door_group.add(door)

        print(f"doors:{self.door_group}")
        return [self.tile_group, self.obj_group, self.door_group]
