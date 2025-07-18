import objects.npc
import objects.battle_object
from event_system import event_system

import objects.npc
class Nurse(objects.npc.NPC):
    def __init__(self, x=800, y=50):
        super().__init__(1000, 300, "Nurse-Sheet.png")


        self.dialog = {
            "start": {
                "text": "Nurse: Hello, I'm the nurse, What do you need help with?",
                "next": "options"
            },
            "options": {
                "options": {
                    "1": {"text": "Im injured.", "next": "heal"},
                    "2": {"text": "Are you single.", "next": "single"},
                    "3": {"text": "Does this cost money?", "next": "cost"},
                    "4": {"text": "Thanks, i'll be going now.", "next": "leave"},
                }
            },
            "heal": {
                "text": "Nurse: Just relax and we'll get you fixed up.'",
                "action": "heal",
                "next": "options"
            },
            "single": {
                "text": "Nurse: Awww thats so cute, but aren’t you just a kid?.",
                "next": "options"
            },
            "cost": {
                "text": "Nurse: No, we hope to be able to claim that we healed the next super star.",
                "next": "options"
            },
            "leave": {
                "text": "Nurse: Be careful, doing high spots on trampolines cause injurys. ",
                "action": "end_dialogue"
            }
        }
