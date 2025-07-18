from states.base_map_state import BaseMapState

class WorldState(BaseMapState):
    def __init__(self, event_system, joystick=None):
        super().__init__()
        self.load_map("town1.tmx")
        self.song = "town.mp3"
