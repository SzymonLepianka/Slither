import pygame
import time
import random
import cmath
import math
import sys
import os

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (34, 177, 76)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
light_green = (0, 255, 0)
n = 1

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

icon = pygame.image.load('icon.ico')
pygame.display.set_icon(icon)
slither = pygame.image.load('tytul3.png')
background = pygame.image.load('background2_rgb.png')
gameover = pygame.image.load('gameoverr2.png')

glowa = pygame.image.load('head_proba2.png')
body = pygame.image.load('tulow.png')
skret = pygame.image.load('skrett.png')
ogon = pygame.image.load('ogonn.png')
glowa2 = pygame.image.load('head_proba22.png')
body2 = pygame.image.load('tulow2.png')
skret2 = pygame.image.load('skrett2.png')
ogon2 = pygame.image.load('ogonn2.png')

appleimg = pygame.image.load('jabko30.png')

play_b_a = pygame.image.load('play_a_rgb.png')
play_b_ia = pygame.image.load('play_ia_rgb.png')
modes_b_a = pygame.image.load('modes_a_rgb.png')
modes_b_ia = pygame.image.load('modes_ia_rgb.png')
quit_b_a = pygame.image.load('quit_a_rgb.png')
quit_b_ia = pygame.image.load('quit_ia_rgb.png')
walls_b_a = pygame.image.load('walls_a_rgb.png')
walls_b_ia = pygame.image.load('walls_ia_rgb.png')
nowalls_b_a = pygame.image.load('nowallls_a_rgb.png')
nowalls_b_ia = pygame.image.load('nowallls_ia_rgb.png')
pvp_b_a = pygame.image.load('pvp_a_rgb.png')
pvp_b_ia = pygame.image.load('pvp_ia_rgb.png')
pvai_b_a = pygame.image.load('pvai_a_rgb.png')
pvai_b_ia = pygame.image.load('pvai_ia_rgb.png')
again_b_a = pygame.image.load('again_a_rgb.png')
again_b_ia = pygame.image.load('again_ia_rgb.png')
resume_b_a = pygame.image.load('resume_a_rgb.png')
resume_b_ia = pygame.image.load('resume_ia_rgb.png')

syk = pygame.mixer.Sound("syk.wav")
crash = pygame.mixer.Sound("crash.wav")

highscore1_file = "high_score1.txt"
highscore2_file = "high_score2.txt"

with open(highscore1_file, 'r') as f1:
    try:
        highscore1 = int(f1.read())
    except:
        highscore1 = 0
    f1.close()
with open(highscore2_file, 'r') as f2:
    try:
        highscore2 = int(f2.read())
    except:
        highscore2 = 0
    f2.close()

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 10

direction1 = "right"
direction2 = "left"

tinyfont = pygame.font.SysFont("comicsansms", 15)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 65)

paused = True


def pause():
    global paused
    paused = True
    message_to_screen("Paused", black, -100, size="large")
    # message_to_screen("Press C to continue or Q to quit", black, 25)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        button("resume", 120, 350, 200, 125, yellow, light_yellow, action="resume")
        button("quit", 480, 350, 200, 125, red, light_red, action="quit")
        pygame.display.update()

        clock.tick(15)
    gameDisplay.fill(white)


def score(score, n, tryb):
    if n == 1:
        text = smallfont.render("Score: " + str(score), True, black)
        if tryb == 1:
            gameDisplay.blit(text, [25, 25])
        else:
            gameDisplay.blit(text, [0, 0])
    elif n == 2:
        text = smallfont.render("Score: " + str(score), True, black)
        gameDisplay.blit(text, [680, 0])


def randAppleGen():
    randAppleX = round(random.randrange(block_size, display_width - AppleThickness - block_size))
    randAppleY = round(random.randrange(block_size, display_height - AppleThickness - block_size))
    return randAppleX, randAppleY


randAppleX, randAppleY = randAppleGen()


def game_intro_walls():
    intro = True
    gameDisplay.fill(white)
    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(slither, (0, 50))
    message_to_screen("The objective of the game is to eat red apples", black, -30)
    message_to_screen("The more apples you eat the longer you get", black, 10)
    message_to_screen("If you run into yourself or the edges you die", black, 50)
    message_to_screen("HIGH SCORE: " + str(highscore1), black, 100)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        button("play", 50, 425, 200, 125, green, light_green, action="play")
        button("modes", 300, 425, 200, 125, yellow, light_yellow, action="modes")
        button("quit", 550, 425, 200, 125, red, light_red, action="quit")

        pygame.display.update()
        clock.tick(15)


