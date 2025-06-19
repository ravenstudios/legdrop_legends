import pygame
from constants import *
import enemy_battle_object
import battle_menu

class Battle():

    def __init__(self, player, enemy=None):
        self.player = player
        self.enemy = enemy_battle_object.EnemyBattleObject()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)
        self.battle_menu = battle_menu.BattleMenu(self)
        self.index = 0
        self.current_menu = list(self.player.battle_object.options.keys())
        self.in_submenu = False
        self.parrent_menu = None
        # print(self.options)
        # self.player_health = 100
        # self.enemy_health = 100
        self.current_hp = 56
        self.max_hp = 100
        self.current_mp = 13
        self.max_mp = 25

        self.enemy_current_hp = 56
        self.enemy_max_hp = 100
        self.enemy_current_mp = 13
        self.enemy_max_mp = 25

        self.turn = "player"
        self.turn_delay = 2000
        self.turn_delay_timer = 0
        self.message = ""
        self.message_index = 0

    def events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
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
        if self.turn != "player":
            now = pygame.time.get_ticks()
            if now - self.turn_delay_timer >= self.turn_delay:
                self.enemy_attack()

    def draw(self, surface):
        self.battle_menu.draw(surface)


    def enemy_attack(self):
        self.player.battle_object.hp -= 5
        self.turn = "player"

    def attack(self, key):

        if self.player.battle_object.mp >= key["cost"]:
            self.enemy.hp -= key["dmg"]
            self.player.battle_object.mp -= key["cost"]
            self.battle_menu.message = ""
            self.message_index = 0
            self.message = key["message"]
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

    def restore_mp(self, key):
        self.battle_menu.message = ""
        self.message_index = 0
        self.message = key["message"]
        bo = self.player.battle_object
        bo.mp += key["mp"]
        bo.mp = min(bo.mp, bo.max_mp)

    def action(self, key):
        if "type" in key:
            if key["type"] == "attack":
                self.attack(key)


            if key["type"] == "restore_hp":
                self.restore_health(key)


            if key["type"] == "restore_mp":
                self.restore_mp(key)
