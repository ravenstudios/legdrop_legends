import pygame
from event_system import event_system

class InputHandler:
    def __init__(self):
        self.control_state = "player"  # 'player', 'menu', or 'battle'

    def set_control_state(self, state):
        self.control_state = state

    def update(self):
        keys = pygame.key.get_pressed()

        key_actions = {
            pygame.K_UP: "move_up",
            pygame.K_DOWN: "move_down",
            pygame.K_LEFT: "move_left",
            pygame.K_RIGHT: "move_right",
            pygame.K_ESCAPE: "escape",
            pygame.K_RETURN: "action_button",
        }

        for key, action in key_actions.items():
            if keys[key]:
                self.handle_action(action)


    def handle_action(self, action):
        if self.control_state == "player":
            if action in ("move_up", "move_down", "move_left", "move_right"):
                event_system.raise_event(action)
            elif action == "escape":
                event_system.raise_event("open_menu")
            elif action == "action_button":
                event_system.raise_event("action_button")

        elif self.control_state == "battle":
            event_system.raise_event(f"battle_{action}")

        elif self.control_state == "menu":
            event_system.raise_event(f"menu_{action}")

        elif self.control_state == "dialog":
            event_system.raise_event(f"dialog_{action}")




    def events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
            elif event.type == pygame.KEYUP:
                self.handle_keyup(event.key)

    def handle_keydown(self, key):
        pass

    def handle_keyup(self, key):
        pass
