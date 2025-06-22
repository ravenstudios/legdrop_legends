import npc
import sys
import os
import enemy_battle_object


import npc
class Crawdaddy(npc.NPC):
    """docstring for "warrior."""

    def __init__(self, event_system):
        super().__init__(400, 350, "craw daddy-Sheet.png")
        self.event_system = event_system
        self.battle_object = enemy_battle_object.EnemyBattleObject(500, 50, "crawdaddy_32x32-Sheet.png", 20)
        self.battle_object.hp = 30
        self.battle_object.mp = 20
        self.battle_object.max_hp = 30
        self.battle_object.max_mp = 20
        self.battle_object.powder_rate = 10
        self.battle_object.name = "Craw Daddy"
        self.battle_object.options = {
            "Attacks": [
                {"name": "Chop", "dmg": 3, "cost": 2, "type":"attack", "message":"Craw Daddy used Chop, it dealt 3 damage"},
                {"name": "Kick", "dmg": 5, "cost": 2, "type":"attack", "message":"Craw Daddy used Kick, it dealt 5 damage"},
                            ],
            "Items": [
                {"name": "Bandaid", "hp": 5, "type":"restore_hp", "message":"Craw Daddy used Bandaid"},
                {"name": "Beer", "mp": 10, "type":"restore_mp", "message":"Craw Daddy used Beer"},
                {"name": "Powder", "mp": 5, "type":"restore_mp", "message":"Craw Daddy powered"},
                            ],
            "Tag Partner": [
                {"name": "Tag Partner", "type":"tag", "message":"Player tagged"},


            ],
            "Powder": [
                {"name": "Powder", "mp": 0, "type":"restore_mp", "message":""},

            ],

            "Run": [
                {"name": "Run", "type":"run", "message":"Player tried running"},
                {"name": "Back"},
            ]
        }
        self.dialog = f"Hello my name is {self.battle_object.name}. This is where we test the game dialog."

        # def update(self):
        #     print("update")
        #     self.battle_object.hp = min(0, max(self.battle_object.hp, self.battle_object.max_hp))
        #     self.battle_object.mp = min(0, max(self.battle_object.mp, self.battle_object.max_mp))
