import pygame
from constants import *
import objects.enemy_battle_object
import battle_menu
import objects.enemy_ai

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
        action = None
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    action = "action_button"
                elif event.button == 11:
                    action = "index_up"
                elif event.button == 12:
                    action = "index_down"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    action = "index_up"
                elif event.key == pygame.K_DOWN:
                    action = "index_down"
                elif event.key == pygame.K_RETURN:
                    action = "action_button"
        if action and self.turn == "player":
            getattr(self, action)()

    def index_up(self):
        self.index -= 1

    def index_down(self):
        self.index += 1

    def action_button(self):
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

    def battle_attack(self, player, enemy, turn, attack):
        p_stats = player
        e_stats = enemy
        p_class = p_stats.class
        e_class = e_stats.class
        won_rps = self.won_rps(p_class, e_class)
        atk = None
        wps_dmg = 0
        if self.turn == "player":
            atk = player.options["Attacks"][attack]
        if won_rps:
            wps_dmg = 10

        return atk["dmg"] + wps_dmg - p_stats.def



    def won_rps(self, p_class, e_class):
        if p_class == "brawler" and e_class == "tactician":
            return True
        if p_class == "tactician" and e_class == "high_flyer":
            return True
        if p_class == "high_flyer" and e_class == "brawler":
            return True
        return False
