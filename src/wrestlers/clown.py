import objects.npc
import objects.battle_object


import objects.npc
class Clown(objects.npc.NPC):
    def __init__(self, x=700, y=50):
        super().__init__(x, y, "clown_16x16-Sheet.png")
        self.battle_object = objects.battle_object.BattleObject(x, y, "clown_32x32.png", 1)
        self.battle_object.max_hp = 20
        self.battle_object.max_mp = 100
        self.battle_object.hp = self.battle_object.max_hp
        self.battle_object.mp = self.battle_object.max_mp
        self.battle_object.level = 1
        self.battle_object.exp = 0
        self.battle_object.powder_rate = 30

        self.battle_object.speed = 60
        self.battle_object.power = 50
        self.battle_object.defense = 40

        self.battle_object.technique = 60
        self.battle_object.charisma = 50
        self.battle_object.luck = 10
        self.battle_object.type_class = "High Flyer"
        self.battle_object.is_poisoned = False
        self.battle_object.name = "Clown"
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
                {"name": "Silly Slap", "power": 10, "cost": 2, "type":"attack", "message":f"{self.battle_object.name} used Silly Slap, it dealt 3 damage"},
                {"name": "Head Juggle", "power": 15, "cost": 6, "type":"attack", "message":f"{self.battle_object.name} used Head Juggle, it dealt 2 damage"},
                            ],

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
