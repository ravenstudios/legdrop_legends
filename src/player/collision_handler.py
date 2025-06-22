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

    def update(self, groups):
        obj_group, door_group, npc_group, map_group = groups
        old_x = self.player.x
        old_y = self.player.y
        if door_group:
            door_collisions = pygame.sprite.spritecollide(self.player, door_group, False, collided = None)
            if door_collisions:
                if door_collisions[0].is_exit:
                    self.player.leaving_submap = True

                elif door_collisions[0].is_entrance:
                    self.player.in_submap = True
                    self.player.prev_cords = (
                        self.player.rect.copy().move(0, BLOCK_SIZE // 8),
                        (self.player.x, self.player.y)
                    )
                self.player.event_system.raise_event("load_map", door_collisions[0].map_file)
        if obj_group:
            obj_collisions = pygame.sprite.spritecollide(self.player, obj_group, False, collided = None)
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
            npc = npc_collisions[0]
            if self.player.action_button_pressed:
                self.player.event_system.raise_event("set_visible", True)
                self.player.event_system.raise_event("change_dialog", npc.dialog)
