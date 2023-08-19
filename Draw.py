import random

import pygame
import math
pygame.font.init()
from animation import animation



# art #
player = pygame.transform.scale(pygame.image.load("art/tile002.png"), (35, 70))
player_flippedX = pygame.transform.flip(player, True, False)
player_flippedY = pygame.transform.flip(player, False, True)
player_flippedYX = pygame.transform.flip(player, True, True)
player1 = pygame.transform.scale(pygame.image.load("art/tile003.png"), (35, 70))
player2 = pygame.transform.scale(pygame.image.load("art/tile004.png"), (35, 70))
player3 = pygame.transform.scale(pygame.image.load("art/tile005.png"), (35, 70))
player4 = pygame.transform.scale(pygame.image.load("art/tile006.png"), (35, 70))

background = pygame.transform.scale(pygame.image.load("art/tile019.png"), (40, 40))
grassUp = pygame.transform.scale(pygame.image.load("art/tile016.png"), (40, 40))
grassDown = pygame.transform.flip(grassUp, False, True)
dirt = pygame.transform.scale(pygame.image.load("art/tile024.png"), (40, 40))
spikedown = pygame.transform.scale(pygame.image.load("art/tile020.png"), (40, 40))
spikeup = pygame.transform.flip(spikedown, False, True)

coin = pygame.transform.scale(pygame.image.load("art/coin/tile000.png"), (35, 35))
coin1 = pygame.transform.scale(pygame.image.load("art/coin/tile001.png"), (35, 35))
coin2 = pygame.transform.scale(pygame.image.load("art/coin/tile002.png"), (35, 35))
coin3 = pygame.transform.scale(pygame.image.load("art/coin/tile003.png"), (35, 35))
###


def draw(flip, WIDTH, HEIGHT, WIN, level, jumpsLeft, frame, player_xy, playerFlipX, dead):
    FONT = pygame.font.SysFont("", 30)
    FONT1 = pygame.font.SysFont("", 100)

    WIN.fill('white')

    # background #
    for x in range(math.ceil(WIDTH / 40)):
        for y in range(math.ceil(HEIGHT / 40)):
            WIN.blit(background, (x * 40, y * 40))
    ###

    # level #
    for x in range(30):
        for y in range (15):
            if level[y][x] == 1:
                WIN.blit(grassUp, (x * 40, y * 40))
            elif level[y][x] == 2:
                WIN.blit(dirt, (x * 40, y * 40))
            elif level[y][x] == 3:
                WIN.blit(spikeup, (x * 40, y * 40))
            elif level[y][x] == 4:
                WIN.blit(spikedown, (x * 40, y * 40))
            elif level[y][x] == 5:
                WIN.blit(grassDown, (x * 40, y * 40))


    # text #
    if dead:
        hi_text = FONT1.render("You Die", True, "white")
        WIN.blit(hi_text, (WIDTH/2 - 100, HEIGHT/2))
    if flip:
        hi_text = FONT.render("Tails", True, "white")
        WIN.blit(hi_text, (WIDTH - 60, 45))
    else:
        hi_text = FONT.render("Heads", True, "white")
        WIN.blit(hi_text, (WIDTH - 70, 45))
    ###

    # misc #
    if not jumpsLeft > 0:
        if frame < 8: #<- this animation has 4 frames, so I play it 2 times
            frame = animation(WIN, [coin, coin1, coin2, coin3], (WIDTH - 55, 0), 100, False)
        else:
            animation(WIN, [coin, coin1, coin2, coin3], (WIDTH - 55, 0), 100, True)
            WIN.blit(coin, (WIDTH - 55, 0))
    else:
        frame = 0
        WIN.blit(coin, (WIDTH - 55, 0))
    ###

    # player #
    if not playerFlipX:
        if flip:
            WIN.blit(player_flippedY, (player_xy[0], player_xy[1]))
        else:
            WIN.blit(player, (player_xy[0], player_xy[1]))
    else:
        if flip:
            WIN.blit(player_flippedYX, (player_xy[0], player_xy[1]))
        else:
            WIN.blit(player_flippedX, (player_xy[0], player_xy[1]))
    ###

    pygame.display.update()