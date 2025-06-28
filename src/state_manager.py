import pygame
from constants import *
import battle
import event_system
import states.world


class StateManager():
    def __init__(self, joystick):
        self.joystick = joystick


        self.event_system = event_system.EventSystem()
        self.world = states.world.World(self.event_system, self.joystick)
        self.current_state = self.world
        self.event_system.on("change_state", self.change_state)
        self.event_system.on("change_to_parent_state", self.change_to_parent_state)
        self.parrent_state = None

    def events(self, events):
        self.current_state.events(events)

    def update(self):
        self.current_state.update()

    def draw(self, surface):
        self.current_state.draw(surface)

    def change_state(self, state):
        self.parrent_state = self.current_state
        self.current_state = state

    def change_to_parent_state(self, arg=None):
        self.current_state = self.parrent_state
