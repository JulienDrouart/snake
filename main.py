import pygame, sys
import random
import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((550, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
"""surface = pygame.image.load('logo.jpg')
pygame.display.set_icon(surface)
fond = pygame.image.load("fond.jpg")"""
run = True
start = False
snakeHeadCooX= 260
snakeHeadCooY = 310
currentTimer = 1
snakeHead = Rect(snakeHeadCooX, snakeHeadCooY, 30, 30)
direction = "null"
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.draw.rect(screen, (255, 0, 0), snakeHead)
targetCooX = (random.randint(0, 10) * 50) + 25
targetCooY = (random.randint(1, 11) * 50) + 25
target = pygame.draw.circle(screen, (255, 255, 255), (targetCooX, targetCooY) , 15)

timerEverySeconds = time.time()

"""
Idées
Accélération du timer régulièrement


"""
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if start is False:
                timerEverySeconds = time.time()
                start = True
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"
            if event.key == pygame.K_LEFT:
                direction = "left"
                snakeHeadCooX = snakeHeadCooX-1
            if event.key == pygame.K_RIGHT:
                direction = "right"
                snakeHeadCooX = snakeHeadCooX + 1
    if time.time() > timerEverySeconds + currentTimer and start is True:
        if direction == "down":
            snakeHeadCooY = snakeHeadCooY + 50
        if direction == "up":
            snakeHeadCooY = snakeHeadCooY - 50
        if direction == "left":
            snakeHeadCooX = snakeHeadCooX - 50
        if direction == "right":
            snakeHeadCooX = snakeHeadCooX + 50

        timerEverySeconds = time.time()
        screen.fill((0,0,0))
        target = pygame.draw.circle(screen, (255, 255, 255), (targetCooX, targetCooY), 15)
        snakeHead = Rect(snakeHeadCooX, snakeHeadCooY, 30, 30)
        pygame.draw.rect(screen, (255, 0, 0), snakeHead)



    pygame.display.flip()

pygame.quit()
quit()