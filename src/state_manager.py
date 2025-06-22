import pygame
from constants import *
import group_manager
import battle
import event_system
import states.world


class StateManager():
    def __init__(self):
        self.joysticks = []
        self.joystick = None

        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            self.joysticks.append(joystick)
        if self.joysticks:
            self.joystick = self.joysticks[0]

        self.event_system = event_system.EventSystem()
        # self.group_manager = group_manager.GroupManager(self, self.event_system, self.joystick)
        self.world = states.world.World(self.event_system, self.joystick)
        self.current_state = self.world
        self.event_system.on("change_state", self.change_state)

    def events(self, events):
        self.current_state.events(events)

    def update(self):
        self.current_state.update()

    def draw(self, surface):
        self.current_state.draw(surface)

    def change_state(self, state):
        self.current_state = state
