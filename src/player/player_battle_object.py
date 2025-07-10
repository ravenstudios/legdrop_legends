class PlayerBattleObject():
    def __init__(self):

        # total 280
        self.max_hp = 40
        self.max_mp = 35

        self.hp = self.max_hp
        self.mp = self.max_mp

        self.speed = 40
        self.power = 40
        self.defense = 40
        self.technique = 45
        self.charisma = 40
        self.luck = 50
        self.type_class = "grappler"



        self.options = {
            "Attacks": [
                {"name": "Chop - D:3  C:2", "power": 20, "cost": 5, "type":"attack", "message":"Player used Chop, it dealt 3 damage."},
                {"name": "Kick - D:5  C:5", "power": 25, "cost": 7, "type":"attack", "message":"Player used Kick, it dealt 5 damage."},
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
