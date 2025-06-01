import main_entity
import pygame
from constants import *


class Player(main_entity.Main_entity):

    def __init__(self):
        self.x = 0
        self.y = 0
        super().__init__(self.x, self.y, "Brother16x16-Sheet.png")
        self.y_sprite_sheet_index = 0
        self.speed = 7

    def update(self, cam_offset):
        # self.update_cam_offset(0)
        self.key_handler(cam_offset)
        self.animate()
        self.rect.x = max(0, min(self.rect.x, GAME_WIDTH  - self.rect.width))
        self.rect.y = max(0, min(self.rect.top, GAME_HEIGHT - self.rect.height))
        # print(f"X:{self.x}")

    def key_handler(self, cam_offset):
        # print(cam_offset)
        half_screen_w = GAME_WIDTH // 2
        half_screen_h = GAME_HEIGHT // 2
        world_right_edge = WORLD_WIDTH - GAME_WIDTH - self.speed
        world_bottom_edge = WORLD_WIDTH - GAME_HEIGHT - self.speed
        # print(world_right_edge)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
                self.y_sprite_sheet_index = 1

                if self.rect.center[1] + self.speed >= half_screen_h and 0 < self.y < world_bottom_edge:
                    self.y -= self.speed
                elif  self.rect.center[1] < half_screen_h and half_screen_h < self.y < world_bottom_edge + self.speed:
                    self.y -= self.speed
                if self.y == 0 or self.y > world_bottom_edge:
                    self.rect.y -= self.speed

        if keys[pygame.K_RIGHT]:
            self.y_sprite_sheet_index = 2

            if self.rect.center[0] > half_screen_w and self.x < world_right_edge:
                self.x += self.speed
            if self.rect.center[0] < half_screen_w or self.x > world_right_edge:
                self.rect.x += self.speed


        if keys[pygame.K_LEFT]:
            self.y_sprite_sheet_index = 3

            if self.rect.center[0] + self.speed >= half_screen_w and 0 < self.x < world_right_edge:
                self.x -= self.speed
            elif  self.rect.center[0] < half_screen_w and half_screen_w < self.x < world_right_edge + self.speed:
                self.x -= self.speed
            if self.x == 0 or self.x > world_right_edge:
                self.rect.x -= self.speed



        if keys[pygame.K_DOWN]:
            self.y_sprite_sheet_index = 0
            if self.rect.center[1] > half_screen_h and self.y < world_bottom_edge:
                self.y += self.speed
            if self.rect.center[1] < half_screen_h or self.y > world_bottom_edge:
                self.rect.y += self.speed
