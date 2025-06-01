import pygame
from constants import *

class StateManager():


    def __init__(self):
        self.game = Game()
        self.pause = Pause()
        self.current_state = self.game

    def update(self):
        self.current_state.update()

    def draw(self, surface):
        self.current_state.draw(surface)


class State():
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self, surface):
        pass


class Game(State):
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass

class Pause(State):
    def __init__(self):
        pass

    
