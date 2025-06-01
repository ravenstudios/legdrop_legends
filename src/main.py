from constants import *
import pygame
import state_manager



clock = pygame.time.Clock()

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.init()

state_manager = state_manager.StateManager()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

        update()
        draw()

    pygame.quit()

def update():

    state_manager.update()
    # pygame.display.set_caption(f"cam:{cam_offset}  |  Y:{player.y}  |  Rect.center.y:{player.rect.center[1]}  |  WORLD:{WORLD_WIDTH}-{WORLD_HEIGHT}  |  Halfscreen:{GAME_WIDTH // 2}")

def draw():
    surface.fill((200, 200, 200))#background

    state_manager.draw(surface)
    # pygame.draw.line(surface, RED, (GAME_WIDTH // 2, 0), (GAME_WIDTH // 2, GAME_HEIGHT), 1)
    # pygame.draw.line(surface, RED, (0, GAME_HEIGHT // 2), (GAME_WIDTH, GAME_HEIGHT // 2), 1)
    pygame.display.flip()


if __name__ == "__main__":
    main()
