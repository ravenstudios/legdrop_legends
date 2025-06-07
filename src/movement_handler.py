import pygame
from constants import *

class MovementHandler():

    def __init__(self, player):
        self.player = player
        self.can_move_x_left = False

    def key_handler(self, map_group):
        half_screen_w = GAME_WIDTH // 2
        half_screen_h = GAME_HEIGHT // 2

        # world_right_edge
        wre = WORLD_WIDTH - GAME_WIDTH - self.player.speed
        # world_bottom_edge
        wbe = WORLD_HEIGHT - GAME_HEIGHT - self.player.speed
        cx, cy = self.player.rect.center
        p = self.player
        pssi = p.y_sprite_sheet_index

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            p.dir = 1
            p.y_sprite_sheet_index = 1

            if cy + p.speed >= half_screen_h and 0 < p.y < wbe:
                if self.can_move_camera(map_group):
                    p.y -= p.speed
            elif  cy < half_screen_h and half_screen_h < p.y < wbe + p.speed:
                if self.can_move_camera(map_group):
                    p.y -= p.speed
            if p.y == 0 or p.y > wbe:
                p.rect.y -= p.speed

        elif keys[pygame.K_RIGHT]:
            p.dir = 2
            p.y_sprite_sheet_index = 2

            if cx >= half_screen_w and p.x <= wre:
                if self.can_move_camera(map_group):
                    p.x += p.speed
            if cx <= half_screen_w or p.x >= wre:
                p.rect.x += p.speed

        elif keys[pygame.K_LEFT]:
            p.dir = 3
            p.y_sprite_sheet_index = 3
            if self.can_move_x_left:
                if self.can_move_camera(map_group):
                    p.x -= p.speed
            if p.x == 0 or p.x >= wre and cx >= half_screen_w:
                self.can_move_x_left = False
                p.rect.x -= p.speed
            else:
                self.can_move_x_left = True

        elif keys[pygame.K_DOWN]:
            p.dir = 0
            p.y_sprite_sheet_index = 0
            if cy > half_screen_h and p.y < wbe:
                if self.can_move_camera(map_group):
                    p.y += p.speed
            if cy < half_screen_h or p.y > wbe:
                p.rect.y += p.speed

    def can_move_camera(self, map_group):
        rect = None
        if self.player.dir == 1:
            rect = self.player.rect.move(0, -self.player.speed)
        if self.player.dir == 2:
            rect = self.player.rect.move(self.player.speed, 0)
        if self.player.dir == 3:
            rect = self.player.rect.move(-self.player.speed, 0)
        if self.player.dir == 0:
            rect = self.player.rect.move(0, self.player.speed)

        temp_sprite = pygame.sprite.Sprite()
        temp_sprite.rect = rect
        collisions = pygame.sprite.spritecollideany(temp_sprite, map_group)
        if not collisions:
            return True
        else:
            return False
