from wrestlers.crawdaddy import Crawdaddy
from wrestlers.clown import Clown
from wrestlers.brother import Brother
from npcs.nurse import Nurse



class NPCManager(object):
    def __init__(self):
        self.npcs = {
            "crawdaddy":Crawdaddy,
            "clown":Clown,
            "brother":Brother,
            "nurse":Nurse,
        }


    def update(self):
        pass

    def load(self, npc_type, x, y):
        npc_class = self.npcs.get(npc_type)
        if npc_class:
            return npc_class(x, y)  # instantiate the class
        else:
            print(f"[ERROR] Unknown NPC type: {npc_type}")
            return None
npc_manager = NPCManager()
