from constants import *
import pygame
import state_manager
import player
import block
import camera

clock = pygame.time.Clock()

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.init()
state_manager = state_manager.StateManager()

player = player.Player()
player_group = pygame.sprite.Group()
player_group.add(player)
blocks_group = pygame.sprite.Group()
camera = camera.Camera()
for i in range(6):
    if i == 0 or i == 9:
        color = (255, 255, 255)
    else:
        color = BLUE
    blocks_group.add (block.Block(i * BLOCK_SIZE + i * BLOCK_SIZE, 0, color))
    blocks_group.add (block.Block(0, i * BLOCK_SIZE + i * BLOCK_SIZE, color))
blocks_group.add (block.Block(WORLD_WIDTH - BLOCK_SIZE, 0, RED))
blocks_group.add (block.Block(0, 0, RED))
blocks_group.add (block.Block(0, WORLD_HEIGHT - BLOCK_SIZE, RED))
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

    cam_offset = camera.update_offset(player)
    player_group.update(cam_offset)
    # print(cam_offset)
    blocks_group.update(cam_offset)

    pygame.display.set_caption(f"cam:{cam_offset}  |  Y:{player.y}  |  Rect.center.y:{player.rect.center[1]}  |  WORLD:{WORLD_WIDTH}-{WORLD_HEIGHT}  |  Halfscreen:{GAME_WIDTH // 2}")

def draw():
    surface.fill((200, 200, 200))#background

    state_manager.draw(surface)
    player_group.draw(surface)
    blocks_group.draw(surface)

    pygame.draw.line(surface, RED, (GAME_WIDTH // 2, 0), (GAME_WIDTH // 2, GAME_HEIGHT), 1)
    pygame.draw.line(surface, RED, (0, GAME_HEIGHT // 2), (GAME_WIDTH, GAME_HEIGHT // 2), 1)

    pygame.display.flip()







if __name__ == "__main__":
    main()
