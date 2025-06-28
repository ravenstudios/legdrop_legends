from constants import *
import pygame

class BattleMenu(object):
    """docstring for BattleMenu."""

    def __init__(self, battle):
        self.battle = battle
        self.message = ""
        self.message_index = 0
        self.enemy_bo = self.battle.enemy

    def draw(self, surface):
        surface.fill((255, 255, 255))
        WIDTH, HEIGHT = surface.get_size()
        BORDER_COLOR = (0, 0, 0)
        GREEN = (100, 200, 100)
        RED = (200, 50, 50)
        BLUE = (100, 100, 255)
        GRAY = (230, 230, 230)


        w = BLOCK_SIZE * 3
        h = BLOCK_SIZE * 2.5
        font_size = 20
        padding = 20
        text_padding = 10

        player_box = pygame.Rect(padding, HEIGHT - h - padding, GAME_WIDTH - padding * 2, h)
        menu_box = player_box.inflate(-player_box.width // 1.3, -padding * 2)
        menu_box.topleft = (player_box.width - menu_box.width - padding, player_box.y + padding)

        message_box = player_box.inflate(-player_box.width // 1.7, -player_box.height // 2)
        message_box.topleft = (player_box.center[0] - message_box.width // 2, player_box.bottom - message_box.height - padding)

        option_box = menu_box.inflate(0, -menu_box.height + (font_size))
        option_box.topleft = (menu_box.x, menu_box.y + self.battle.index * font_size + text_padding + text_padding // 4)

        text_box = menu_box


        health_box = pygame.Rect(padding * 4, player_box.y + padding * 2, w, BLOCK_SIZE // 2)
        mp_box = pygame.Rect(padding * 4, health_box.y + padding * 3, w, BLOCK_SIZE // 2)
        font = pygame.font.SysFont("Arial", font_size)


        enemy_health_box = pygame.Rect(padding * 4, padding, w, BLOCK_SIZE // 2)
        enemy_mp_box = pygame.Rect(padding * 4, padding * 4, w, BLOCK_SIZE // 2)
        enemy_name_box = self.battle.enemy.rect.move(0, self.battle.enemy.rect.bottom - padding)
        pygame.draw.rect(surface, (200, 0, 200), player_box)
        pygame.draw.rect(surface, (200, 200, 200), menu_box)
        pygame.draw.rect(surface, (255, 200, 200), message_box)

        for i, option in enumerate(self.battle.current_menu):
            text = None
            str = ""
            if isinstance(option, dict):
                if "qty" in option:
                    str = f"{option['name']} - Qty:{option['qty']}"
                else:
                    str = option['name']
                text = font.render(str, True, (0, 0, 0))
            else:
                text = font.render(option, True, (0, 0, 0))

            surface.blit(text, (text_box.x+ text_padding, text_box.y + font_size * i + text_padding))
        if self.battle.message and self.battle.message_index < len(self.battle.message):
            self.message += self.battle.message[self.battle.message_index]
            self.battle.message_index += 1
        message_text = font.render(self.message, True, (0, 0, 0))
        surface.blit(message_text, message_box)


        pygame.draw.rect(surface, BORDER_COLOR, option_box.inflate(5, 5), 3)


        hp_ratio = self.battle.player.battle_object.hp / self.battle.player.battle_object.max_hp
        pygame.draw.rect(surface, GREEN, (health_box.x, health_box.y, hp_ratio * health_box.width, health_box.height))
        pygame.draw.rect(surface, BLACK, health_box.inflate(5, 5), 6)

        mp_ratio = self.battle.player.battle_object.mp / self.battle.player.battle_object.max_mp
        pygame.draw.rect(surface, BLUE, (mp_box.x, mp_box.y, mp_ratio * mp_box.width, mp_box.height))
        pygame.draw.rect(surface, BLACK, mp_box.inflate(5, 5), 6)

        enemy_hp_ratio = self.enemy_bo.hp / self.enemy_bo.max_hp
        pygame.draw.rect(surface, GREEN, (enemy_health_box.x, enemy_health_box.y, enemy_hp_ratio * enemy_health_box.width, enemy_health_box.height))
        pygame.draw.rect(surface, BLACK, enemy_health_box.inflate(5, 5), 6)

        enemy_mp_ratio = self.enemy_bo.mp / self.enemy_bo.max_mp
        pygame.draw.rect(surface, BLUE, (enemy_mp_box.x, enemy_mp_box.y, enemy_mp_ratio * enemy_mp_box.width, enemy_mp_box.height))
        pygame.draw.rect(surface, BLACK, enemy_mp_box.inflate(5, 5), 6)

        hp_text = font.render(f"HP:{self.battle.player.battle_object.hp} / {self.battle.player.battle_object.max_hp}", True, (0, 0, 0))
        surface.blit(hp_text, health_box.inflate(-text_padding * 2, -text_padding))

        mp_text = font.render(f"MP:{self.battle.player.battle_object.mp} / {self.battle.player.battle_object.max_mp}", True, (0, 0, 0))
        surface.blit(mp_text, mp_box.inflate(-text_padding * 2, -text_padding))

        enemy_hp_text = font.render(f"HP:{self.enemy_bo.hp} / {self.enemy_bo.max_hp}", True, (0, 0, 0))
        surface.blit(enemy_hp_text, enemy_health_box.inflate(-text_padding * 2, -text_padding))

        enemy_mp_text = font.render(f"MP:{self.enemy_bo.mp} / {self.enemy_bo.max_mp}", True, (0, 0, 0))
        surface.blit(enemy_mp_text, enemy_mp_box.inflate(-text_padding * 2, -text_padding))

        self.battle.enemy_group.draw(surface)
        enemy_name = font.render(self.enemy_bo.name, True, (0, 0, 0))
        surface.blit(enemy_name, enemy_name_box)
