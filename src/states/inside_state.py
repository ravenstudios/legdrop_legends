from states.base_map_state import BaseMapState

class InsideState(BaseMapState):
    def __init__(self, event_system, joystick=None):
        super().__init__()
        self.state_name = "world"
        self.song = "town.mp3"
