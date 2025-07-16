import pygame
import os

class MusicManager:
    def __init__(self, music_folder="assets/music"):
        self.music_folder = music_folder
        self.current_track = None
        self.volume = 0.8
        pygame.mixer.init()

    def play(self, track_name, loop=True):
        path = os.path.join(self.music_folder, track_name)
        if not os.path.exists(path):
            print(f"[MusicManager] Track not found: {path}")
            return

        if self.current_track != path:
            pygame.mixer.music.load(path)
            self.current_track = path

        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1 if loop else 0)
        print(f"[MusicManager] Playing: {track_name}")

    def stop(self):
        pygame.mixer.music.stop()
        self.current_track = None
        print("[MusicManager] Stopped music")

    def pause(self):
        pygame.mixer.music.pause()
        print("[MusicManager] Music paused")

    def resume(self):
        pygame.mixer.music.unpause()
        print("[MusicManager] Music resumed")

    def set_volume(self, volume):
        self.volume = max(0, min(1, volume))  # Clamp between 0 and 1
        pygame.mixer.music.set_volume(self.volume)
        print(f"[MusicManager] Volume set to {self.volume}")
