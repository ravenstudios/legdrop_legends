import pygame
from event_system import event_system


class TimerManager:
    def __init__(self):
        self.timers = []
        event_system.on("add_timer", self.add_timer)

    def add_timer(self, data):
        timer = {
            "start": pygame.time.get_ticks(),
            "delay": data[0],
            "callback": data[1],
            "one_shot": data[2],
            "done": False
        }
        self.timers.append(timer)

    def update(self):
        now = pygame.time.get_ticks()
        for timer in self.timers:
            if not timer["done"] and now - timer["start"] >= timer["delay"]:
                timer["callback"]()
                if timer["one_shot"]:
                    timer["done"] = True
                else:
                    timer["start"] = now  # reset for repeating

        # Remove finished one-shot timers
        self.timers = [t for t in self.timers if not t["done"]]
timer_manager = TimerManager()
