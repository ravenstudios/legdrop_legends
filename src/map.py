import pygame
import pytmx
import os


import json
import pygame
import block
import csv
from constants import *
from tile_sprites import TileSprite

class Map:
    def __init__(self, tmx_file):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/maps", tmx_file)
        self.tmx_data = pytmx.load_pygame(path)

        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight
        self.tile_group = pygame.sprite.Group()

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
                    image = self.tmx_data.get_tile_image_by_gid(gid)
                    if image:
                        tile = TileSprite(image, x * self.tile_width, y * self.tile_height)
                        self.tile_group.add(tile)
        return self.tile_group
