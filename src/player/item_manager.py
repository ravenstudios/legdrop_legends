from event_system import event_system


class ItemManager():
    def __init__(self):
        self.items = [
            {"name": "Bandaid", "hp": 25, "type":"restore_hp", "qty":3},
            {"name": "Beer", "mp": 25, "type":"restore_mp", "qty":3}
        ]
        event_system.on("get_items", self.get_items)


    def get_items(self):
        return self.items


    def update(self):
        pass


    def draw(self, surfce):
        pass

item_manager = ItemManager()
