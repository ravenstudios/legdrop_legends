import objects.npc
import objects.battle_object


import objects.npc
class Clown(objects.npc.NPC):
    def __init__(self, x=700, y=50):
        print(x)
        super().__init__(500, 350, "clown_16x16-Sheet.png")
        self.battle_object = objects.battle_object.BattleObject(x, y, "clown_32x32.png", 1)
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
                {"name": "Silly Slap", "power": 5, "cost": 2, "type":"attack", "message":f"{self.battle_object.name} used Silly Slap, it dealt 3 damage"},
                {"name": "Head Juggle", "power": 10, "cost": 2, "type":"attack", "message":f"{self.battle_object.name} used Head Juggle, it dealt 2 damage"},
                            ],
            # "Items": [
            #     {"name": "Bandaid", "hp": 5, "type":"restore_hp", "message":f"{self.battle_object.name} used Bandaid"},
            #     {"name": "Beer", "mp": 10, "type":"restore_mp", "message":f"{self.battle_object.name} used Beer"},
            #     {"name": "Powder", "mp": 5, "type":"restore_mp", "message":f"{self.battle_object.name} powered"},
            #                 ],
            # "Tag Partner": [
            #     {"name": "Tag Partner", "type":"tag", "message":"Player tagged"},
            #
            #
            # ],
            # "Powder": [
            #     {"name": "Powder", "mp": 0, "type":"restore_mp", "message":""},
            #
            # ],
            #
            # "Run": [
            #     {"name": "Run", "type":"run", "message":"Player tried running"},
            #
            # ]
        }
        self.dialog = {
        "start": {
            "text": "A squeaky horn honks from nowhere... Slappy Taffy rolls up in a tiny invisible car. 'HONK HONK! You lookin’ for a laugh or a smackdown?'",
            "next": "options"
        },
        "options": {
            "options": {
                "1": {"text": "I’m here to fight, clown.", "next": "fight"},
                "2": {"text": "No thanks, I’m allergic to greasepaint.", "next": "no_fight"},
                "3": {"text": "Who even *are* you?", "next": "who"},
                "4": {"text": "Where *is* this?", "next": "where"},
            }
        },
        "who": {
            "text": "Slappy Taffy: 'Name’s Slappy Taffy — the ticklish terror of turnbuckle town! I’ve tripped over more chairs than you’ve seen matches!'",
            "next": "options"
        },
        "where": {
            "text": "Slappy Taffy: 'This? This is The Yard, baby! Where dreams go SPLAT and pies go SMACK. Step right up!'",
            "next": "options"
        },
        "fight": {
            "text": "Slappy Taffy: 'AHAHAHA! Let’s see if you can dodge my Balloon Suplex!'",
            "action": "start_battle"
        },
        "no_fight": {
            "text": "Slappy Taffy: 'Pfft... You’re about as fun as a flat whoopee cushion. Come back when you're ready to boogie with the buffoon.'",
            "action": "end_dialogue"
        }
    }
