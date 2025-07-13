from  battle import battle_calc
from event_system import event_system
import random


class PlayerActions():
    def __init__(self, battle):

        self.battle = battle
        self.attack_message_delay = 2000
        self.poisoned_message_delay = 1000
        self.run_dice = 5



    def reset(self):
        self.battle.enemy.reset()
        self.battle.m_player.reset()
        event_system.raise_event("change_to_parent_state")



    def player_died(self):
        self.battle.m_player.is_dead = True
        event_system.raise_event("add_timer", [
            self.attack_message_delay * 2,
            lambda:self.battle.message_display.set_message("You got knocked the fuck on out!!"),
            True
        ])

        event_system.raise_event("add_timer", [
            self.attack_message_delay * 4,
            self.reset,
            True
        ])


    def enemy_died(self):
        self.battle.enemy.is_dead = True
        event_system.raise_event("add_timer", [
            self.attack_message_delay * 2,
            lambda:self.battle.message_display.set_message(f"You knocked {self.battle.enemy.name} fuck on out!!"),
            True
        ])

        event_system.raise_event("add_timer", [
            self.attack_message_delay * 4,
            self.reset,
            True
        ])



    def attack(self, key):
        self.battle.is_start_of_turn = False
        if self.battle.m_player.mp >= key["cost"]:
            atk_dmg = battle_calc.damage(key["power"], self.battle.m_player, self.battle.enemy)
            self.battle.enemy.hp -= atk_dmg[0]
            self.battle.m_player.mp -= key["cost"]

            str = f"Player used {key['name']}"
            # self.battle.message_display.set_message(str)

            txt = ""
            if atk_dmg[1]:
                txt = f"{str} Critical Hit!! It dealt {atk_dmg[0]} damage"
            else:
                txt = f"{str} it dealt {atk_dmg[0]} damage"
            self.battle.message_display.set_message(txt)
            self.battle.m_player.start_lunge(self.battle.enemy)
            self.set_enemy_turn()
            self.battle.current_menu = self.battle.parent_menu
            self.battle.index = 0
            self.battle.in_submenu = False

            self.set_enemy_shake()

        else:
            self.battle.message_display.set_message("Not enough MP!")

    def set_enemy_shake(self):
        self.battle.enemy.set_shake(True)
        event_system.raise_event("add_timer", [
            self.battle.shake_delay,
            lambda: self.battle.enemy.set_shake(False),
            True
        ])


    def set_enemy_turn(self):
        self.battle.has_controls = False
        event_system.raise_event("add_timer", [
            self.battle.turn_delay,
            lambda: setattr(self.battle, "turn", "enemy"),
            True
        ])

    def restore_health(self, key):
        self.battle.is_start_of_turn = Fals
        self.battle.message = key["message"]
        bo = self.battle.m_player
        bo.hp += key["hp"]
        bo.hp = min(bo.hp, bo.max_hp)
        self.set_enemy_turn()
        self.battle.current_menu = self.battle.parent_menu
        self.battle.index = 0
        self.battle.in_submenu = False

    def restore_mp(self, key):
        self.battle.is_start_of_turn = False
        self.battle.message = key["message"]
        bo = self.battle.m_player
        bo.mp += key["mp"]
        bo.mp = min(bo.mp, bo.max_mp)
        self.set_enemy_turn()
        self.battle.current_menu = self.battle.parent_menu
        self.battle.index = 0
        self.battle.in_submenu = False


    def poison_attack(self, key):
        self.battle.is_start_of_turn = False
        self.battle.enemy.is_poisoned = True
        self.set_enemy_turn()
        self.set_enemy_shake()
        self.battle.message_display.set_message("Player poisoned enemy")
        self.battle.m_player.start_lunge(self.battle.enemy)

    def action(self, key):
        if self.battle.turn == "player":
            if "type" in key:
                if key["type"] == "attack":
                    self.attack(key)

                if key["type"] == "restore_hp":
                    if key["qty"] > 0:
                        current_qty = key["qty"] - 1
                        key["qty"] = current_qty
                        self.restore_health(key)

                if key["type"] == "poison":
                    self.poison_attack(key)

                if key["type"] == "restore_mp":
                    self.restore_mp(key)

                if key["type"] == "run":
                    self.run()


    def run(self):
        dice = random.randint(1, self.run_dice)
        if dice == 1:
            self.battle.message_display.set_message("Player ran away")
            event_system.raise_event("add_timer", [
                self.attack_message_delay,
                lambda:event_system.raise_event("change_to_parent_state"),
                True
            ])
        else:
            self.battle.message_display.set_message("Player couldnt run away")
            self.set_enemy_turn()
            self.battle.current_menu = self.battle.parent_menu
            self.battle.index = 0
            self.battle.in_submenu = False


    def check_poison(self):
        if self.battle.m_player.is_poisoned and self.battle.is_start_of_turn:
            self.battle.is_start_of_turn = False
            self.battle.m_player.hp -= 5

            self.battle.message = "Player damaged by poison"

        if self.battle.enemy.is_poisoned and self.battle.is_start_of_turn:
            self.battle.is_start_of_turn = False
            self.battle.enemy.hp -= 5

            self.battle.message = "Enemy damaged by poison"
