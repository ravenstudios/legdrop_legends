import pygame
from constants import *
from  battle.battle_graphics import BattleGraphics
import battle.enemy_ai
from player.player import main_player
from battle.player_actions import PlayerActions
from  battle import message_display
from event_system import event_system


class Battle():
    def __init__(self, enemy):
        self.message_display = message_display.MessageDisplay()
        self.player_actions = PlayerActions(self)
        self.m_player = main_player.current_wrestler.battle_object
        self.enemy = enemy.battle_object

        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.m_player)
        self.index = 0
        self.battle_options = self.m_player.options
        self.extra_options = {
            "Items": [
                {"name": "Bandaid", "hp": 5, "type": "restore_hp", "message": f" used Bandaid"},
                {"name": "Beer", "mp": 10, "type": "restore_mp", "message": f" used Beer"},
                {"name": "Powder", "mp": 5, "type": "restore_mp", "message": f" powered"},
            ],
            "Tag Partner": [
                {"name": "Tag Partner", "type": "tag", "message": "Player tagged"},
            ],
            "Powder": [
                {"name": "Powder", "mp": 0, "type": "restore_mp", "message": ""},
            ],
            "Run": [
                {"name": "Run", "type": "run", "message": "Player tried running"},
            ]
        }
        self.battle_options.update(self.extra_options)
        self.current_menu = list(self.battle_options.keys())
        self.in_submenu = False
        self.parrent_menu = None
        self.turn = "player"
        self.can_enemy_turn = False
        self.turn_delay = 3000
        self.shake_delay = 500

        self.is_start_of_turn = True
        self.battle_graphics = BattleGraphics(self)

        self.enemy_ai = battle.enemy_ai.EnemyAI(self.enemy, self)
        self.has_controls = True
        self.has_player_died = False
        self.has_enemy_died = False

        event_system.on("battle_index_up", self.index_up)
        event_system.on("battle_index_down", self.index_down)
        event_system.on("battle_action_button", self.action_button)
        event_system.on("battle_back", self.back)

    def update(self):
        self.player_group.update()
        self.enemy_group.update()
        self.message_display.update()
        self.enemy.update()
        self.m_player.update()



        if self.m_player.hp <= 0 and not self.has_player_died:
            self.has_player_died = True
            self.player_actions.player_died()
            self.has_controls = False

        if self.enemy.hp <= 0 and not self.has_enemy_died:
            self.has_enemy_died = True
            self.player_actions.enemy_died()
            self.has_controls = False

        self.index = max(0, min(self.index, len(self.current_menu) - 1))
        if self.turn == "enemy" and not self.has_enemy_died:
            self.enemy_ai.enemy_turn()


    def draw(self, surface):
        self.battle_graphics.draw(surface)
        self.enemy_group.draw(surface)
        self.player_group.draw(surface)


    def set_player_turn(self):
        self.has_controls = True
        self.turn = "player"


    def events(self, events):
        pass


    def index_up(self):
        self.index -= 1


    def index_down(self):
        self.index += 1

    def back(self):
        self.current_menu = self.parent_menu
        self.index = 0
        self.in_submenu = False

    def action_button(self):
        key = self.current_menu[self.index]
        if not self.in_submenu:
            submenu_data = self.battle_options[key]
            if isinstance(submenu_data, list):
                self.parent_menu = self.current_menu
                self.current_menu = submenu_data
                self.index = 0
                self.in_submenu = True
        # if isinstance(key, dict):
        #     if key["name"] == "Back":
        #         self.current_menu = self.parent_menu
        #         self.index = 0
        #         self.in_submenu = False
        #     else:
        self.player_actions.action(key)
