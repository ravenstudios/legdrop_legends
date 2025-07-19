from constants import *
import pygame
from event_system import event_system

font = pygame.font.SysFont(None, 24)


class Checkbox:
    def __init__(self, x, y, size, text=""):
        self.rect = pygame.Rect(x, y, size, size)
        self.checked = False
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        if self.checked:
            pygame.draw.line(surface, BLACK, self.rect.topleft, self.rect.bottomright, 3)
            pygame.draw.line(surface, BLACK, self.rect.topright, self.rect.bottomleft, 3)

        label = font.render(self.text, True, WHITE)
        surface.blit(label, (self.rect.right + 10, self.rect.y))

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.checked = not self.checked
                    event_system.raise_event("toggle_mute", None)

# Slider class
class Slider:
    def __init__(self, x, y, w, min_val=0, max_val=100, value=50):
        self.rect = pygame.Rect(x, y, w, 10)
        self.knob = pygame.Rect(x, y - 5, 10, 20)
        self.dragging = False
        self.min_val = min_val
        self.max_val = max_val
        self.value = value
        self.update_knob()

    def update_knob(self):
        ratio = (self.value - self.min_val) / (self.max_val - self.min_val)
        self.knob.x = self.rect.x + int(ratio * self.rect.width)

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)
        pygame.draw.rect(surface, GREEN if self.dragging else WHITE, self.knob)
        value_text = font.render(f"{int(self.value)}", True, WHITE)
        surface.blit(value_text, (self.rect.right + 10, self.rect.y - 10))

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.knob.collidepoint(event.pos):
                    self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    pos = max(self.rect.left, min(event.pos[0], self.rect.right))
                    ratio = (pos - self.rect.x) / self.rect.width
                    self.value = self.min_val + ratio * (self.max_val - self.min_val)
                    self.update_knob()
                    event_system.raise_event("set_volume", self.value)
# # Instantiate
# checkbox = Checkbox(50, 50, 20, "Enable sound")
# slider = Slider(50, 100, 200, value=25)
