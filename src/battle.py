import pygame
from constants import *
import enemy_battle_object
class Battle():

    def __init__(self, player, enemy=None):
        self.player = player
        self.enemy = enemy_battle_object.EnemyBattleObject()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)

    def update(self):
        self.enemy_group.update()

    def draw(self, surface):

        surface.fill((255, 255, 255))  # White background

        WIDTH, HEIGHT = surface.get_size()
        BORDER_COLOR = (0, 0, 0)
        GREEN = (100, 200, 100)
        RED = (200, 50, 50)
        BLUE = (100, 100, 255)
        GRAY = (230, 230, 230)

        # Enemy info box (top left)
        enemy_box = pygame.Rect(50, 40, 250, 80)
        pygame.draw.rect(surface, GRAY, enemy_box)
        pygame.draw.rect(surface, BORDER_COLOR, enemy_box, 3)

        # Player info box (bottom right)
        player_box = pygame.Rect(WIDTH - 300, HEIGHT - 200, 250, 80)
        pygame.draw.rect(surface, GRAY, player_box)
        pygame.draw.rect(surface, BORDER_COLOR, player_box, 3)

        # HP bar inside player box
        hp_bar_width = 150
        hp_bar_height = 15
        player_hp_bar = pygame.Rect(player_box.x + 80, player_box.y + 35, hp_bar_width, hp_bar_height)
        pygame.draw.rect(surface, RED, player_hp_bar)
        pygame.draw.rect(surface, BORDER_COLOR, player_hp_bar, 2)

        # HP bar inside enemy box
        enemy_hp_bar = pygame.Rect(enemy_box.x + 80, enemy_box.y + 35, hp_bar_width, hp_bar_height)
        pygame.draw.rect(surface, GREEN, enemy_hp_bar)
        pygame.draw.rect(surface, BORDER_COLOR, enemy_hp_bar, 2)

        # Text box (bottom)
        text_box = pygame.Rect(20, HEIGHT - 100, WIDTH - 40, 80)
        pygame.draw.rect(surface, (255, 255, 255), text_box)
        pygame.draw.rect(surface, BORDER_COLOR, text_box, 3)

        # Placeholder for Pokémon (circles)
        # Enemy Pokémon (top right)
        pygame.draw.circle(surface, RED, (WIDTH - 120, 100), 40)
        # Player Pokémon (bottom left)
        pygame.draw.circle(surface, BLUE, (120, HEIGHT - 140), 40)

        # Optional: placeholder text
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(self.player.battle_object.moves[0]["name"], True, (0, 0, 0))
        surface.blit(text, (text_box.x + 20, text_box.y + 25))

        self.enemy_group.draw(surface)
