import pygame
from constants import *

class CollisionHandler():

    def __init__(self, player):
        self.player = player
        self.direction_to_collision_fix = {
            0: lambda player, obj: setattr(player.rect, 'bottom', obj.rect.top),    # moving down
            1: lambda player, obj: setattr(player.rect, 'top', obj.rect.bottom),    # moving up
            2: lambda player, obj: setattr(player.rect, 'right', obj.rect.left),    # moving right
            3: lambda player, obj: setattr(player.rect, 'left', obj.rect.right),    # moving left
        }

    def update(self, map_group):
        old_x = self.player.x
        old_y = self.player.y

        collisions = pygame.sprite.spritecollide(self.player, map_group, False, collided = None)
        if collisions:
            for obj in collisions:
                fix = self.direction_to_collision_fix.get(self.player.dir)
                if fix:
                    fix(self.player, obj)
            self.player.x = old_x
            self.player.y = old_y
