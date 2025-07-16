import pygame
from constants import *
from  battle.battle_graphics import BattleGraphics
import battle.enemy_ai
from player.player import main_player
from battle.player_actions import PlayerActions
from  battle import message_display



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
        self.current_menu = list(self.m_player.options.keys())
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


        # self.player_actions.check_poison()


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
        action = None
        if self.has_controls:
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
            submenu_data = self.m_player.options[key]
            if isinstance(submenu_data, list):
                self.parent_menu = self.current_menu
                self.current_menu = submenu_data
                self.index = 0
                self.in_submenu = True
        if isinstance(key, dict):
            if key["name"] == "Back":
                self.current_menu = self.parent_menu
                self.index = 0
                self.in_submenu = False
            else:
                self.player_actions.action(key)
