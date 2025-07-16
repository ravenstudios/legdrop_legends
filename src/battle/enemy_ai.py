import random
from battle import battle_calc
from player.player import main_player
from event_system import event_system


class EnemyAI():

    def __init__(self, enemy, battle):
        self.player_bo = main_player.get_current_wrestler().battle_object
        self.enemy = enemy
        self.battle = battle
        self.message_display = battle.message_display
        self.attacks = self.enemy.options["Attacks"]
        self.attack_message_delay = 2000
        self.message_display.set_message(f"{self.enemy.name} has enterd the ring")
        self.is_start_of_turn = False
        self.turn_in_progress = False
        self.poisoned_message_delay = 2000


    def update(self):
        pass



    def attack(self):
        attack = random.choice(self.attacks)
        cost = attack["cost"]
        dmg = attack["power"]

        self.battle.battle_graphics.message = ""
        self.battle.message_index = 0

        if self.enemy.mp >= cost:
            atk_dmg = battle_calc.damage(dmg, self.enemy, self.player_bo)
            str = f"{self.enemy.name} used {attack['name']}"
            # def msg():
            if atk_dmg[1]:
                self.message_display.set_message(f"{str} Critical Hit!! it deal {atk_dmg[0]} damage")
            else:
                self.message_display.set_message(f"{str} it dealt {atk_dmg[0]} damage")
            self.player_bo.hp -= atk_dmg[0]
            self.enemy.mp -= cost
            self.set_player_shake()
            self.enemy.start_lunge(self.player_bo)

        else:
            self.message_display.set_message("Crawdaddy Powered")
            self.powder()

        self.battle.set_player_turn()
        self.battle.is_start_of_turn = True


    def powder(self):
        self.enemy.mp += self.enemy.powder_rate
        self.battle.set_player_turn()

    def restore_health(self, key):
        pass


    def restore_mp(self, key):
        pass


    def enemy_turn(self):
        if self.turn_in_progress:
            return  # avoid re-triggering the turn

        self.turn_in_progress = True
        self.is_start_of_turn = True

        if self.enemy.is_poisoned and self.is_start_of_turn:
            self.battle.enemy.hp -= 5
            self.is_start_of_turn = False
            self.message_display.set_message(f"{self.enemy.name} is damaged by poison.")
            self.battle.player_actions.set_enemy_shake()
            event_system.raise_event("add_timer", [
                self.poisoned_message_delay,
                lambda: self._continue_enemy_turn(),
                True
            ])
        else:
            self._continue_enemy_turn()

    def _continue_enemy_turn(self):
        self.is_start_of_turn = False
        self.turn_in_progress = False
        if not self.battle.has_enemy_died:
            self.attack()


    def set_player_shake(self):
        self.player_bo.set_shake(True)
        event_system.raise_event("add_timer", [
            self.battle.shake_delay,
            lambda: self.player_bo.set_shake(False),
            True
        ])


    def set_player_turn(self):
        event_system.raise_event("add_timer", [
            self.battle.turn_delay,
            lambda: setattr(self.battle, "turn", "player"),
            True
        ])
