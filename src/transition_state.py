import pygame
import random

class TransitionState:
    def __init__(self, state_manager, duration=1000, rows=6, cols=8):
        self.state_manager = state_manager
        self.duration = duration
        self.rows = rows
        self.cols = cols
        self.tiles = []
        self.active = False
        self.callback = None
        self.elapsed = 0
        self.gravity = 0.5
        self.screen_size = pygame.display.get_surface().get_size()

    def start(self, callback):
        self.callback = callback
        self.active = True
        self.elapsed = 0
        self.tiles = []

        # Take a screenshot of the current display
        screen = pygame.display.get_surface()
        screenshot = screen.copy()

        tile_width = self.screen_size[0] // self.cols
        tile_height = self.screen_size[1] // self.rows

        # Create tile surfaces and animation parameters
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * tile_width, row * tile_height, tile_width, tile_height)
                image = screenshot.subsurface(rect).copy()
                dx = random.randint(-6, 6)
                dy = random.randint(-12, -4)
                self.tiles.append({
                    "image": image,
                    "rect": rect.copy(),
                    "dx": dx,
                    "dy": dy,
                    "gravity": self.gravity
                })

    def update(self):
        if not self.active:
            return

        self.elapsed += 16  # Assume 60 FPS for now; use dt if needed

        for tile in self.tiles:
            tile["rect"].x += tile["dx"]
            tile["rect"].y += tile["dy"]
            tile["dy"] += tile["gravity"]

        if self.elapsed >= self.duration // 2 and self.callback:
            # Do callback only once
            self.callback()
            self.callback = None  # prevent repeat

        if self.elapsed >= self.duration:
            self.active = False

    def draw(self, surface):
        if not self.active:
            return

        for tile in self.tiles:
            surface.blit(tile["image"], tile["rect"])
