import random
import battle_calc
from player.player import main_player

class EnemyAI():

    def __init__(self, enemy, battle):
        self.player_bo = main_player.get_current_wrestler().battle_object
        self.enemy = enemy
        self.battle = battle
        self.attacks = self.enemy.options["Attacks"]
        self.items = self.enemy.options["Items"]

    def attack(self):
        attack = random.choice(self.attacks)
        cost = attack["cost"]
        dmg = attack["power"]

        self.battle.battle_menu.message = ""
        self.battle.message_index = 0

        if self.enemy.mp >= cost:
            atk_dmg = battle_calc.damage(dmg, self.enemy, self.player_bo)

            self.player_bo.hp -= atk_dmg[0]
            self.enemy.mp -= cost
            self.battle.battle_menu.message = ""
            self.battle.message_index = 0
            # self.battle.message = attack["message"]
            if atk_dmg[1]:
                self.battle.message = f"Critical Hit!! Dealt {atk_dmg[0]} damage"
            else:
                self.battle.message = f"Dealt {atk_dmg[0]} damage"

        else:

            self.battle.message = "Crawdaddy Powered"
            self.powder()
        self.battle.turn = "player"
        self.battle.is_start_of_turn = True

    def powder(self):
        self.enemy.mp += self.enemy.powder_rate

    def restore_health(self, key):
        pass

    def restore_mp(self, key):
        pass

    def enemy_turn(self):
        self.attack()
