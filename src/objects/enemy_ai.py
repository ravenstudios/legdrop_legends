import random

class EnemyAI():

    def __init__(self, player, enemy, battle):
        self.player = player.battle_object
        self.enemy = enemy
        self.battle = battle
        self.attacks = self.enemy.options["Attacks"]
        self.items = self.enemy.options["Items"]

    def attack(self):
        attack = random.choice(self.attacks)
        cost = attack["cost"]
        dmg = attack["dmg"]
        if self.enemy.mp >= cost:
            self.player.hp -= dmg
            self.enemy.mp -= cost
            self.battle.battle_menu.message = ""
            self.battle.message_index = 0
            self.battle.message = attack["message"]

        else:

            self.battle.battle_menu.message = ""
            self.battle.message_index = 0
            self.battle.message = "Crawdaddy Powered"
            self.powder()

        self.battle.turn = "player"

    def powder(self):
        self.enemy.mp += self.enemy.powder_rate

    def restore_health(self, key):
        pass

    def restore_mp(self, key):
        pass

    def enemy_turn(self):
        self.attack()
