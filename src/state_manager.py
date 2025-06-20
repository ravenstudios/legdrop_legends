import pygame
from constants import *
import group_manager
import battle


class StateManager():
    def __init__(self):
        self.group_manager = group_manager.GroupManager(self)
        self.world = World(self.group_manager)
        self.current_state = self.world

    def events(self, events):
        self.current_state.events(events)

    def update(self):
        self.current_state.update()

    def draw(self, surface):
        self.current_state.draw(surface)

    def change_state(self, state, enemy=None):
        self.current_state = state
        if self.current_state == self.battle:
            self.battle.enemy = enemy.battle_object



class State():
    def __init__(self):
        pass
    def events(self, events=None):
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
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy


    def events(self, events):
        self.battle.events(events)

    def update(self):
        self.battle.update()

    def draw(self, surface):
        self.battle.draw(surface)
