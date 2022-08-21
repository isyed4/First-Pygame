import pygame
import os


# width and height of window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# os helps with path finding regardless of operating system
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window():
    WIN.fill((WHITE))
    # use blit when you want to draw a surface on the screen
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (300, 100))
    WIN.blit(RED_SPACESHIP_IMAGE, (700, 100))
    pygame.display.update()


# pygame event loop, what is going to pop up on screen?
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
