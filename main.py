import pygame, sys
import random
import time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Snake')

run = True
start = gameover = False
snakeHeadCooX = 260
snakeHeadCooY = 310
direction = "null"
font = pygame.font.Font('freesansbold.ttf', 32)
snakeHead = Rect(snakeHeadCooX, snakeHeadCooY, 30, 30)
pygame.draw.rect(screen, (255, 0, 0), snakeHead)
targetCooX = random.randint(0, 970)
targetCooY = random.randint(1, 770)
target = pygame.draw.circle(screen, (255, 255, 255), (targetCooX, targetCooY), 15)
pygame.draw.circle(screen, (255, 255, 0), (snakeHeadCooX + 7, snakeHeadCooY + 15), 5)
pygame.draw.circle(screen, (255, 255, 0), (snakeHeadCooX + 22, snakeHeadCooY + 15), 5)
score = 0
snakeBody = []
clock = pygame.time.Clock()
snake_speed = 7
snake_length = 1
font = pygame.font.SysFont(None, 24)

while run:

    while gameover:
        font = pygame.font.SysFont(None, 50)
        end = font.render('Press Enter to restart game : ', True, (255, 255, 255))
        screen.blit(end, (50, 50))
        clock.tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen = pygame.display.set_mode((1000, 800))
                    run = True
                    start = gameover = False
                    snakeHeadCooX = 260
                    snakeHeadCooY = 310
                    direction = "null"
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    snakeHead = Rect(snakeHeadCooX, snakeHeadCooY, 30, 30)
                    pygame.draw.rect(screen, (255, 0, 0), snakeHead)
                    targetCooX = random.randint(0, 970)
                    targetCooY = random.randint(1, 770)
                    target = pygame.draw.circle(screen, (255, 255, 255), (targetCooX, targetCooY), 15)
                    pygame.draw.circle(screen, (255, 255, 0), (snakeHeadCooX + 7, snakeHeadCooY + 15), 5)
                    pygame.draw.circle(screen, (255, 255, 0), (snakeHeadCooX + 22, snakeHeadCooY + 15), 5)
                    score = 0
                    snakeBody = []
                    clock = pygame.time.Clock()
                    snake_speed = 7
                    snake_length = 1
                    font = pygame.font.SysFont(None, 24)
                    clock.tick(60)
                    pygame.display.flip()
    else:
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
                if event.key == pygame.K_RIGHT:
                    direction = "right"

        if start is True:
            if direction == "down":
                snakeHeadCooY = snakeHeadCooY + snake_speed
            if direction == "up":
                snakeHeadCooY = snakeHeadCooY - snake_speed
            if direction == "left":
                snakeHeadCooX = snakeHeadCooX - snake_speed
            if direction == "right":
                snakeHeadCooX = snakeHeadCooX + snake_speed

            """ if snake get out of the screen then you lose"""
            if snakeHeadCooX < 0 or snakeHeadCooX > 970 or snakeHeadCooY < 0 or snakeHeadCooY > 770:
                """gameover = True"""

            snakeBody.append([snakeHeadCooX, snakeHeadCooY])
            if len(snakeBody) > snake_length:
                del snakeBody[0]
            """ if the snake catch the target"""
            if pygame.Rect.colliderect(target, snakeHead):
                score += 1
                targetCooX = (random.randint(0, 10) * 50) + 25
                targetCooY = (random.randint(1, 11) * 50) + 25
                snake_speed += 0.5
                snake_length += 1

            screen.fill((0, 0, 0))
            target = pygame.draw.circle(screen, (255, 255, 255), (targetCooX, targetCooY), 15)
            snakeHead = Rect(snakeHeadCooX, snakeHeadCooY, 30, 30)
            pygame.draw.rect(screen, (255, 0, 0), snakeHead)

            img = font.render('Score : ' + str(score), True, (255, 255, 255))
            i = 0
            snakeBodyReversed = list(reversed(snakeBody))
            for element in snakeBodyReversed:
                i += 1
                currentBodypart = pygame.draw.rect(screen, (255, 0, 0), [element[0], element[1], 30, 30])
                if i > 6 and pygame.Rect.colliderect(currentBodypart, snakeHead):
                    gameover = True
            pygame.draw.circle(screen, (255, 255, 0), (snakeHeadCooX + 7, snakeHeadCooY + 15), 5)
            pygame.draw.circle(screen, (255, 255, 0), (snakeHeadCooX + 22, snakeHeadCooY + 15), 5)

            screen.blit(img, (20, 20))

    clock.tick(60)
    pygame.display.flip()
