import pygame

class MessageDisplay(object):

    def __init__(self):
        self.message_index = 0
        self.message = ""
        self.message_buffer = ""
        self.message_speed = 30
        self.last_message_update = 0



    def update(self):
        if self.message and self.message_index < len(self.message):
            current_time = pygame.time.get_ticks()

            if (self.message and
                self.message_index < len(self.message) and
                current_time - self.last_message_update >= self.message_speed):

                self.message_buffer += self.message[self.message_index]
                self.message_index += 1
                self.last_message_update = current_time


    def draw(self, surface):
        pass

    def get_message(self):
        return self.message_buffer


    def set_message(self, message):
        self.message_buffer = ""
        self.message_index = 0
        self.message = message
