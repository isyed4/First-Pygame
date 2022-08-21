import pygame
import os


# width and height of window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
velocity = 5

# os helps with path finding regardless of operating system
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill((WHITE))
    # use blit when you want to draw a surface on the screen
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]: # LEFT
        yellow.x -= velocity
    if keys_pressed[pygame.K_d]: # RIGHT
        yellow.x += velocity
    if keys_pressed[pygame.K_w]: # UP
        yellow.y -= velocity
    if keys_pressed[pygame.K_s]: # DOWN
        yellow.y += velocity

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: # LEFT
        red.x -= velocity
    if keys_pressed[pygame.K_RIGHT]: # RIGHT
        red.x += velocity
    if keys_pressed[pygame.K_UP]: # UP
        red.y -= velocity
    if keys_pressed[pygame.K_DOWN]: # DOWN
        red.y += velocity


# pygame event loop, what is going to pop up on screen?
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        


        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
