class PlayerBattleObject():
    def __init__(self):
        self.hp = 50
        self.mp = 20
        self.max_hp = 100
        self.max_mp = 50
        self.options = {
            "Attacks": [
                {"name": "Chop", "dmg": 3, "cost": 2, "type":"attack", "message":"Player used Chop"},
                {"name": "Kick", "dmg": 5, "cost": 2, "type":"attack", "message":"Player used Kick"},
                {"name": "Back"}
            ],
            "Items": [
                {"name": "Bandaid", "hp": 5, "type":"restore_hp", "message":"Player used Bandaid"},
                {"name": "Beer", "mp": 3, "type":"restore_mp", "message":"Player used Beer"},
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
