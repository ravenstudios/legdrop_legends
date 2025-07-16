from states.state import State
from states import state
from battle.battle import Battle


class BattleState(State):
    def __init__(self, enemy):
        self.enemy = enemy
        self.battle = Battle(self.enemy)
        self.state_name = "battle"
        self.song = "wrestler.mp3"

    def events(self, events):
        self.battle.events(events)

    def update(self):
        self.battle.update()

    def draw(self, surface):
        self.battle.draw(surface)
