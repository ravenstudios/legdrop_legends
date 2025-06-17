import pygame
from constants import *
import enemy_battle_object
class Battle():

    def __init__(self, player, enemy=None):
        self.player = player
        self.enemy = enemy_battle_object.EnemyBattleObject()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)

        self.index = 0
        self.rect = pygame.Rect(0, 0, 200, 30)
        self.options = ["Fight", "Item", "Tag", "Run"]


    def events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.index -= 1
                if event.key == pygame.K_DOWN:
                    self.index += 1

    def update(self):
        self.enemy_group.update()
        self.index = self.index % len(self.options)
        # keys = pygame.key.get_pressed()
        #


    def draw(self, surface):

        surface.fill((255, 255, 255))  # White background

        WIDTH, HEIGHT = surface.get_size()
        BORDER_COLOR = (0, 0, 0)
        GREEN = (100, 200, 100)
        RED = (200, 50, 50)
        BLUE = (100, 100, 255)
        GRAY = (230, 230, 230)

        # Enemy info box (top left)
        # enemy_box = pygame.Rect(50, 40, 250, 80)
        # pygame.draw.rect(surface, GRAY, enemy_box)
        # pygame.draw.rect(surface, BORDER_COLOR, enemy_box, 3)
        #
        # # Player info box (bottom right)
        # player_box = pygame.Rect(WIDTH - 300, HEIGHT - 200, 250, 80)
        # pygame.draw.rect(surface, GRAY, player_box)
        # pygame.draw.rect(surface, BORDER_COLOR, player_box, 3)
        #
        # # HP bar inside player box
        # hp_bar_width = 150
        # hp_bar_height = 15
        # player_hp_bar = pygame.Rect(player_box.x + 80, player_box.y + 35, hp_bar_width, hp_bar_height)
        # pygame.draw.rect(surface, RED, player_hp_bar)
        # pygame.draw.rect(surface, BORDER_COLOR, player_hp_bar, 2)
        #
        # # HP bar inside enemy box
        # enemy_hp_bar = pygame.Rect(enemy_box.x + 80, enemy_box.y + 35, hp_bar_width, hp_bar_height)
        # pygame.draw.rect(surface, GREEN, enemy_hp_bar)
        # pygame.draw.rect(surface, BORDER_COLOR, enemy_hp_bar, 2)
        #
        # # Text box (bottom)

        # pygame.draw.rect(surface, (255, 255, 255), text_box)
        # pygame.draw.rect(surface, BORDER_COLOR, text_box, 3)
        #
        # # Placeholder for Pokémon (circles)
        # # Enemy Pokémon (top right)
        # pygame.draw.circle(surface, RED, (WIDTH - 120, 100), 40)
        # # Player Pokémon (bottom left)
        # pygame.draw.circle(surface, BLUE, (120, HEIGHT - 140), 40)

        # Optional: placeholder text
        w = BLOCK_SIZE * 3
        h = BLOCK_SIZE * 2
        menu_box = pygame.Rect(WIDTH - w - 20, HEIGHT - h - 20, w, h)
        option_box = pygame.Rect(WIDTH - w - 20, HEIGHT - h - 20 + (25 * self.index), w, 25)
        text_box = pygame.Rect(menu_box.x + menu_box.width // 2, menu_box.y, menu_box.width // 2, menu_box.height // 2)
        font = pygame.font.SysFont("Arial", 20)

        pygame.draw.rect(surface, (200, 200, 200), menu_box)

        for i, option in enumerate(self.options):
            text = font.render(option, True, (0, 0, 0))
            surface.blit(text, (text_box.x, text_box.y + 25 * i))

        pygame.draw.rect(surface, BORDER_COLOR, option_box, 3)
        # pygame.draw.rect(surface, BORDER_COLOR, , 3)
        self.enemy_group.draw(surface)
