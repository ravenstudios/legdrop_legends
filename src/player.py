import main_entity
import pygame
from constants import *
import movement_handler
import player_battle_object
class Player(main_entity.Main_entity):

    def __init__(self):
        self.x = 0
        self.y = 0
        super().__init__(self.x, self.y, "Brother16x16-Sheet.png")
        self.y_sprite_sheet_index = 0
        self.speed = 7
        self.movement_handler = movement_handler.MovementHandler(self)
        self.battle_object = player_battle_object.PlayerBattleObject()


    def update(self, cam_offset):
        # self.update_cam_offset(0)
        self.movement_handler.key_handler(cam_offset)
        self.animate()
        self.rect.x = max(0, min(self.rect.x, GAME_WIDTH  - self.rect.width))
        self.rect.y = max(0, min(self.rect.top, GAME_HEIGHT - self.rect.height))
        # print(f"X:{self.x}")
        pygame.display.set_caption(f"cam:{cam_offset}  |  X:{self.x}  |  Rect.center.x:{self.rect.left}  |  WORLD:{WORLD_WIDTH}-{WORLD_HEIGHT}  |  Halfscreen:{GAME_WIDTH // 2}")
