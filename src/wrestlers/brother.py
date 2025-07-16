import objects.npc
import objects.battle_object
from event_system import event_system

import objects.npc
class Brother(objects.npc.NPC):
    def __init__(self, x=500, y=50):
        super().__init__(300, 350, "Brother16x16-Sheet.png")

        self.battle_object = objects.battle_object.BattleObject(x, y, "brother_32x32-Sheet.png", 20)

        self.battle_object.max_hp = 50
        self.battle_object.max_mp = 50

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
        self.battle_object.name = "Brother"
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
                {"name": "Leg Drop", "power": 15, "cost": 5, "type":"attack"},
                {"name": "Clothesline", "power": 20, "cost": 7, "type":"attack"},
                {"name": "Choke Hold", "power": 10, "cost": 7, "type":"poison"},
                {"name": "Powder", "mp": 20, "type":"restore_mp", "message":"Player powered"},
                {"name": "Back"}
            ],
            "Items": [
                {"name": "Bandaid - HP+25", "hp": 25, "type":"restore_hp", "message":"Player used Bandaid", "qty":3},
                {"name": "Beer - MP+10", "mp": 25, "type":"restore_mp", "message":"Player used Beer", "qty":3},

                {"name": "Back"}
            ],
            "Tag Partner": [
                {"name": "Tag Partner", "type":"tag", "message":"Player tagged"},
                {"name": "Back"},

            ],

            "Run": [
                {"name": "Run", "type":"run", "message":"Player tried running"},
                {"name": "Back"},
            ]
        }

        self.dialog = {
            "start": {
                "text": "Big Rick stares you down.",
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
                "text": "Big Rick: 'Name's Big Rick. King of the Backyard. Ain’t nobody throws a slam like me.'",
                "next": "options"
            },
            "where": {
                "text": "Big Rick: 'This here’s The Yard. Broken fences, busted dreams, and a whole lotta bruised egos.'",
                "next": "options"
            },
            "fight": {
                "text": "Big Rick: 'HA! Now you're speakin' my language!'",
                "action": "start_battle"
            },
            "no_fight": {
                "text": "Big Rick: 'Tch... Figures. Come back when you grow a spine.'",
                "action": "end_dialogue"
            }
        }

        def heal(self):
            self.battle_object.hp = self.battle_object.max_hp
            self.battle_object.mp = self.battle_object.max_mp
            self.battle_object.is_poisoned = False
