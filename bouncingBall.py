import pygame
from pygame.locals import  *
import sys
import random

from typer.rich_utils import MAX_WIDTH

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAME_PER_SECOND = 60
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load('images/ball.png')
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)

xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()

    if (ballRect.left < 0) or (ballRect.right > WINDOW_WIDTH):
        xSpeed = -xSpeed
        bounceSound.play()
    if (ballRect.top < 0) or (ballRect.bottom > WINDOW_HEIGHT):
        ySpeed = -ySpeed
        bounceSound.play()

    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    window.fill(BLACK)
    window.blit(ballImage, ballRect)
    pygame.display.update()
    clock.tick(FRAME_PER_SECOND)
