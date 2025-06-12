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

    def update(self, map_group=None, npc_group=None, state_manager=None):
        old_x = self.player.x
        old_y = self.player.y

        map_collisions = pygame.sprite.spritecollide(self.player, map_group, False, collided = None)
        if map_collisions:
            for obj in map_collisions:
                fix = self.direction_to_collision_fix.get(self.player.dir)
                if fix:
                    fix(self.player, obj)
            self.player.x = old_x
            self.player.y = old_y

        npc_collisions = None
        if npc_group:
            npc_collisions = pygame.sprite.spritecollide(self.player, npc_group, False)

        if npc_collisions:
            state_manager.current_state = state_manager.battle
