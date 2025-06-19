import npc
import sys
import os
import enemy_battle_object


import npc
class Clown(npc.NPC):
    """docstring for "warrior."""

    def __init__(self):
        super().__init__(400, 200, "clown_16x16-Sheet.png")
        self.battle_object = enemy_battle_object.EnemyBattleObject(500, 50, "clown_32x32.png", 1)
        self.battle_object.hp = 50
        self.battle_object.mp = 30
        self.battle_object.max_hp = 75
        self.battle_object.max_mp = 50
        self.battle_object.name = "Funny Guy"
        self.battle_object.options = {
            "Attacks": [
                {"name": "Chop", "dmg": 3, "cost": 2, "type":"attack", "message":"Player used Chop"},
                {"name": "Kick", "dmg": 5, "cost": 2, "type":"attack", "message":"Player used Kick"},
                {"name": "Back"}
            ],
            "Items": [
                {"name": "Bandaid", "hp": 5, "type":"restore_hp", "message":"Player used Bandaid"},
                {"name": "Beer", "mp": 10, "type":"restore_mp", "message":"Player used Beer"},
                {"name": "Powder", "mp": 5, "type":"restore_mp", "message":"Player powered"},
                {"name": "Back"}
            ],
            "Tag Partner": [
                {"name": "Tag Partner", "type":"tag", "message":"Player tagged"},
                {"name": "Back"},

            ],
            "Powder": [
                {"name": "Powder", "mp": 0, "type":"restore_mp", "message":""},
                {"name": "Back"},
            ],

            "Run": [
                {"name": "Run", "type":"run", "message":"Player tried running"},
                {"name": "Back"},
            ]
        }
