import pygame
from constants import *

class DialogDisplay(pygame.sprite.Sprite):
    def __init__(self, event_system):
        super().__init__()
        self.event_system = event_system
        self.event_system.on("change_dialog", self.update_text)
        self.event_system.on("set_visible", self.set_visible)
        self.width = BLOCK_SIZE * 10
        self.height = BLOCK_SIZE * 2
        self.x = GAME_WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - self.height

        self.is_visible = False

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((210, 210 ,210))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.font_size = 30
        self.font = pygame.font.SysFont(None, self.font_size)

    def set_visible(self, visible):
        self.is_visible = visible


    def update_text(self, text, max_chars_per_line=30):
        self.image.fill((0, 0, 0))  # clear previous text

        # Split the text into wrapped lines
        lines = []
        while len(text) > max_chars_per_line:
            # Try to break at last space within limit
            split_at = text.rfind(" ", 0, max_chars_per_line)
            if split_at == -1:
                split_at = max_chars_per_line  # force break mid-word if no space
            lines.append(text[:split_at])
            text = text[split_at:].lstrip()
        lines.append(text)  # add the remainder

        # Render each line
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, RED)
            self.image.blit(text_surface, (0, i * self.font.get_linesize()))
