import objects.npc
import objects.enemy_battle_object


import objects.npc
class Crawdaddy(objects.npc.NPC):
    """docstring for "warrior."""

    def __init__(self, event_system, x=700, y=50):
        super().__init__(400, 350, "craw daddy-Sheet.png")
        self.event_system = event_system
        self.battle_object = objects.enemy_battle_object.EnemyBattleObject(x, y, "crawdaddy_32x32-Sheet.png", 20)

        self.battle_object.max_hp = 50
        self.battle_object.max_mp = 50
        self.battle_object.hp = self.battle_object.max_hp
        self.battle_object.mp = self.battle_object.max_mp
        self.battle_object.powder_rate = 50

        # total 280
        self.battle_object.speed = 50
        self.battle_object.power = 50
        self.battle_object.defense = 50
        self.battle_object.technique = 50
        self.battle_object.charisma = 50
        self.battle_object.type_class = "brawler"
        self.battle_object.is_poisoned = False

        self.battle_object.luck = 10


        self.battle_object.name = "Craw Daddy"
        self.battle_object.options = {
            "Attacks": [
                {"name": "Nipple Chop", "power": 5, "cost": 2, "type":"attack", "message":"Craw Daddy used Chop, it dealt 3 damage"},
                {"name": "Elbow", "power": 10, "cost": 2, "type":"attack", "message":"Craw Daddy used Kick, it dealt 5 damage"},
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
