import pygame
import pytmx
import os
import block
import door
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
        self.visible_layers = list(self.tmx_data.visible_layers)

    def load_map(self):
        for layer in self.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    image = self.tmx_data.get_tile_image_by_gid(gid)
                    if image:
                        tile = TileSprite(image, x * self.tile_width, y * self.tile_height)
                        self.tile_group.add(tile)

        for i, obj in enumerate(self.tmx_data.objects):
            if "block" in obj.properties:
                x, y = int(obj.x), int(obj.y)
                self.obj_group.add(block.Block(x * 4, y * 4, obj.width * 4, obj.height * 4))

            if "map_file" in obj.properties:
                map_file = obj.properties["map_file"]
                x, y = int(obj.x), int(obj.y)
                self.door_group.add(
                    door.Door(x * 4, y * 4, obj.width * 4, obj.height * 4, map_file=map_file)
                )
        return [self.tile_group, self.obj_group, self.door_group]
