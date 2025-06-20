import pygame
from constants import *
import enemy_battle_object
import battle_menu
import enemy_ai

class Battle():

    def __init__(self, player, enemy):

        self.player = player
        self.enemy = enemy
        self.enemy_ai = enemy_ai.EnemyAI(self.player, self.enemy, self)
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)
        self.battle_menu = battle_menu.BattleMenu(self)
        self.index = 0
        self.current_menu = list(self.player.battle_object.options.keys())
        self.in_submenu = False
        self.parrent_menu = None

        self.turn = "player"
        self.can_enemy_turn = False
        self.turn_delay = 2000
        self.turn_delay_timer = 0
        self.message = ""
        self.message_index = 0

    def events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and self.turn == "player":
                if event.key == pygame.K_UP:
                    self.index -= 1
                if event.key == pygame.K_DOWN:
                    self.index += 1
                if event.key == pygame.K_RETURN:
                    key = self.current_menu[self.index]
                    if not self.in_submenu:
                        submenu_data = self.player.battle_object.options[key]
                        if isinstance(submenu_data, list):
                            self.parent_menu = self.current_menu
                            self.current_menu = submenu_data  # now current_menu is a list of dicts
                            self.index = 0
                            self.in_submenu = True
                    if isinstance(key, dict):
                        if key["name"] == "Back":
                            self.current_menu = self.parent_menu
                            self.index = 0
                            self.in_submenu = False
                        else:
                            self.action(key)

    def update(self):
        
        self.enemy_group.update()
        self.index = max(0, min(self.index, len(self.current_menu) - 1))
        if self.turn == "enemy":

            now = pygame.time.get_ticks()
            if now - self.turn_delay_timer >= self.turn_delay:
                self.enemy_ai.enemy_turn()

    def draw(self, surface):
        self.battle_menu.draw(surface)


    def attack(self, key):

        if self.player.battle_object.mp >= key["cost"]:
            self.enemy.hp -= key["dmg"]
            self.player.battle_object.mp -= key["cost"]
            self.battle_menu.message = ""
            self.message_index = 0
            self.message = key["message"]
            self.turn = "enemy"
            self.turn_delay_timer = pygame.time.get_ticks()
            self.current_menu = self.parent_menu
            self.index = 0
            self.in_submenu = False

        else:
            self.battle_menu.message = ""
            self.message_index = 0
            self.message = "Not enough MP!"

    def restore_health(self, key):
        self.battle_menu.message = ""
        self.message_index = 0
        self.message = key["message"]
        bo = self.player.battle_object
        bo.hp += key["hp"]
        bo.hp = min(bo.hp, bo.max_hp)
        self.turn = "enemy"
        self.turn_delay_timer = pygame.time.get_ticks()
        self.current_menu = self.parent_menu
        self.index = 0
        self.in_submenu = False

    def restore_mp(self, key):
        self.battle_menu.message = ""
        self.message_index = 0
        self.message = key["message"]
        bo = self.player.battle_object
        bo.mp += key["mp"]
        bo.mp = min(bo.mp, bo.max_mp)
        self.turn = "enemy"
        self.turn_delay_timer = pygame.time.get_ticks()
        self.current_menu = self.parent_menu
        self.index = 0
        self.in_submenu = False

    def action(self, key):
        if self.turn == "player":
            if "type" in key:
                if key["type"] == "attack":
                    self.attack(key)


                if key["type"] == "restore_hp":
                    if key["qty"] > 0:
                        current_qty = key["qty"] - 1
                        key["qty"] = current_qty
                        self.restore_health(key)


                if key["type"] == "restore_mp":
                    self.restore_mp(key)
