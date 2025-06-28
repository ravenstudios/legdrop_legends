import pygame
from constants import *
from battle import Battle
from states import state, battle_state

class DialogDisplay(pygame.sprite.Sprite):
    def __init__(self, event_system):
        super().__init__()
        self.event_system = event_system

        # Hook to events
        self.event_system.on("dialog_start_chat", self.chat)
        self.event_system.on("dialog_set_visible", self.set_visible)
        self.event_system.on("dialog_set_has_controles", self.set_has_controles)
        self.event_system.on("dialog_action_end_dialogue", self.back)  # <- Handles end

        self.width = BLOCK_SIZE * 10
        self.height = BLOCK_SIZE * 3
        self.x = GAME_WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - self.height

        # State
        self.is_visible = False
        self.has_controles = False
        self.showing_options = False
        self.index = 0

        self.npc = None
        self.dialog = None
        self.current_node = None

        # Surface
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        # Font
        self.font = pygame.font.SysFont(None, 28)
        self.text = ""
        self.running_text = ""
        self.text_index = 0

    # ------------------------------
    # Event Hooks
    # ------------------------------

    def set_has_controles(self, value):
        self.has_controles = value


    def set_visible(self, visible):
        self.is_visible = visible

    def update(self):
        if self.text_index < len(self.text):
            self.running_text += self.text[self.text_index]
            self.text_index += 1
            self.update_text(self.running_text)
    # ------------------------------
    # Input Handling
    # ------------------------------

    def events(self, events):
        if not self.has_controles or not self.is_visible:
            return
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.showing_options:
                    if event.key == pygame.K_UP:
                        self.index = (self.index - 1) % len(self.dialog[self.current_node]["options"])
                        self.update_text()
                    elif event.key == pygame.K_DOWN:
                        self.index = (self.index + 1) % len(self.dialog[self.current_node]["options"])
                        self.update_text()
                if event.key == pygame.K_RETURN:
                    self.enter()
                elif event.key == pygame.K_ESCAPE:
                    self.back()

    def back(self, arg=None):
        self.is_visible = False
        self.has_controles = False
        self.showing_options = False
        self.index = 0
        self.event_system.raise_event("player_set_in_dialog", False)

    def enter(self):
        node = self.dialog[self.current_node]

        if "options" in node:
            keys = list(node["options"].keys())
            selected_key = keys[self.index]
            next_node_key = node["options"][selected_key].get("next")
            if next_node_key:
                self.display_node(next_node_key)
            else:
                self.back()
            return

        if "text" in node and "next" in node:
            self.display_node(node["next"])
            return

        if "action" in node:
            if node["action"] == "start_battle":
                player = self.event_system.raise_event("player_get_player", False)[0]
                bs = battle_state.BattleState(player, self.npc)
                self.event_system.raise_event("change_state", bs)
                self.back()
            # self.event_system.raise_event(f"dialog_action_{node['action']}")
            # If action is 'end_dialogue', 'back' will be called from the event hook
                return
            if node["action"] == "end_dialogue":
                self.back()

        self.back()

    # ------------------------------
    # Dialog Flow
    # ------------------------------

    def chat(self, npc):
        self.npc = npc
        self.dialog = self.npc.dialog
        self.current_node = "start"
        self.showing_options = False
        self.index = 0
        self.set_visible(True)
        self.set_has_controles(True)
        # self.update_text(self.dialog[self.current_node].get("text", ""))
        self.text = self.dialog[self.current_node].get("text", "")
        self.text_index = 0
        self.running_text = ""
    def display_node(self, node_key):
        self.current_node = node_key
        node = self.dialog[node_key]
        self.index = 0
        self.showing_options = "options" in node

        if self.showing_options:
            self.update_text()
        else:
            # self.update_text(node.get("text", ""))
            self.text = node.get("text", "")
            self.text_index = 0
            self.running_text = ""
    # ------------------------------
    # Drawing Text
    # ------------------------------

    def update_text(self, text=None):
        self.image.fill((20, 20, 20))
        y_offset = 10

        if text is not None:
            max_chars = 50
            lines = []
            while len(text) > max_chars:
                split_at = text.rfind(" ", 0, max_chars)
                if split_at == -1:
                    split_at = max_chars
                lines.append(text[:split_at])
                text = text[split_at:].lstrip()
            lines.append(text)

            for i, line in enumerate(lines):
                line_surf = self.font.render(line, True, (255, 255, 255))
                self.image.blit(line_surf, (10, y_offset + i * self.font.get_linesize()))

        elif self.showing_options:
            node = self.dialog[self.current_node]
            options = node.get("options", {})
            for idx, (key, option) in enumerate(options.items()):
                color = (255, 255, 0) if idx == self.index else (200, 200, 200)
                option_surf = self.font.render(option["text"], True, color)
                self.image.blit(option_surf, (20, y_offset + idx * self.font.get_linesize()))
                if idx == self.index:
                    pygame.draw.rect(
                        self.image,
                        (255, 255, 0),
                        (15, y_offset + idx * self.font.get_linesize() - 2, self.width - 30, self.font.get_linesize() + 4), 2)
