import objects.npc
import objects.battle_object
from event_system import event_system

import objects.npc
class Punching_bag(objects.npc.NPC):
    def __init__(self, x=600, y=50):
        super().__init__(600, 350, "punching_bag16x16.png")

        self.battle_object = objects.battle_object.BattleObject(x, y, "punching_bag32x32.png", 1)

        self.battle_object.max_hp = 50
        self.battle_object.max_mp = 50
        self.y_sprite_sheet_index = 0
        self.frame = 0
        self.max_frame = 0
        self.animation_speed = 0
        self.ticks_till_frame_change = self.animation_speed

        self.battle_object.hp = self.battle_object.max_hp
        self.battle_object.mp = self.battle_object.max_mp
        self.battle_object.level = 5
        self.battle_object.exp = 0
        self.battle_object.speed = 50
        self.battle_object.power = 50
        self.battle_object.defense = 50
        self.battle_object.technique = 50
        self.battle_object.charisma = 50
        self.battle_object.luck = 10
        self.battle_object.type_class = "Grappler"
        self.battle_object.is_poisoned = False
        self.battle_object.name = "Punching Bag"
        self.battle_object.stats = [
            self.battle_object.level,
            self.battle_object.exp,
            self.battle_object.speed,
            self.battle_object.power,
            self.battle_object.defense,
            self.battle_object.technique,
            self.battle_object.charisma,
            self.battle_object.luck
        ]

        self.battle_object.options = {
            "Attacks": [
                {"name": "Swing", "power": 2, "cost": 1, "type":"attack"},
                {"name": "Stand", "power": 0, "cost": 0, "type":"attack"},
                        ]
                    }
            #
            # ],
            # "Items": [
            #     {"name": "Bandaid - HP+25", "hp": 25, "type":"restore_hp", "message":"Player used Bandaid", "qty":3},
            #     {"name": "Beer - MP+10", "mp": 25, "type":"restore_mp", "message":"Player used Beer", "qty":3},
            #
            #
            # ],
            # "Tag Partner": [
            #     {"name": "Tag Partner", "type":"tag", "message":"Player tagged"},
            #
            #
            # ],
            #
            # "Run": [
            #     {"name": "Run", "type":"run", "message":"Player tried running"},
            #
            # ]


        self.dialog = {
            "start": {
                "text": "Punching bag stands still",
                "next": "options"
            },
            "options": {
                "options": {
                    "1": {"text": "I'm here to fight. Let’s do this.", "next": "fight"},
                    "2": {"text": "Not lookin’ for trouble.", "next": "no_fight"},
                    "3": {"text": "Who are you, anyway?", "next": "who"},
                    "4": {"text": "What is this place?", "next": "where"},
                }
            },
            "who": {
                "text": "Punching Bag: '...................'",
                "next": "options"
            },
            "where": {
                "text": "Brother: 'Hit the punching bag already!'",
                "next": "options"
            },
            "fight": {
                "text": "Punching Bag: '...................'",
                "action": "start_battle"
            },
            "no_fight": {
                "text": "Brother: 'Wow your really a wuss",
                "action": "end_dialogue"
            }
        }

        def heal(self):
            self.battle_object.hp = self.battle_object.max_hp
            self.battle_object.mp = self.battle_object.max_mp
            self.battle_object.is_poisoned = False
