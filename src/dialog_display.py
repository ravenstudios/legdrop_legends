import pygame
from constants import *

class DialogDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = BLOCK_SIZE * 10
        self.height = BLOCK_SIZE * 2
        self.x = GAME_WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - self.height

        self.is_visable = True

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((210, 210 ,210))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.font_size = 30
        self.font = pygame.font.SysFont(None, self.font_size)


    def update_text(self, text):
        text_surface = self.font.render(text, True, RED)
        self.image.blit(text_surface, (0, 0))
