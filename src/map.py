import pygame
import pytmx
import os
import block
import door
from constants import *
import constants
from tile_sprites import TileSprite

class Map:
    def __init__(self):
        pass


    def load_map(self, tmx_file):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/maps", tmx_file)
        self.tmx_data = pytmx.load_pygame(path)
        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight
        self.width = self.tmx_data.width
        self.height = self.tmx_data.height
        constants.WORLD_WIDTH = self.width * BLOCK_SIZE
        constants.WORLD_HEIGHT = self.height * BLOCK_SIZE
        self.tile_group = pygame.sprite.Group()
        self.obj_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        self.visible_layers = list(self.tmx_data.visible_layers)
        self.spawn_point = (0, 0)
        self.current_map_file = ""

        x_offset = max((GAME_WIDTH - constants.WORLD_WIDTH) // 8, 0)
        y_offset = max((GAME_HEIGHT - constants.WORLD_HEIGHT) // 8, 0)

        for layer in self.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    image = self.tmx_data.get_tile_image_by_gid(gid)
                    if image:
                        tile = TileSprite(image, x * self.tile_width + x_offset, y * self.tile_height + y_offset)
                        self.tile_group.add(tile)

        for i, obj in enumerate(self.tmx_data.objects):
            x = int(obj.x * 4 + x_offset * 4)
            y = int(obj.y * 4 + y_offset * 4)
            w = int(obj.width * 4)
            h = int(obj.height * 4)
            map_file = ""

            if "spawn_point" in obj.properties:
                self.spawn_point = (x, y)

            if "block" in obj.properties:
                self.obj_group.add(block.Block(x, y, w, h))

            if "door" in obj.properties:
                # if "map_file" in obj.properties:
                #     map_file = obj.properties["map_file"]
                #     self.door_group.add(
                #         door.Door(x, y, w, h, map_file, False)
                #     )
                if "exit" in obj.properties:
                    print("exit")
                    map_file = obj.properties["map_file"]
                    self.door_group.add(
                        door.Door(x, y, w, h, map_file, True)
                    )
                else:
                    map_file = obj.properties["map_file"]
                    self.door_group.add(
                        door.Door(x, y, w, h, map_file, False)
                    )


        return [self.tile_group, self.obj_group, self.door_group, self.spawn_point]
