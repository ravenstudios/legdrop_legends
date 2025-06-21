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

    def update(self, obj_group=None, npc_group=None, state_manager=None, group_manager=None):
        old_x = self.player.x
        old_y = self.player.y
        obj_collisions = pygame.sprite.spritecollide(self.player, obj_group, False, collided = None)
        door_collisions = pygame.sprite.spritecollide(self.player, group_manager.door_group, False, collided = None)



        if door_collisions:
            group_manager.load_map(door_collisions[0].map_file)
        if obj_collisions:
            for obj in obj_collisions:
                fix = self.direction_to_collision_fix.get(self.player.dir)
                if fix:
                    fix(self.player, obj)
            self.player.x = old_x
            self.player.y = old_y

        npc_collisions = None
        if npc_group:
            npc_collisions = pygame.sprite.spritecollide(self.player, npc_group, False)

        if npc_collisions:
            npc_collisions[0].change_state(state_manager, self.player)
