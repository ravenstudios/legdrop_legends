from objects.main_entity import MainEntity
import pygame
from constants import *
import os
import random


class BattleObject(MainEntity):

    def __init__(self, x, y, spritesheet, max_frame):
        self.x, self.y = x, y
        self.width = 64 * SCALE
        self.height = 64 * SCALE
        super().__init__(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.orignal_rect = self.rect.copy()
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Goes from src/objects/ → src/
        ASSET_DIR = os.path.join(BASE_DIR, "../assets/images")
        path = os.path.normpath(os.path.join(ASSET_DIR, spritesheet))
        self.spritesheet = pygame.image.load(path).convert_alpha()
        scaled_width, scaled_height = self.spritesheet.get_size()
        self.spritesheet = pygame.transform.scale(self.spritesheet, (scaled_width * SCALE * 2, scaled_height * SCALE * 2))
        self.max_frame = max_frame - 1
        self.animation_speed = 10
        self.y_sprite_sheet_index = 0
        self.orginal_pos_rect = self.rect.copy()
        self.can_shake = False
        self.shake_movement = 5
        self.lunge_dir = (0,0)
        self.is_lunging = False
        self.lunge_distance = 400  # pixels
        self.lunge_speed = 40      # pixels per frame
        self.lunge_forward = True
        self.lunge_offset = 0
        self.hp = 0
        self.death_animation_speed = 5
        self.is_dead = False

    def update(self):
        self.hp = max(0, self.hp)
        if self.can_shake:
            self.shake()

        self.lunge()
        if self.is_dead:
            self.death_animation()
        super().update()



    def set_shake(self, do_shake):
        if not self.can_shake and do_shake:
            self.orginal_pos_rect = self.rect.copy()
            self.can_shake = True
        elif not do_shake:
            self.can_shake = False
            self.rect = self.orginal_pos_rect.copy()


    def shake(self):
        x = random.randint(-self.shake_movement, self.shake_movement)
        y = random.randint(-self.shake_movement, self.shake_movement)
        self.rect = self.rect.move(x, y)


    def start_lunge(self, target):
        if not self.is_lunging:
            self.is_lunging = True
            self.lunge_forward = True
            self.lunge_offset = 0

            # Get direction vector toward the opponent's center
            dx = target.rect.centerx - self.rect.centerx
            dy = target.rect.centery - self.rect.centery

            # Normalize to get unit direction
            length = max((dx ** 2 + dy ** 2) ** 0.5, 1)  # avoid divide by 0
            self.lunge_dir = (dx / length, dy / length)


    def lunge(self):
        if self.is_lunging:
            dx = self.lunge_dir[0] * self.lunge_speed
            dy = self.lunge_dir[1] * self.lunge_speed

            if self.lunge_forward:
                self.rect.x += dx
                self.rect.y += dy
                self.lunge_offset += self.lunge_speed

                if self.lunge_offset >= self.lunge_distance:
                    self.lunge_forward = False  # Start returning

            else:  # returning
                self.rect.x -= dx
                self.rect.y -= dy
                self.lunge_offset -= self.lunge_speed

                if self.lunge_offset <= 0:
                    self.rect = self.orginal_pos_rect.copy()
                    self.is_lunging = False


    def reset(self):
        self.rect = self.orignal_rect.copy()
        self.is_dead = False
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.is_poisoned = False

    def death_animation(self):
        self.rect.y += self.death_animation_speed
