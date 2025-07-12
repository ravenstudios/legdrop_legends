import pygame
from constants import *
import objects.enemy_battle_object
import battle_graphics
import objects.enemy_ai
# import battle_calc

from player.player import main_player
import battle_actions

class Battle():

    def __init__(self, enemy):
        self.battle_actions = battle_actions.BattleActions(self)
        self.m_player = main_player.current_wrestler.battle_object

        self.enemy = enemy.battle_object
        self.enemy_ai = objects.enemy_ai.EnemyAI(self.enemy, self)
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.m_player)
        self.battle_graphics = battle_graphics.BattleGraphics(self)
        self.index = 0
        self.current_menu = list(self.m_player.options.keys())
        self.in_submenu = False
        self.parrent_menu = None

        self.turn = "player"
        self.can_enemy_turn = False
        self.turn_delay = 2000

        self.shake_delay = 500

        self.message = ""
        self.message_index = 0

        self.is_start_of_turn = True

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
            submenu_data = self.m_player.options[key]
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
                self.battle_actions.action(key)




    def update(self):
        # print(f"main player:{self.m_player}")
        self.player_group.update()
        self.enemy_group.update()

        if self.enemy.can_shake:
            self.enemy.shake()

        if self.enemy.hp <= 0:
            self.battle_actions.enemy_died()

        if self.m_player.hp <= 0:
            self.battle_actions.player_died()

        self.battle_actions.check_poison()


        self.index = max(0, min(self.index, len(self.current_menu) - 1))
        if self.turn == "enemy":

            # now = pygame.time.get_ticks()
            # if now - self.turn_delay_timer >= self.turn_delay:
            #     print("enemy turn")
            self.enemy_ai.enemy_turn()
            # if now - self.shake_delay_timer >= self.shake_delay:

            # self.enemy.set_shake(False)

    def draw(self, surface):
        self.battle_graphics.draw(surface)
        self.enemy_group.draw(surface)
        self.player_group.draw(surface)
