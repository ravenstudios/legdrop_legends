from constants import *

class Camera(object):


    def __init__(self, event_system):
        self.event_system = event_system

    def update_offset(self, player):
        return (-player.x, -player.y)
