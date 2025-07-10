import objects.npc
import objects.enemy_battle_object


import objects.npc
class Brother(objects.npc.NPC):

    def __init__(self, event_system):
        super().__init__(400, 350, "Brother16x16-Sheet.png")
        self.event_system = event_system
        self.battle_object = objects.enemy_battle_object.EnemyBattleObject(50, 500, "Brother64x64-Sheet.png", 20, "cd")

        self.battle_object.max_hp = 40
        self.battle_object.max_mp = 35

        self.battle_object.hp = self.battle_object.max_hp
        self.battle_object.mp = self.battle_object.max_mp

        self.battle_object.speed = 40
        self.battle_object.power = 40
        self.battle_object.defense = 40
        self.battle_object.technique = 45
        self.battle_object.charisma = 40
        self.battle_object.luck = 50
        self.battle_object.type_class = "grappler"



        self.battle_object.options = {
            "Attacks": [
                {"name": "Leg Drop", "power": 20, "cost": 5, "type":"attack", "message":"Player used Chop, it dealt 3 damage."},
                {"name": "Clothesline", "power": 25, "cost": 7, "type":"attack", "message":"Player used Kick, it dealt 5 damage."},
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
