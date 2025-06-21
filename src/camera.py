from constants import *

class Camera(object):


    def __init__(self):
        pass

    def update_offset(self, player):
        return (-player.x, -player.y)
