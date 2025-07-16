from constants import *
import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "-1200,0"
clock = pygame.time.Clock()
pygame.init()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.joystick.init()
joysticks = []
joystick = None

import state_manager

for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)
if joysticks:
    joystick = joysticks[0]
state_manager = state_manager.StateManager(joystick)


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        py_events = pygame.event.get()
        for event in py_events:

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False
        events(py_events)
        update()
        draw()

    pygame.quit()


def update():
    state_manager.update()


def events(events):
    state_manager.events(events)


def draw():
    surface.fill((30, 30, 30))
    state_manager.draw(surface)
    pygame.display.flip()


if __name__ == "__main__":
    main()
