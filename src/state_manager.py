import pygame
from constants import *
import group_manager
import battle


class StateManager():
    def __init__(self):
        self.group_manager = group_manager.GroupManager()
        self.world = World(self.group_manager)
        self.battle = Battle(self.group_manager)
        self.current_state = self.world

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


class World(State):
    def __init__(self, group_manager):
        self.group_manager = group_manager

    def update(self):
        self.group_manager.update()

    def draw(self, surface):
        self.group_manager.draw(surface)

class Battle(State):
    def __init__(self, group_manager):
        self.group_manager = group_manager
        self.battle = battle.Battle(group_manager.player)

    def update(self):
        self.battle.update()

    def draw(self, surface):
        self.battle.draw(surface)
