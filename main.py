import pygame
import os


# width and height of window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
velocity = 5
BULLET_VEL = 7
MAX_BULLETS = 3


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
    pygame.draw.rect(WIN, BLACK, BORDER)
    # use blit when you want to draw a surface on the screen
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - velocity > 0:  # LEFT
        yellow.x -= velocity
    if keys_pressed[pygame.K_d] and yellow.x + velocity + yellow.width < BORDER.x:  # RIGHT
        yellow.x += velocity
    if keys_pressed[pygame.K_w] and yellow.y - velocity > 0:  # UP
        yellow.y -= velocity
    if keys_pressed[pygame.K_s] and yellow.y + velocity + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += velocity


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - velocity > BORDER.x + BORDER.width:  # LEFT
        red.x -= velocity
    if keys_pressed[pygame.K_RIGHT] and red.x + velocity + red.width < WIDTH:  # RIGHT
        red.x += velocity
    if keys_pressed[pygame.K_UP] and red.y - velocity > 0:  # UP
        red.y -= velocity
    if keys_pressed[pygame.K_DOWN] and red.y + velocity + red.height < HEIGHT - 15:  # DOWN
        red.y += velocity


# pygame event loop, what is going to pop up on screen?
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    # BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_SEMICOLON and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    # BULLET_FIRE_SOUND.play()
        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        


        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
