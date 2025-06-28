from states.state import State
from states import state
import battle


class BattleState(State):
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.battle = battle.Battle(self.player, self.enemy)

    def events(self, events):
        self.battle.events(events)

    def update(self):
        self.battle.update()

    def draw(self, surface):
        self.battle.draw(surface)
