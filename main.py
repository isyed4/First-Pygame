import pygame
import os




# width and height of window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)

FPS = 60

# os helps with path finding regardless of operating system
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))


def draw_window():
        WIN.fill((WHITE))
        # use blit when you want to draw a surface on the screen
        WIN.blit()
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


