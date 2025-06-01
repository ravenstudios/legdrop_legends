import pygame
from constants import *

class MovementHandler():

    def __init__(self, player):
        self.player = player

    def key_handler(self, cam_offset):
        # print(cam_offset)
        half_screen_w = GAME_WIDTH // 2
        half_screen_h = GAME_HEIGHT // 2
        world_right_edge = WORLD_WIDTH - GAME_WIDTH - self.player.speed
        world_bottom_edge = WORLD_WIDTH - GAME_HEIGHT - self.player.speed
        # print(world_right_edge)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
                self.player.y_sprite_sheet_index = 1

                if self.player.rect.center[1] + self.player.speed >= half_screen_h and 0 < self.player.y < world_bottom_edge:
                    self.player.y -= self.player.speed
                elif  self.player.rect.center[1] < half_screen_h and half_screen_h < self.player.y < world_bottom_edge + self.player.speed:
                    self.player.y -= self.player.speed
                if self.player.y == 0 or self.player.y > world_bottom_edge:
                    self.player.rect.y -= self.player.speed

        elif keys[pygame.K_RIGHT]:
            self.player.y_sprite_sheet_index = 2

            if self.player.rect.center[0] > half_screen_w and self.player.x < world_right_edge:
                self.player.x += self.player.speed
            if self.player.rect.center[0] < half_screen_w or self.player.x > world_right_edge:
                self.player.rect.x += self.player.speed


        elif keys[pygame.K_LEFT]:
            self.player.y_sprite_sheet_index = 3

            if self.player.rect.center[0] + self.player.speed >= half_screen_w and 0 < self.player.x < world_right_edge:
                self.player.x -= self.player.speed
            elif  self.player.rect.center[0] < half_screen_w and half_screen_w < self.player.x < world_right_edge + self.player.speed:
                self.player.x -= self.player.speed
            if self.player.x == 0 or self.player.x > world_right_edge:
                self.player.rect.x -= self.player.speed



        elif keys[pygame.K_DOWN]:
            self.player.y_sprite_sheet_index = 0
            if self.player.rect.center[1] > half_screen_h and self.player.y < world_bottom_edge:
                self.player.y += self.player.speed
            if self.player.rect.center[1] < half_screen_h or self.player.y > world_bottom_edge:
                self.player.rect.y += self.player.speed
