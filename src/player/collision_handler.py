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
        self.player.interaction_zone = pygame.Rect(0, 0, 0, 0)
        self.player.dialog_cooldown = 0


    def push_player_away_from_npc(self, npc, distance=12):
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

        if self.player.dialog_cooldown > 0:
            self.player.dialog_cooldown -= 1

        # Door collisions
        if door_group:
            door_collisions = pygame.sprite.spritecollide(self.player, door_group, False)
            if door_collisions:
                door = door_collisions[0]
                if door.is_exit:
                    self.player.leaving_submap = True
                    event_system.raise_event("change_to_parent_state", None)
                    event_system.raise_event("load_map", door.map_file)
                elif door.is_entrance:
                    self.player.in_submap = True
                    self.player.prev_cords = (
                        self.player.rect.copy().move(0, BLOCK_SIZE // 8),
                        (self.player.x, self.player.y)
                    )
                    event_system.raise_event("change_inside_state", None)
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

        if npc_group and self.player.dialog_cooldown == 0:
            for npc in npc_group:
                if self.player.action_button_pressed:
                    self.player.interaction_zone = self.create_facing_rect(self.player)
                    if self.player.interaction_zone.colliderect(npc.rect):
                        if (
                            not getattr(self.player, "in_dialog", False) and
                            event_system.raise_event("get_control_state")[0] == "world"
                        ):
                            self.player.in_dialog = True
                            self.player.action_button_pressed = False  # <- directly stop input retrigger
                            event_system.raise_event("action_button_released")
                            event_system.raise_event("dialog_set_visible", True)
                            event_system.raise_event("dialog_start_chat", npc)
                            # self.push_player_away_from_npc(npc)
                            break
                else:
                    self.player.interaction_zone = pygame.Rect(0, 0, 0, 0)


    def create_facing_rect(self, player, distance=64, size=16):
        if player.dir == 0:  # down
            return pygame.Rect(player.rect.centerx - size // 2,
                               player.rect.bottom,
                               size, distance)
        elif player.dir == 1:  # up
            return pygame.Rect(player.rect.centerx - size // 2,
                               player.rect.top - distance,
                               size, distance)
        elif player.dir == 2:  # right
            return pygame.Rect(player.rect.right,
                               player.rect.centery - size // 2,
                               distance, size)
        elif player.dir == 3:  # left
            return pygame.Rect(player.rect.left - distance,
                               player.rect.centery - size // 2,
                               distance, size)
