import pygame
class DrawText(object):
    """ for DrawText."""

    def __init__(self):
        pass



    def update_surface(self, text, font_size, x, y, surface, color=(255, 255, 255)):
        font = pygame.font.SysFont(None, font_size)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))
