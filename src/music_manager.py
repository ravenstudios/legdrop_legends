import pygame
import os

class MusicManager:
    def __init__(self):
        self.track = None
        self.volume = 0.0
        pygame.mixer.init()

    def play(self, file, loop=True):
        if not file:
            return
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/music", file)
        if not os.path.exists(path):
            print("MUSIC NOT FOUND:", path)
            return

        if self.track != path:
            pygame.mixer.music.load(path)
            self.track = path

        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1 if loop else 0)


    def stop(self):
        pygame.mixer.music.stop()
        self.track = None

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def set_volume(self, v):
        self.volume = v
        pygame.mixer.music.set_volume(self.volume)
