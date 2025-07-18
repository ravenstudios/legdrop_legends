import pygame
from constants import *
from battle import battle
from states import state, battle_state
from player import player
from event_system import event_system


# Created from world_state
class DialogDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        print("DialogDisplay initialized and event listeners registered")

        
        event_system.on("dialog_start_chat", self.chat)
        event_system.on("dialog_set_visible", self.set_visible)
        event_system.on("dialog_action_end_dialogue", self.end_dialogue)
        event_system.on("dialog_index_up", self.index_up)
        event_system.on("dialog_index_down", self.index_down)
        event_system.on("dialog_enter", self.enter)
        event_system.on("dialog_back", self.back)

        self.width = BLOCK_SIZE * 10
        self.height = BLOCK_SIZE * 3
        self.x = GAME_WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - self.height

        self.is_visible = False
        self.showing_options = False
        self.index = 0

        self.npc = None
        self.dialog = None
        self.current_node = None

        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.font = pygame.font.SysFont(None, 28)
        self.text = ""
        self.running_text = ""
        self.text_index = 0
        self.pending_back = False


    def set_visible(self, visible):
        self.is_visible = visible
        if visible:
            event_system.raise_event("action_button_released")
            event_system.raise_event("set_control_state", "dialog")


    def update(self):
        # print(f"dialog_diaply:self.is_visible:{self.is_visible}")
        if self.text_index < len(self.text):
            self.running_text += self.text[self.text_index]
            self.text_index += 1
            self.update_text(self.running_text)

        if self.pending_back:
            self.pending_back = False
            self.back()

    def events(self, events):
        pass


    def index_up(self):
        node = self.dialog.get(self.current_node, {})
        options = node.get("options")

        if options:
            self.index = (self.index - 1) % len(options)
            self.update_text()


    def index_down(self):
        node = self.dialog.get(self.current_node, {})
        options = node.get("options")

        if options:
            self.index = (self.index + 1) % len(options)
            self.update_text()


    def back(self, arg=None):
        self.dialog = None
        self.is_visible = False
        self.showing_options = False
        self.index = 0
        event_system.raise_event("player_set_in_dialog", False)

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

        if "action" in node:
            if node["action"] == "start_battle":
                if event_system.raise_event("get_control_state")[0] != "dialog":
                    return

                event_system.raise_event("set_control_state", "battle")
                bs = battle_state.BattleState(self.npc)
                event_system.raise_event("change_state", bs)
                # self.is_visible = False
                self.pending_back = True  # <- delay cleanup one frame


            if node["action"] == "end_dialogue":
                self.end_dialogue()

            if node["action"] == "heal":
                print("player healed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                # player.current_wrestler.heal()
                self.display_node(node.get("next", "options"))

        if "text" in node and "next" in node:
            self.display_node(node["next"])
            return

        self.back()


    def end_dialogue(self):
        event_system.raise_event("set_control_state", "world")
        self.back()


    def chat(self, npc):
        print("chat")
        self.npc = npc
        self.dialog = self.npc.dialog
        self.current_node = "start"
        self.showing_options = False
        self.index = 0
        self.set_visible(True)
        self.text = self.dialog[self.current_node].get("text", "")
        self.text_index = 0
        self.running_text = ""


    def display_node(self, node_key):
        self.current_node = node_key
        node = self.dialog[node_key]
        self.showing_options = "options" in node
        if self.showing_options:
            self.update_text()
        else:
            self.text = node.get("text", "")
            self.text_index = 0
            self.running_text = ""


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
dialog_display = DialogDisplay()
