import pygame
from constants import *

class MovementHandler():

    def __init__(self, player):
        self.player = player
        self.can_move_x_left = False


    def key_handler(self, joystick, obj_group=None):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move_up(obj_group)

        elif keys[pygame.K_RIGHT]:
            self.move_right(obj_group)

        elif keys[pygame.K_LEFT]:
            self.move_left(obj_group)

        elif keys[pygame.K_DOWN]:
            self.move_down(obj_group)

        elif keys[pygame.K_RETURN]:
            self.action_button()

        if self.player.joystick:
            if  joystick.get_button(12):
                self.move_down(obj_group)

            elif joystick.get_button(13):
                self.move_left(obj_group)

            elif joystick.get_button(14):
                self.move_right(obj_group)

            elif joystick.get_button(11):
                self.move_up(obj_group)

            elif joystick.get_button(0):
                self.action_button()

        self.player.action_button_pressed = False


    def move_up(self, obj_group):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 1
        p.y_sprite_sheet_index = 1

        if cy + p.speed >= half_screen_h and 0 < p.y < wbe:
            if self.can_move_camera(obj_group):
                p.y -= p.speed
        elif  cy < half_screen_h and half_screen_h < p.y < wbe + p.speed:
            if self.can_move_camera(obj_group):
                p.y -= p.speed
        if p.y == 0 or p.y > wbe:
            p.rect.y -= p.speed


    def move_down(self, obj_group):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 0
        p.y_sprite_sheet_index = 0
        if cy > half_screen_h and p.y < wbe:
            if self.can_move_camera(obj_group):
                p.y += p.speed
        if cy < half_screen_h or p.y > wbe:
            p.rect.y += p.speed


    def move_right(self, obj_group):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 2
        p.y_sprite_sheet_index = 2
        if cx >= half_screen_w and p.x <= wre:
            if self.can_move_camera(obj_group):
                p.x += p.speed
        if cx <= half_screen_w or p.x >= wre:
            p.rect.x += p.speed


    def move_left(self, obj_group):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 3
        p.y_sprite_sheet_index = 3
        if self.can_move_x_left:
            if self.can_move_camera(obj_group):
                p.x -= p.speed
        if p.x == 0 or p.x >= wre and cx >= half_screen_w:
            self.can_move_x_left = False
            p.rect.x -= p.speed
        else:
            self.can_move_x_left = True


    def action_button(self):
        self.player.action_button_pressed = True


    def can_move_camera(self, obj_group):
        # rect = None
        # if self.player.dir == 1:
        #     rect = self.player.rect.move(0, -self.player.speed)
        # if self.player.dir == 2:
        #     rect = self.player.rect.move(self.player.speed, 0)
        # if self.player.dir == 3:
        #     rect = self.player.rect.move(-self.player.speed, 0)
        # if self.player.dir == 0:
        #     rect = self.player.rect.move(0, self.player.speed)
        #
        # temp_sprite = pygame.sprite.Sprite()
        # temp_sprite.rect = rect
        # collisions = pygame.sprite.spritecollideany(temp_sprite, obj_group)
        # if not collisions:
        #     return True
        #     prrint("true")
        # else:
        #     return False

        return True
    def get_movement_context(self):
        p = self.player
        cx, cy = p.rect.center
        half_screen_w = GAME_WIDTH // 2
        half_screen_h = GAME_HEIGHT // 2
        wre = WORLD_WIDTH - GAME_WIDTH - p.speed
        wbe = WORLD_HEIGHT - GAME_HEIGHT - p.speed
        return p, cx, cy, half_screen_w, half_screen_h, wre, wbe
