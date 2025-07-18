import pygame
from constants import *
from event_system import event_system


class CollisionHandler:
    def __init__(self, player):
        self.player = player

        self.direction_to_collision_fix = {
            0: lambda player, obj: setattr(player.rect, 'bottom', obj.rect.top),    # moving down
            1: lambda player, obj: setattr(player.rect, 'top', obj.rect.bottom),    # moving up
            2: lambda player, obj: setattr(player.rect, 'right', obj.rect.left),    # moving right
            3: lambda player, obj: setattr(player.rect, 'left', obj.rect.right),    # moving left
        }

    def push_player_away_from_npc(self, npc, distance=10):
        # Vector from npc center to player center
        dx = self.player.rect.centerx - npc.rect.centerx
        dy = self.player.rect.centery - npc.rect.centery
        dist = max((dx**2 + dy**2)**0.5, 0.1)  # avoid zero division
        offset_x = int(dx / dist * distance)
        offset_y = int(dy / dist * distance)
        self.player.rect = self.player.rect.move(offset_x, offset_y)

    def update(self, groups):
        obj_group, door_group, npc_group, map_group = groups

        old_x = self.player.x
        old_y = self.player.y

        # Door collisions
        if door_group:
            door_collisions = pygame.sprite.spritecollide(self.player, door_group, False)
            if door_collisions:
                door = door_collisions[0]
                if door.is_exit:
                    self.player.leaving_submap = True
                elif door.is_entrance:
                    self.player.in_submap = True
                    self.player.prev_cords = (
                        self.player.rect.copy().move(0, BLOCK_SIZE // 8),
                        (self.player.x, self.player.y)
                    )
                event_system.raise_event("load_map", door.map_file)

        # Object collisions (walls, obstacles)
        if obj_group:
            obj_collisions = pygame.sprite.spritecollide(self.player, obj_group, False)
            if obj_collisions:
                for obj in obj_collisions:
                    fix = self.direction_to_collision_fix.get(self.player.dir)
                    if fix:
                        fix(self.player, obj)
                self.player.x = old_x
                self.player.y = old_y

        # NPC collisions — block movement
        if npc_group:
            npc_collisions = pygame.sprite.spritecollide(self.player, npc_group, False)
            if npc_collisions:
                for npc in npc_collisions:
                    fix = self.direction_to_collision_fix.get(self.player.dir)
                    if fix:
                        fix(self.player, npc)
                self.player.x = old_x
                self.player.y = old_y

        # NPC dialog interaction — separate from collision
        if npc_group:
            for npc in npc_group:
                interaction_zone = npc.rect.inflate(20, 20)  # 20 px bigger for easier interaction
                if interaction_zone.colliderect(self.player.rect):

                    if self.player.action_button_pressed and not getattr(self.player, "in_dialog", False):
                        self.player.in_dialog = True
                        event_system.raise_event("dialog_set_visible", True)
                        event_system.raise_event("dialog_start_chat", npc)
                        self.push_player_away_from_npc(npc)
                        break  # Only trigger for one NPC at a time
