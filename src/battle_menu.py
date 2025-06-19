from constants import *
import pygame

class BattleMenu(object):
    """docstring for BattleMenu."""

    def __init__(self, player):
        self.player = player
        self.message = ""
        self.message_index = 0

    def draw(self, surface):
        WIDTH, HEIGHT = surface.get_size()
        BORDER_COLOR = (0, 0, 0)
        GREEN = (100, 200, 100)
        RED = (200, 50, 50)
        BLUE = (100, 100, 255)
        GRAY = (230, 230, 230)


        w = BLOCK_SIZE * 3
        h = BLOCK_SIZE * 2.5
        font_size = 25
        padding = 20
        text_padding = 10

        player_box = pygame.Rect(padding, HEIGHT - h - padding, GAME_WIDTH - padding * 2, h)
        menu_box = player_box.inflate(-player_box.width // 1.3, -padding * 2)
        menu_box.topleft = (player_box.width - menu_box.width - padding, player_box.y + padding)

        message_box = player_box.inflate(-player_box.width // 1.7, -player_box.height // 2)
        message_box.topleft = (player_box.center[0] - message_box.width // 2, player_box.bottom - message_box.height - padding)

        option_box = menu_box.inflate(0, -menu_box.height + (font_size))
        option_box.topleft = (menu_box.x, menu_box.y + self.player.index * font_size + text_padding)

        text_box = menu_box


        health_box = pygame.Rect(padding * 4, player_box.y + padding * 2, w, BLOCK_SIZE // 2)
        mp_box = pygame.Rect(padding * 4, health_box.y + padding * 3, w, BLOCK_SIZE // 2)
        font = pygame.font.SysFont("Arial", font_size)


        enemy_health_box = pygame.Rect(padding * 4, padding, w, BLOCK_SIZE // 2)
        enemy_mp_box = pygame.Rect(padding * 4, padding * 4, w, BLOCK_SIZE // 2)

        pygame.draw.rect(surface, (200, 0, 200), player_box)
        pygame.draw.rect(surface, (200, 200, 200), menu_box)
        pygame.draw.rect(surface, (255, 200, 200), message_box)

        for i, option in enumerate(self.player.current_menu):
            text = None
            if isinstance(option, dict):
                text = font.render(option["name"], True, (0, 0, 0))
            else:
                text = font.render(option, True, (0, 0, 0))
            surface.blit(text, (text_box.x, text_box.y + font_size * i + text_padding))
        if self.player.message and self.player.message_index < len(self.player.message):
            self.message += self.player.message[self.player.message_index]
            self.player.message_index += 1
        message_text = font.render(self.message, True, (0, 0, 0))
        surface.blit(message_text, message_box)


        pygame.draw.rect(surface, BORDER_COLOR, option_box, 3)


        hp_ratio = self.player.player.battle_object.hp / self.player.player.battle_object.max_hp
        pygame.draw.rect(surface, GREEN, (health_box.x, health_box.y, hp_ratio * health_box.width, health_box.height))
        pygame.draw.rect(surface, BLACK, health_box.inflate(5, 5), 6)

        mp_ratio = self.player.player.battle_object.mp / self.player.player.battle_object.max_mp
        pygame.draw.rect(surface, BLUE, (mp_box.x, mp_box.y, mp_ratio * mp_box.width, mp_box.height))
        pygame.draw.rect(surface, BLACK, mp_box.inflate(5, 5), 6)


        enemy_hp_ratio = self.player.enemy.hp / self.player.enemy.max_hp
        pygame.draw.rect(surface, GREEN, (enemy_health_box.x, enemy_health_box.y, enemy_hp_ratio * enemy_health_box.width, enemy_health_box.height))
        pygame.draw.rect(surface, BLACK, enemy_health_box.inflate(5, 5), 6)

        enemy_mp_ratio = self.player.enemy.mp / self.player.enemy.max_mp
        pygame.draw.rect(surface, BLUE, (enemy_mp_box.x, enemy_mp_box.y, enemy_mp_ratio * enemy_mp_box.width, enemy_mp_box.height))
        pygame.draw.rect(surface, BLACK, enemy_mp_box.inflate(5, 5), 6)

        hp_text = font.render(f"HP:{self.player.player.battle_object.hp} / {self.player.player.battle_object.max_hp}", True, (0, 0, 0))
        surface.blit(hp_text, health_box)

        mp_text = font.render(f"MP:{self.player.player.battle_object.mp} / {self.player.player.battle_object.max_mp}", True, (0, 0, 0))
        surface.blit(mp_text, mp_box)

        enemy_hp_text = font.render(f"HP:{self.player.enemy.hp} / {self.player.enemy.max_hp}", True, (0, 0, 0))
        surface.blit(enemy_hp_text, enemy_health_box)

        enemy_mp_text = font.render(f"MP:{self.player.enemy.mp} / {self.player.enemy.max_mp}", True, (0, 0, 0))
        surface.blit(enemy_mp_text, enemy_mp_box)

        self.player.enemy_group.draw(surface)