def game_intro_nowalls():
    intro = True
    while intro:
        gameDisplay.fill(white)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(slither, (0, 50))
        # message_to_screen("The objective of the game is to eat red apples", black, -30)
        message_to_screen("The more apples you eat the longer you get", black, -30)
        message_to_screen("If you run into yourself you die", black, 10)
        message_to_screen("You can go through the edges", black, 50)
        message_to_screen("HIGH SCORE: " + str(highscore2), black, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        button("play", 50, 425, 200, 125, green, light_green, action="play")
        button("modes", 300, 425, 200, 125, yellow, light_yellow, action="modes")
        button("quit", 550, 425, 200, 125, red, light_red, action="quit")
        # button("play", 150, 500, 100, 50, green,light_green, action="play")
        # button("modes", 350, 500, 100, 50, yellow,light_yellow, action="modes")
        # button("quit", 550, 500, 100, 50, red,light_red, action="quit")

        pygame.display.update()
        clock.tick(15)


def game_intro_pvp():
    intro = True
    while intro:
        gameDisplay.fill(white)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(slither, (0, 50))
        message_to_screen("The more apples you eat the longer you get", black, -30)
        message_to_screen("If you run into yourself or your opponent, you die", black, 50)
        message_to_screen("Try to reach 10 points to win", black, 90)
        message_to_screen("You can go through the edges", black, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        button("play", 50, 425, 200, 125, green, light_green, action="play")
        button("modes", 300, 425, 200, 125, yellow, light_yellow, action="modes")
        button("quit", 550, 425, 200, 125, red, light_red, action="quit")
        # button("play", 150, 500, 100, 50, green,light_green, action="play")
        # button("modes", 350, 500, 100, 50, yellow,light_yellow, action="modes")
        # button("quit", 550, 500, 100, 50, red,light_red, action="quit")

        pygame.display.update()
        clock.tick(15)


def game_intro_pvai():
    intro = True
    while intro:
        gameDisplay.fill(white)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(slither, (0, 50))
        message_to_screen("The more apples you eat the longer you get", black, -30)
        message_to_screen("If you run into yourself or your opponent, you die", black, 50)
        message_to_screen("Try to reach 10 points to win", black, 90)
        message_to_screen("You can go through the edges", black, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        button("play", 50, 425, 200, 125, green, light_green, action="play")
        button("modes", 300, 425, 200, 125, yellow, light_yellow, action="modes")
        button("quit", 550, 425, 200, 125, red, light_red, action="quit")
        # button("play (pvai)", 150, 500, 100, 50, green,light_green, action="play")
        # button("modes", 350, 500, 100, 50, yellow,light_yellow, action="modes")
        # button("quit", 550, 500, 100, 50, red,light_red, action="quit")

        pygame.display.update()
        clock.tick(15)


def modes():
    intro = True
    while intro:
        gameDisplay.fill(white)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(slither, (0, 25))
        message_to_screen("Choose your mode:", black, -60, "medium")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        button("walls", 100, 285, 200, 125, yellow, light_yellow, action="walls")
        button("no walls", 100, 450, 200, 125, yellow, light_yellow, action="no_walls")
        button("PvP", 500, 285, 200, 125, yellow, light_yellow, action="pvp")
        button("PvAI", 500, 450, 200, 125, yellow, light_yellow, action="pvai")
        # button("quit", 350, 100, 200, 125, red, light_red, action="quit")

        pygame.display.update()
        clock.tick(15)


def snake1(block_size, snake1list):
    if direction1 == "right":
        head = pygame.transform.rotate(glowa, 270)
    elif direction1 == "left":
        head = pygame.transform.rotate(glowa, 90)
    elif direction1 == "up":
        head = glowa
    elif direction1 == "down":
        head = pygame.transform.rotate(glowa, 180)

    if snake1list[-len(snake1list)][0] == snake1list[-len(snake1list) + 1][0] and snake1list[-len(snake1list)][1] < \
            snake1list[-len(snake1list) + 1][1]:
        ogonn = pygame.transform.rotate(ogon, 180)
    elif snake1list[-len(snake1list)][0] == snake1list[-len(snake1list) + 1][0] and snake1list[-len(snake1list)][1] > \
            snake1list[-len(snake1list) + 1][1]:
        ogonn = ogon
    elif snake1list[-len(snake1list)][0] < snake1list[-len(snake1list) + 1][0] and snake1list[-len(snake1list)][1] == \
            snake1list[-len(snake1list) + 1][1]:
        ogonn = pygame.transform.rotate(ogon, 270)
    elif snake1list[-len(snake1list)][0] > snake1list[-len(snake1list) + 1][0] and snake1list[-len(snake1list)][1] == \
            snake1list[-len(snake1list) + 1][1]:
        ogonn = pygame.transform.rotate(ogon, 90)
    if (snake1list[-len(snake1list) + 1][0] == 0 and snake1list[-len(snake1list)][0] == display_width - block_size) or (
            snake1list[-len(snake1list) + 1][1] == 0 and snake1list[-len(snake1list)][
        1] == display_height - block_size) or (
            snake1list[-len(snake1list) + 1][0] == display_width - block_size and snake1list[-len(snake1list)][
        0] == 0) or (
            snake1list[-len(snake1list) + 1][1] == display_height - block_size and snake1list[-len(snake1list)][
        1] == 0):
        ogonn = pygame.transform.rotate(ogonn, 180)

    for i in range(1, len(snake1list) + 1):
        if i == 1:
            gameDisplay.blit(head, (snake1list[-i][0], snake1list[-i][1]))
        elif i == len(snake1list):
            gameDisplay.blit(ogonn, (snake1list[-i][0], snake1list[-i][1]))
        elif snake1list[-i - 1][0] == snake1list[-i][0] == snake1list[-i + 1][0]:
            gameDisplay.blit(body, (snake1list[-i][0], snake1list[-i][1]))
        elif snake1list[-i - 1][1] == snake1list[-i][1] == snake1list[-i + 1][1]:
            gameDisplay.blit(pygame.transform.rotate(body, 90), (snake1list[-i][0], snake1list[-i][1]))
        else:
            if snake1list[-i][0] < snake1list[-i + 1][0] and snake1list[-i][1] == snake1list[-i + 1][1] and \
                    snake1list[-i][0] == snake1list[-i - 1][0] and snake1list[-i][1] < snake1list[-i - 1][1]:
                skret_rotated = pygame.transform.rotate(skret, 90)
            elif snake1list[-i][0] == snake1list[-i + 1][0] and snake1list[-i][1] < snake1list[-i + 1][1] and \
                    snake1list[-i][0] < snake1list[-i - 1][0] and snake1list[-i][1] == snake1list[-i - 1][1]:
                skret_rotated = pygame.transform.rotate(skret, 90)
            elif snake1list[-i][0] == snake1list[-i + 1][0] and snake1list[-i][1] > snake1list[-i + 1][1] and \
                    snake1list[-i][0] < snake1list[-i - 1][0] and snake1list[-i][1] == snake1list[-i - 1][1]:
                skret_rotated = pygame.transform.rotate(skret, 180)
            elif snake1list[-i][0] < snake1list[-i + 1][0] and snake1list[-i][1] == snake1list[-i + 1][1] and \
                    snake1list[-i][0] == snake1list[-i - 1][0] and snake1list[-i][1] > snake1list[-i - 1][1]:
                skret_rotated = pygame.transform.rotate(skret, 180)
            elif snake1list[-i][0] == snake1list[-i + 1][0] and snake1list[-i][1] < snake1list[-i + 1][1] and \
                    snake1list[-i][0] > snake1list[-i - 1][0] and snake1list[-i][1] == snake1list[-i - 1][1]:
                skret_rotated = skret
            elif snake1list[-i][0] > snake1list[-i + 1][0] and snake1list[-i][1] == snake1list[-i + 1][1] and \
                    snake1list[-i][0] == snake1list[-i - 1][0] and snake1list[-i][1] < snake1list[-i - 1][1]:
                skret_rotated = skret
            elif snake1list[-i][0] == snake1list[-i + 1][0] and snake1list[-i][1] > snake1list[-i + 1][1] and \
                    snake1list[-i][0] > snake1list[-i - 1][0] and snake1list[-i][1] == snake1list[-i - 1][1]:
                skret_rotated = pygame.transform.rotate(skret, 270)
            elif snake1list[-i][0] > snake1list[-i + 1][0] and snake1list[-i][1] == snake1list[-i + 1][1] and \
                    snake1list[-i][0] == snake1list[-i - 1][0] and snake1list[-i][1] > snake1list[-i - 1][1]:
                skret_rotated = pygame.transform.rotate(skret, 270)
            if (snake1list[-i][0] == 0 and snake1list[-i + 1][1] > snake1list[-i][1] and snake1list[-i - 1][
                0] == display_width - block_size) or (
                    snake1list[-i][0] == display_width - block_size and snake1list[-i - 1][1] < snake1list[-i][1] and
                    snake1list[-i + 1][0] == 0) or (
                    snake1list[-i][1] == 0 and snake1list[-i + 1][0] < snake1list[-i][0] and snake1list[-i - 1][
                1] == display_height - block_size) or (
                    snake1list[-i][1] == display_height - block_size and snake1list[-i - 1][0] > snake1list[-i][0] and
                    snake1list[-i + 1][1] == 0) or (
                    snake1list[-i][0] == display_width - block_size and snake1list[-i + 1][1] < snake1list[-i][1] and
                    snake1list[-i - 1][0] == 0) or (
                    snake1list[-i][0] == 0 and snake1list[-i - 1][1] > snake1list[-i][1] and snake1list[-i + 1][
                0] == display_width - block_size) or (
                    snake1list[-i][1] == display_height - block_size and snake1list[-i + 1][0] > snake1list[-i][0] and
                    snake1list[-i - 1][1] == 0) or (
                    snake1list[-i][1] == 0 and snake1list[-i - 1][0] < snake1list[-i][0] and snake1list[-i + 1][
                1] == display_height - block_size):
                skret_rotated = pygame.transform.rotate(skret_rotated, 270)
            elif (snake1list[-i][0] == 0 and snake1list[-i + 1][1] < snake1list[-i][1] and snake1list[-i - 1][
                0] == display_width - block_size) or (
                    snake1list[-i][0] == display_width - block_size and snake1list[-i - 1][1] > snake1list[-i][1] and
                    snake1list[-i + 1][0] == 0) or (
                    snake1list[-i][1] == 0 and snake1list[-i + 1][0] > snake1list[-i][0] and snake1list[-i - 1][
                1] == display_height - block_size) or (
                    snake1list[-i][1] == display_height - block_size and snake1list[-i - 1][0] < snake1list[-i][0] and
                    snake1list[-i + 1][1] == 0) or (
                    snake1list[-i][0] == display_width - block_size and snake1list[-i + 1][1] > snake1list[-i][1] and
                    snake1list[-i - 1][0] == 0) or (
                    snake1list[-i][0] == 0 and snake1list[-i - 1][1] < snake1list[-i][1] and snake1list[-i + 1][
                0] == display_width - block_size) or (
                    snake1list[-i][1] == display_height - block_size and snake1list[-i + 1][0] < snake1list[-i][0] and
                    snake1list[-i - 1][1] == 0) or (
                    snake1list[-i][1] == 0 and snake1list[-i - 1][0] > snake1list[-i][0] and snake1list[-i + 1][
                1] == display_height - block_size):
                skret_rotated = pygame.transform.rotate(skret_rotated, 90)
            gameDisplay.blit(skret_rotated, (snake1list[-i][0], snake1list[-i][1]))


def snake2(block_size, snake2list):
    if direction2 == "right":
        head = pygame.transform.rotate(glowa2, 270)
    elif direction2 == "left":
        head = pygame.transform.rotate(glowa2, 90)
    elif direction2 == "up":
        head = glowa2
    elif direction2 == "down":
        head = pygame.transform.rotate(glowa2, 180)

    if snake2list[-len(snake2list)][0] == snake2list[-len(snake2list) + 1][0] and snake2list[-len(snake2list)][1] < \
            snake2list[-len(snake2list) + 1][1]:
        ogonn2 = pygame.transform.rotate(ogon2, 180)
    elif snake2list[-len(snake2list)][0] == snake2list[-len(snake2list) + 1][0] and snake2list[-len(snake2list)][1] > \
            snake2list[-len(snake2list) + 1][1]:
        ogonn2 = ogon2
    elif snake2list[-len(snake2list)][0] < snake2list[-len(snake2list) + 1][0] and snake2list[-len(snake2list)][1] == \
            snake2list[-len(snake2list) + 1][1]:
        ogonn2 = pygame.transform.rotate(ogon2, 270)
    elif snake2list[-len(snake2list)][0] > snake2list[-len(snake2list) + 1][0] and snake2list[-len(snake2list)][1] == \
            snake2list[-len(snake2list) + 1][1]:
        ogonn2 = pygame.transform.rotate(ogon2, 90)
    if (snake2list[-len(snake2list) + 1][0] == 0 and snake2list[-len(snake2list)][0] == display_width - block_size) or (
            snake2list[-len(snake2list) + 1][1] == 0 and snake2list[-len(snake2list)][
        1] == display_height - block_size) or (
            snake2list[-len(snake2list) + 1][0] == display_width - block_size and snake2list[-len(snake2list)][
        0] == 0) or (
            snake2list[-len(snake2list) + 1][1] == display_height - block_size and snake2list[-len(snake2list)][
        1] == 0):
        ogonn2 = pygame.transform.rotate(ogonn2, 180)

    for i in range(1, len(snake2list) + 1):
        if i == 1:
            gameDisplay.blit(head, (snake2list[-i][0], snake2list[-i][1]))
        elif i == len(snake2list):
            gameDisplay.blit(ogonn2, (snake2list[-i][0], snake2list[-i][1]))
        elif snake2list[-i - 1][0] == snake2list[-i][0] == snake2list[-i + 1][0]:
            gameDisplay.blit(body2, (snake2list[-i][0], snake2list[-i][1]))
        elif snake2list[-i - 1][1] == snake2list[-i][1] == snake2list[-i + 1][1]:
            gameDisplay.blit(pygame.transform.rotate(body2, 90), (snake2list[-i][0], snake2list[-i][1]))
        else:
            if snake2list[-i][0] < snake2list[-i + 1][0] and snake2list[-i][1] == snake2list[-i + 1][1] and \
                    snake2list[-i][0] == snake2list[-i - 1][0] and snake2list[-i][1] < snake2list[-i - 1][1]:
                skret2_rotated = pygame.transform.rotate(skret2, 90)
            elif snake2list[-i][0] == snake2list[-i + 1][0] and snake2list[-i][1] < snake2list[-i + 1][1] and \
                    snake2list[-i][0] < snake2list[-i - 1][0] and snake2list[-i][1] == snake2list[-i - 1][1]:
                skret2_rotated = pygame.transform.rotate(skret2, 90)
            elif snake2list[-i][0] == snake2list[-i + 1][0] and snake2list[-i][1] > snake2list[-i + 1][1] and \
                    snake2list[-i][0] < snake2list[-i - 1][0] and snake2list[-i][1] == snake2list[-i - 1][1]:
                skret2_rotated = pygame.transform.rotate(skret2, 180)
            elif snake2list[-i][0] < snake2list[-i + 1][0] and snake2list[-i][1] == snake2list[-i + 1][1] and \
                    snake2list[-i][0] == snake2list[-i - 1][0] and snake2list[-i][1] > snake2list[-i - 1][1]:
                skret2_rotated = pygame.transform.rotate(skret2, 180)
            elif snake2list[-i][0] == snake2list[-i + 1][0] and snake2list[-i][1] < snake2list[-i + 1][1] and \
                    snake2list[-i][0] > snake2list[-i - 1][0] and snake2list[-i][1] == snake2list[-i - 1][1]:
                skret2_rotated = skret2
            elif snake2list[-i][0] > snake2list[-i + 1][0] and snake2list[-i][1] == snake2list[-i + 1][1] and \
                    snake2list[-i][0] == snake2list[-i - 1][0] and snake2list[-i][1] < snake2list[-i - 1][1]:
                skret2_rotated = skret2
            elif snake2list[-i][0] == snake2list[-i + 1][0] and snake2list[-i][1] > snake2list[-i + 1][1] and \
                    snake2list[-i][0] > snake2list[-i - 1][0] and snake2list[-i][1] == snake2list[-i - 1][1]:
                skret2_rotated = pygame.transform.rotate(skret2, 270)
            elif snake2list[-i][0] > snake2list[-i + 1][0] and snake2list[-i][1] == snake2list[-i + 1][1] and \
                    snake2list[-i][0] == snake2list[-i - 1][0] and snake2list[-i][1] > snake2list[-i - 1][1]:
                skret2_rotated = pygame.transform.rotate(skret2, 270)
            if (snake2list[-i][0] == 0 and snake2list[-i + 1][1] > snake2list[-i][1] and snake2list[-i - 1][
                0] == display_width - block_size) or (
                    snake2list[-i][0] == display_width - block_size and snake2list[-i - 1][1] < snake2list[-i][1] and
                    snake2list[-i + 1][0] == 0) or (
                    snake2list[-i][1] == 0 and snake2list[-i + 1][0] < snake2list[-i][0] and snake2list[-i - 1][
                1] == display_height - block_size) or (
                    snake2list[-i][1] == display_height - block_size and snake2list[-i - 1][0] > snake2list[-i][0] and
                    snake2list[-i + 1][1] == 0) or (
                    snake2list[-i][0] == display_width - block_size and snake2list[-i + 1][1] < snake2list[-i][1] and
                    snake2list[-i - 1][0] == 0) or (
                    snake2list[-i][0] == 0 and snake2list[-i - 1][1] > snake2list[-i][1] and snake2list[-i + 1][
                0] == display_width - block_size) or (
                    snake2list[-i][1] == display_height - block_size and snake2list[-i + 1][0] > snake2list[-i][0] and
                    snake2list[-i - 1][1] == 0) or (
                    snake2list[-i][1] == 0 and snake2list[-i - 1][0] < snake2list[-i][0] and snake2list[-i + 1][
                1] == display_height - block_size):
                skret2_rotated = pygame.transform.rotate(skret2_rotated, 270)
            elif (snake2list[-i][0] == 0 and snake2list[-i + 1][1] < snake2list[-i][1] and snake2list[-i - 1][
                0] == display_width - block_size) or (
                    snake2list[-i][0] == display_width - block_size and snake2list[-i - 1][1] > snake2list[-i][1] and
                    snake2list[-i + 1][0] == 0) or (
                    snake2list[-i][1] == 0 and snake2list[-i + 1][0] > snake2list[-i][0] and snake2list[-i - 1][
                1] == display_height - block_size) or (
                    snake2list[-i][1] == display_height - block_size and snake2list[-i - 1][0] < snake2list[-i][0] and
                    snake2list[-i + 1][1] == 0) or (
                    snake2list[-i][0] == display_width - block_size and snake2list[-i + 1][1] > snake2list[-i][1] and
                    snake2list[-i - 1][0] == 0) or (
                    snake2list[-i][0] == 0 and snake2list[-i - 1][1] < snake2list[-i][1] and snake2list[-i + 1][
                0] == display_width - block_size) or (
                    snake2list[-i][1] == display_height - block_size and snake2list[-i + 1][0] < snake2list[-i][0] and
                    snake2list[-i - 1][1] == 0) or (
                    snake2list[-i][1] == 0 and snake2list[-i - 1][0] > snake2list[-i][0] and snake2list[-i + 1][
                1] == display_height - block_size):
                skret2_rotated = pygame.transform.rotate(skret2_rotated, 90)
            gameDisplay.blit(skret2_rotated, (snake2list[-i][0], snake2list[-i][1]))


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


# def text_to_button (msg,color,buttonx,buttony,buttonwidth, buttonheight, size ="small"):
#    textSurf,textRect = text_objects(msg,color,size)
#    textRect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
#    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def button(text, x, y, width, height, inactivecolor, activecolor, action=None):
    global n
    global paused
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:

        if text == "play":
            gameDisplay.blit(play_b_a, (x, y))
        elif text == "modes":
            gameDisplay.blit(modes_b_a, (x, y))
        elif text == "quit":
            gameDisplay.blit(quit_b_a, (x, y))
        elif text == "walls":
            gameDisplay.blit(walls_b_a, (x, y))
        elif text == "no walls":
            gameDisplay.blit(nowalls_b_a, (x, y))
        elif text == "PvP":
            gameDisplay.blit(pvp_b_a, (x, y))
        elif text == "PvAI":
            gameDisplay.blit(pvai_b_a, (x, y))
        elif text == "play again":
            gameDisplay.blit(again_b_a, (x, y))
        elif text == "resume":
            gameDisplay.blit(resume_b_a, (x, y))
        else:
            pygame.draw.rect(gameDisplay, activecolor, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "modes":
                modes()
            if action == "play":
                pygame.time.wait(100)
                gameLoop(n)
            if action == "walls":
                n = 1
                pygame.time.wait(100)
                game_intro_walls()
            if action == "no_walls":
                n = 2
                pygame.time.wait(100)
                game_intro_nowalls()
            if action == "pvp":
                n = 3
                pygame.time.wait(100)
                game_intro_pvp()
            if action == "pvai":
                n = 4
                pygame.time.wait(100)
                game_intro_pvai()
            if action == "resume":
                paused = False
    else:
        if text == "play":
            gameDisplay.blit(play_b_ia, (x, y))
        elif text == "modes":
            gameDisplay.blit(modes_b_ia, (x, y))
        elif text == "quit":
            gameDisplay.blit(quit_b_ia, (x, y))
        elif text == "walls":
            gameDisplay.blit(walls_b_ia, (x, y))
        elif text == "no walls":
            gameDisplay.blit(nowalls_b_ia, (x, y))
        elif text == "PvP":
            gameDisplay.blit(pvp_b_ia, (x, y))
        elif text == "PvAI":
            gameDisplay.blit(pvai_b_ia, (x, y))
        elif text == "play again":
            gameDisplay.blit(again_b_ia, (x, y))
        elif text == "resume":
            gameDisplay.blit(resume_b_ia, (x, y))
        else:
            pygame.draw.rect(gameDisplay, inactivecolor, (x, y, width, height))
    # text_to_button(text, black, x,y,width,height)


def gameLoop(n):
    global direction1
    global direction2
    global FPS
    global highscore1
    global highscore2
    direction1 = 'right'
    direction2 = 'left'

    gameExit = False
    gameOver = False
    gameOver1 = False
    gameOver2 = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 20
    lead_y_change = 0
    if n == 3 or n == 4:
        lead_x2 = display_width / 2 + block_size
        lead_y2 = display_height / 2
        lead_x2_change = -20
        lead_y2_change = 0

    snakelist = []
    snakeLength = 2
    if n == 3 or n == 4:
        snake2list = []
        snake2Length = 2

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:
        if n == 3 or n == 4:
            # gameDisplay.blit(gameover, (0, 0))
            if gameOver1 == True and gameOver2 == True:
                gameDisplay.blit(gameover, (0, 0))
                message_to_screen("DRAW!", black, 0, size="large")
            elif gameOver1 == True:
                gameDisplay.blit(gameover, (0, 0))
                message_to_screen("PLAYER 1 HAS WON!", black, 0, size="large")
            elif gameOver2 == True:
                gameDisplay.blit(gameover, (0, 0))
                message_to_screen("PLAYER 2 HAS WON!", black, 0, size="large")
            while gameOver1 == True or gameOver2 == True:
                if n == 3:
                    tof = "pvp"
                else:
                    tof = "pvai"

                if gameOver1 == True and gameOver2 == True:
                    button("play again", 110, 380, 200, 125, yellow, light_yellow, action=tof)
                    button("quit", 490, 380, 200, 125, red, light_red, action="quit")
                    pygame.display.update()
                elif gameOver1 == True:
                    button("play again", 110, 380, 200, 125, yellow, light_yellow, action=tof)
                    button("quit", 490, 380, 200, 125, red, light_red, action="quit")
                    pygame.display.update()
                elif gameOver2 == True:
                    button("play again", 110, 380, 200, 125, yellow, light_yellow, action=tof)
                    button("quit", 490, 380, 200, 125, red, light_red, action="quit")
                    pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver1 = False
                        gameOver2 = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver1 = False
                            gameOver2 = False
                        if event.key == pygame.K_c:
                            game_intro_walls()
        if n == 1 or n == 2:
            if gameOver == True:
                # message_to_screen("Game over,", red, -50, size="large")
                gameDisplay.blit(gameover, (0, 0))
                if n == 1:
                    if snakeLength - 2 > highscore1:
                        highscore1 = snakeLength - 2
                        message_to_screen("You beat high score!!!", black, 30, "medium")
                        with open(highscore1_file, 'w') as f1:
                            f1.write(str(highscore1))
                    else:
                        message_to_screen("HIGH SCORE: " + str(highscore1), black, 30, "medium")
                else:
                    if snakeLength - 2 > highscore2:
                        highscore2 = snakeLength - 2
                        message_to_screen("You beat high score!!!", black, 30, "medium")
                        with open(highscore2_file, 'w') as f2:
                            f2.write(str(highscore2))
                    else:
                        message_to_screen("HIGH SCORE: " + str(highscore2), black, 30, "medium")

            while gameOver == True:
                if n == 1:
                    ort = "walls"
                elif n == 2:
                    ort = "no_walls"
                    # print("x")
                if gameOver == True:
                    # message_to_screen("Game over,", red, -50, size="large")
                    button("play again", 110, 380, 200, 125, yellow, light_yellow, action=ort)
                    button("quit", 490, 380, 200, 125, red, light_red, action="quit")
                    pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            # gameLoop()
                            if n == 1:
                                game_intro_walls()
                            if n == 2:
                                game_intro_nowalls()
                            if n == 3:
                                game_intro_pvp()
                            if n == 4:
                                game_intro_pvai()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction1 = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction1 = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction1 = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction1 = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
                if n == 3:
                    if event.key == pygame.K_w:
                        direction2 = "up"
                        lead_y2_change = -block_size
                        lead_x2_change = 0
                    elif event.key == pygame.K_s:
                        direction2 = "down"
                        lead_y2_change = block_size
                        lead_x2_change = 0
                    elif event.key == pygame.K_d:
                        direction2 = "right"
                        lead_x2_change = block_size
                        lead_y2_change = 0
                    elif event.key == pygame.K_a:
                        direction2 = "left"
                        lead_x2_change = -block_size
                        lead_y2_change = 0

        if n == 4:
            if math.fabs(lead_x2 - randAppleX) > display_width / 2:
                if math.fabs(lead_y2 - randAppleY) > display_height / 2:
                    if lead_x2 > randAppleX and direction2 != "left" and display_width - math.fabs(
                            lead_x2 - randAppleX) > display_height - math.fabs(lead_y2 - randAppleY):
                        lead_x2_change = block_size
                        lead_y2_change = 0
                        direction2 = "right"
                    elif lead_x2 <= randAppleX and direction2 != "right" and display_width - math.fabs(
                            lead_x2 - randAppleX) > display_height - math.fabs(lead_y2 - randAppleY):
                        lead_x2_change = -block_size
                        lead_y2_change = 0
                        direction2 = "left"
                    elif lead_y2 > randAppleY and direction2 != "up" and display_width - math.fabs(
                            lead_x2 - randAppleX) < display_height - math.fabs(lead_y2 - randAppleY):
                        lead_y2_change = block_size
                        lead_x2_change = 0
                        direction2 = "down"
                    elif lead_y2 <= randAppleY and direction2 != "down" and display_width - math.fabs(
                            lead_x2 - randAppleX) < display_height - math.fabs(lead_y2 - randAppleY):
                        lead_y2_change = -block_size
                        lead_x2_change = 0
                        direction2 = "up"
                else:
                    if lead_x2 > randAppleX and direction2 != "left" and display_width - math.fabs(
                            lead_x2 - randAppleX) > math.fabs(lead_y2 - randAppleY):
                        lead_x2_change = block_size
                        lead_y2_change = 0
                        direction2 = "right"
                    elif lead_x2 < randAppleX and direction2 != "right" and display_width - math.fabs(
                            lead_x2 - randAppleX) > math.fabs(lead_y2 - randAppleY):
                        lead_x2_change = -block_size
                        lead_y2_change = 0
                        direction2 = "left"
                    elif lead_y2 > randAppleY and direction2 != "down" and display_width - math.fabs(
                            lead_x2 - randAppleX) < math.fabs(lead_y2 - randAppleY):
                        lead_y2_change = -block_size
                        lead_x2_change = 0
                        direction2 = "up"
                    elif lead_y2 < randAppleY and direction2 != "up" and display_width - math.fabs(
                            lead_x2 - randAppleX) < math.fabs(lead_y2 - randAppleY):
                        lead_y2_change = block_size
                        lead_x2_change = 0
                        direction2 = "down"
            else:
                if math.fabs(lead_y2 - randAppleY) > display_height / 2:
                    if lead_x2 > randAppleX and direction2 != "right" and math.fabs(
                            lead_x2 - randAppleX) > display_height - math.fabs(lead_y2 - randAppleY):
                        lead_x2_change = -block_size
                        lead_y2_change = 0
                        direction2 = "left"
                    elif lead_x2 < randAppleX and direction2 != "left" and math.fabs(
                            lead_x2 - randAppleX) > display_height - math.fabs(lead_y2 - randAppleY):
                        lead_x2_change = block_size
                        lead_y2_change = 0
                        direction2 = "right"
                    elif lead_y2 > randAppleY and direction2 != "up" and math.fabs(
                            lead_x2 - randAppleX) < display_height - math.fabs(lead_y2 - randAppleY):
                        lead_y2_change = block_size
                        lead_x2_change = 0
                        direction2 = "down"
                    elif lead_y2 < randAppleY and direction2 != "down" and math.fabs(
                            lead_x2 - randAppleX) < display_height - math.fabs(lead_y2 - randAppleY):
                        lead_y2_change = -block_size
                        lead_x2_change = 0
                        direction2 = "up"
                else:
                    if lead_x2 > randAppleX and direction2 != "right" and math.fabs(lead_x2 - randAppleX) > math.fabs(
                            lead_y2 - randAppleY):
                        lead_x2_change = -block_size
                        lead_y2_change = 0
                        direction2 = "left"
                    elif lead_x2 < randAppleX and direction2 != "left" and math.fabs(lead_x2 - randAppleX) > math.fabs(
                            lead_y2 - randAppleY):
                        lead_x2_change = block_size
                        lead_y2_change = 0
                        direction2 = "right"
                    elif lead_y2 > randAppleY and direction2 != "down" and math.fabs(lead_x2 - randAppleX) < math.fabs(
                            lead_y2 - randAppleY):
                        lead_y2_change = -block_size
                        lead_x2_change = 0
                        direction2 = "up"
                    elif lead_y2 < randAppleY and direction2 != "up" and math.fabs(lead_x2 - randAppleX) < math.fabs(
                            lead_y2 - randAppleY):
                        lead_y2_change = block_size
                        lead_x2_change = 0
                        direction2 = "down"
            for eachSegment in snake2list[:-1]:
                if eachSegment[0] == snake2Head[0] + lead_x2_change and eachSegment[1] == snake2Head[
                    1] + lead_y2_change:
                    if lead_x2_change != 0:
                        if direction2 == "right":
                            direction2 = "down"
                        else:
                            direction2 = "up"
                        lead_y2_change = lead_x2_change
                        lead_x2_change = 0
                    else:
                        if direction2 == "down":
                            direction2 = "right"
                        else:
                            direction2 = "left"
                        lead_x2_change = lead_y2_change
                        lead_y2_change = 0
                    for eachSegment in snake2list[:-1]:
                        if eachSegment[0] == snake2Head[0] + lead_x2_change and eachSegment[1] == snake2Head[
                            1] + lead_y2_change:
                            if lead_x2_change == 0:
                                if direction2 == "down":
                                    direction2 = "up"
                                else:
                                    direction2 = "down"
                                lead_y2_change = -lead_y2_change
                            else:
                                if direction2 == "right":
                                    direction2 = "left"
                                else:
                                    direction2 = "right"
                                lead_x2_change = -lead_x2_change
            for eachSegment in snakelist:
                if eachSegment[0] == snake2Head[0] + lead_x2_change and eachSegment[1] == snake2Head[
                    1] + lead_y2_change:
                    if lead_x2_change != 0:
                        if direction2 == "right":
                            direction2 = "down"
                        else:
                            direction2 = "up"
                        lead_y2_change = lead_x2_change
                        lead_x2_change = 0
                    else:
                        if direction2 == "down":
                            direction2 = "right"
                        else:
                            direction2 = "left"
                        lead_x2_change = lead_y2_change
                        lead_y2_change = 0
                    for eachSegment in snake2list[:-1]:
                        if eachSegment[0] == snake2Head[0] + lead_x2_change and eachSegment[1] == snake2Head[
                            1] + lead_y2_change:
                            if lead_x2_change == 0:
                                if direction2 == "down":
                                    direction2 = "up"
                                else:
                                    direction2 = "down"
                                lead_y2_change = -lead_y2_change
                            else:
                                if direction2 == "right":
                                    direction2 = "left"
                                else:
                                    direction2 = "right"
                                lead_x2_change = -lead_x2_change

        lead_x += lead_x_change
        lead_y += lead_y_change
        if n == 3 or n == 4:
            lead_x2 += lead_x2_change
            lead_y2 += lead_y2_change

        if n == 1:
            if lead_x > display_width - 2 * block_size or lead_x < block_size or lead_y > display_height - 2 * block_size or lead_y < block_size:
                gameOver = True
                pygame.mixer.Sound.play(crash)
                FPS = 10
        else:
            if lead_x > display_width - block_size:
                lead_x = 0
            if lead_x < 0:
                lead_x = display_width - block_size
            if lead_y > display_height - block_size:
                lead_y = 0
            if lead_y < 0:
                lead_y = display_height - block_size
        if n == 3 or n == 4:
            if lead_x2 > display_width - block_size:
                lead_x2 = 0
            if lead_x2 < 0:
                lead_x2 = display_width - block_size
            if lead_y2 > display_height - block_size:
                lead_y2 = 0
            if lead_y2 < 0:
                lead_y2 = display_height - block_size

        gameDisplay.fill(white)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)
        if n == 3 or n == 4:
            snake2Head = []
            snake2Head.append(lead_x2)
            snake2Head.append(lead_y2)
            snake2list.append(snake2Head)
            if len(snake2list) > snake2Length:
                del snake2list[0]
            for eachSegment in snake2list[:-1]:
                if eachSegment == snake2Head:
                    gameOver1 = True
                    pygame.mixer.Sound.play(crash)
                    FPS = 10
            for eachSegment in snakelist[:-1]:
                if eachSegment == snake2Head:
                    FPS = 10
                    gameOver1 = True
                    pygame.mixer.Sound.play(crash)
            for eachSegment in snake2list[:-1]:
                if eachSegment == snakeHead:
                    FPS = 10
                    gameOver2 = True
                    pygame.mixer.Sound.play(crash)
        if len(snakelist) > snakeLength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            if eachSegment == snakeHead:
                gameOver2 = True
                gameOver = True
                FPS = 10
                pygame.mixer.Sound.play(crash)

        if n == 1:
            pygame.draw.rect(gameDisplay, black, [0, 0, block_size, display_height])
            pygame.draw.rect(gameDisplay, black, [block_size, 0, display_width - 2 * block_size, block_size])
            pygame.draw.rect(gameDisplay, black, [display_width - block_size, 0, block_size, display_height])
            pygame.draw.rect(gameDisplay, black,
                             [block_size, display_height - block_size, display_width - 2 * block_size, block_size])

        snake1(block_size, snakelist)
        if n == 3 or n == 4:
            snake2(block_size, snake2list)
            score(snake2Length - 2, 2, n)

        score(snakeLength - 2, 1, n)

        if n == 3 or n == 4:
            if snakeLength == 12:
                gameOver1 = True
                FPS = 10
            if snake2Length == 12:
                gameOver2 = True
                FPS = 10

        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                FPS = FPS + 1
                pygame.mixer.Sound.play(syk)
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                FPS = FPS + 1
                pygame.mixer.Sound.play(syk)
        if n == 3 or n == 4:
            if lead_x2 > randAppleX and lead_x2 < randAppleX + AppleThickness or lead_x2 + block_size > randAppleX and lead_x2 + block_size < randAppleX + AppleThickness:
                if lead_y2 > randAppleY and lead_y2 < randAppleY + AppleThickness:
                    randAppleX, randAppleY = randAppleGen()
                    snake2Length += 1
                    FPS = FPS + 1
                    pygame.mixer.Sound.play(syk)
                elif lead_y2 + block_size > randAppleY and lead_y2 + block_size < randAppleY + AppleThickness:
                    randAppleX, randAppleY = randAppleGen()
                    snake2Length += 1
                    FPS = FPS + 1
                    pygame.mixer.Sound.play(syk)

        clock.tick(FPS)
    pygame.quit()
    quit()


game_intro_walls()
gameLoop(n)
