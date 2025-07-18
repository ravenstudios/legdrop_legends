import pygame
from constants import *
import constants
from event_system import event_system

class MovementHandler():

    def __init__(self, player):
        self.player = player
        self.can_move_x_left = False
        event_system.on("move_up", self.move_up)
        event_system.on("move_down", self.move_down)
        event_system.on("move_right", self.move_right)
        event_system.on("move_left", self.move_left)
        event_system.on("action_button_pressed", self.action_button_pressed)
        event_system.on("action_button_released", self.action_button_released)

        self.obj_group = None


    def update(self, obj_group):
        self.obj_group = obj_group


    def move_up(self):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 1
        p.y_sprite_sheet_index = 1

        if cy <= half_screen_h and p.y > 0:
            # Move camera up
            if self.can_move_camera():
                p.y -= p.speed
        elif p.rect.top > 0:
            # Move player sprite up
            p.rect.y -= p.speed


    def move_down(self):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 0
        p.y_sprite_sheet_index = 0
        if cy > half_screen_h and p.y < wbe:
            if self.can_move_camera():
                p.y += p.speed
        if cy < half_screen_h or p.y > wbe:
            p.rect.y += p.speed


    def move_right(self):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 2
        p.y_sprite_sheet_index = 2
        if cx >= half_screen_w and p.x <= wre:
            if self.can_move_camera():
                p.x += p.speed
        if cx <= half_screen_w or p.x >= wre:
            p.rect.x += p.speed


    def move_left(self):
        p, cx, cy, half_screen_w, half_screen_h, wre, wbe = self.get_movement_context()
        p.dir = 3
        p.y_sprite_sheet_index = 3
        if self.can_move_x_left:
            if self.can_move_camera():
                p.x -= p.speed
        if p.x == 0 or p.x >= wre and cx >= half_screen_w:
            self.can_move_x_left = False
            p.rect.x -= p.speed
        else:
            self.can_move_x_left = True


    def action_button_pressed(self):
        self.player.action_button_pressed = True

    def action_button_released(self):
        self.player.action_button_pressed = False


    def can_move_camera(self):
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
        collisions = pygame.sprite.spritecollideany(temp_sprite, self.obj_group)
        if not collisions:
            return True
        else:
            return False


    def get_movement_context(self):
        p = self.player
        cx, cy = p.rect.center
        half_screen_w = GAME_WIDTH // 2
        half_screen_h = GAME_HEIGHT // 2
        wre = constants.WORLD_WIDTH - GAME_WIDTH - p.speed
        wbe = constants.WORLD_HEIGHT - GAME_HEIGHT - p.speed
        return p, cx, cy, half_screen_w, half_screen_h, wre, wbe
