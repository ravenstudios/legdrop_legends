from states.state import State

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
