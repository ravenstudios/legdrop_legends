from constants import *
import pygame
import state_manager

import os

# Set window position to monitor 3
os.environ['SDL_VIDEO_WINDOW_POS'] = "-1200,0"



clock = pygame.time.Clock()

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.init()
pygame.joystick.init()

state_manager = state_manager.StateManager()


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
    # for i in range(joystick.get_numbuttons()):
    #     if joystick.get_button(i):
    #         print(f"Button {i} is pressed")
    state_manager.update()
    # pygame.display.set_caption(f"FPS:{clock.get_fps()}")
def events(events):
    state_manager.events(events)

def draw():
    surface.fill((200, 200, 200))#background
    # draw_grid(surface)
    state_manager.draw(surface)
    # pygame.draw.line(surface, RED, (GAME_WIDTH // 2, 0), (GAME_WIDTH // 2, GAME_HEIGHT), 1)
    # pygame.draw.line(surface, RED, (0, GAME_HEIGHT // 2), (GAME_WIDTH, GAME_HEIGHT // 2), 1)

    pygame.display.flip()

def draw_grid(surface):
    for col in range(GAME_WIDTH):
        for row in range(GAME_HEIGHT):
            if (row + col) % 2 == 0:
                color = (0, 200, 0)
            else:
                color = (0, 150, 0)

            pygame.draw.rect(surface, color, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), width=0)

if __name__ == "__main__":
    main()
