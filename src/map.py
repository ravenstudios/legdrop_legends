import json
import pygame
import block
import csv
from constants import *


class Map():
    def __init__(self):
        self.tile_group = pygame.sprite.Group()
        self.map = self.load_csv_map("assets/maps/town1.csv")
        self.load_map(self.map, self.tile_group)

    def load_csv_map(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            map_data = [[int(tile) for tile in row] for row in reader]
        return map_data

    def load_map(self, map, group):
        for y, row in enumerate(map):
            for x, gid in enumerate(row):
                # print(f"Tile at ({x}, {y}) has GID: {gid}")
                if gid == 0:
                    group.add(block.Block(x * BLOCK_SIZE, y * BLOCK_SIZE,BLOCK_SIZE * 4, BLOCK_SIZE * 4, (255, 0, 255)))
        # self.map_width = self.tiled_map["width"]
        # self.map_height = self.tiled_map["height"]
        # self.tile_width = self.tiled_map["tilewidth"]
        # self.tile_height = self.tiled_map["tileheight"]
        #
        # for layer in self.tiled_map["layers"]:
        #     if layer["type"] == "tilelayer":
        #         print(f"Layer: {layer['name']}")
        #         data = layer["data"]  # 1D list of GIDs
        #         for row in range(self.map_height):
        #             for col in range(self.map_width):
        #                 index = row * self.map_width + col
        #                 gid = data[index]
        #                 print(f"Tile at ({col}, {row}) has GID: {gid}")
