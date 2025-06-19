class PlayerBattleObject():
    def __init__(self):
        self.hp = 30
        self.mp = 20
        self.max_hp = 30
        self.max_mp = 20
        self.options = {
            "Attacks": [
                {"name": "Chop - D:3  C:2", "dmg": 3, "cost": 2, "type":"attack", "message":"Player used Chop, it dealt 3 damage."},
                {"name": "Kick - D:5  C:5", "dmg": 5, "cost": 5, "type":"attack", "message":"Player used Kick, it dealt 5 damage."},
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
