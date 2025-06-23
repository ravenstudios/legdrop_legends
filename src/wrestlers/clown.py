import objects.npc
import objects.enemy_battle_object
import objects.npc

class Clown(objects.npc.NPC):
    def __init__(self, event_system):
        super().__init__(500, 150, "clown_16x16-Sheet.png")
        self.event_system = event_system
        self.battle_object = objects.enemy_battle_object.EnemyBattleObject(500, 50, "clown_32x32.png", 1)
        self.battle_object.hp = 30
        self.battle_object.mp = 20
        self.battle_object.max_hp = 30
        self.battle_object.max_mp = 20
        self.battle_object.powder_rate = 10
        self.battle_object.name = "Funny Guy"
        self.level = 1
        self.def = 5
        self.class = "tactician"
        self.luck = 5
        self.face = 0
        self.heel = 0

        self.battle_object.options = {
            "Attacks": [
                {"name": "Silly Slap", "dmg": 3, "cost": 2, "type":"attack", "message":f"{self.battle_object.name} used Silly Slap, it dealt 3 damage"},
                {"name": "Head Juggle", "dmg": 2, "cost": 2, "type":"attack", "message":f"{self.battle_object.name} used Head Juggle, it dealt 2 damage"},
                            ],
            "Items": [
                {"name": "Bandaid", "hp": 5, "type":"restore_hp", "message":f"{self.battle_object.name} used Bandaid"},
                {"name": "Beer", "mp": 10, "type":"restore_mp", "message":f"{self.battle_object.name} used Beer"},
                {"name": "Powder", "mp": 5, "type":"restore_mp", "message":f"{self.battle_object.name} powered"},
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
