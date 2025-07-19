import pygame
import os
from event_system import event_system


class MusicManager:
    def __init__(self):
        self.track = None
        self.volume = 0.0
        pygame.mixer.init()
        event_system.on("set_volume", self.set_volume)
        event_system.on("toggle_mute", self.toggle_mute)
        self.is_muted = False


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


    def toggle_mute(self):
        self.is_muted = not self.is_muted
        pygame.mixer.music.set_volume(0 if self.is_muted else self.volume)


    def stop(self):
        pygame.mixer.music.stop()
        self.track = None

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def set_volume(self, v):

        self.volume = v / 100
        pygame.mixer.music.set_volume(self.volume)
