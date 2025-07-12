import objects.npc
import objects.enemy_battle_object
from event_system import event_system

import objects.npc
class Brother(objects.npc.NPC):

    def __init__(self, x=500, y=50):
        super().__init__(400, 350, "Brother16x16-Sheet.png")

        self.battle_object = objects.enemy_battle_object.EnemyBattleObject(x, y, "Brother64x64-Sheet.png", 20)

        self.battle_object.max_hp = 50
        self.battle_object.max_mp = 50

        self.battle_object.hp = self.battle_object.max_hp
        self.battle_object.mp = self.battle_object.max_mp

        self.battle_object.speed = 50
        self.battle_object.power = 50
        self.battle_object.defense = 50
        self.battle_object.technique = 50
        self.battle_object.charisma = 50
        self.battle_object.luck = 10
        self.battle_object.type_class = "grappler"
        self.battle_object.is_poisoned = False
        self.battle_object.name = "Brother"


        self.battle_object.options = {
            "Attacks": [
                {"name": "Leg Drop", "power": 5, "cost": 5, "type":"attack"},
                {"name": "Clothesline", "power": 10, "cost": 7, "type":"attack"},
                {"name": "Choke Hold", "power": 10, "cost": 7, "type":"poison"},
                {"name": "Powder", "mp": 10, "type":"restore_mp", "message":"Player powered"},
                {"name": "Back"}
            ],
            "Items": [
                {"name": "Bandaid - HP+5", "hp": 5, "type":"restore_hp", "message":"Player used Bandaid", "qty":3},
                {"name": "Beer - MP+10", "mp": 10, "type":"restore_mp", "message":"Player used Beer", "qty":3},

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

        def heal(self):
            self.battle_object.hp = self.battle_object.max_hp
            self.battle_object.mp = self.battle_object.max_mp
            self.battle_object.is_poisoned = False
