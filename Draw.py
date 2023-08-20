import button
import pygame
import math
from main import resetscore
pygame.font.init()
from animation import animation

dead = False
t = False

# art #
player = pygame.transform.scale(pygame.image.load("art/player/tile002.png"), (35, 70))
player_flippedX = pygame.transform.flip(player, True, False)
player_flippedY = pygame.transform.flip(player, False, True)
player_flippedYX = pygame.transform.flip(player, True, True)


background = pygame.transform.scale(pygame.image.load("art/tiles/tile019.png"), (40, 40))
grassUp = pygame.transform.scale(pygame.image.load("art/tiles/tile016.png"), (40, 40))
grassDown = pygame.transform.flip(grassUp, False, True)
dirt = pygame.transform.scale(pygame.image.load("art/tiles/tile024.png"), (40, 40))
spikedown = pygame.transform.scale(pygame.image.load("art/tiles/spike.png"), (40, 40))
spikeup = pygame.transform.flip(spikedown, False, True)

coin = pygame.transform.scale(pygame.image.load("art/coin/tile000.png"), (35, 35))
coin1 = pygame.transform.scale(pygame.image.load("art/coin/tile001.png"), (35, 35))
coin2 = pygame.transform.scale(pygame.image.load("art/coin/tile002.png"), (35, 35))
coin3 = pygame.transform.scale(pygame.image.load("art/coin/tile003.png"), (35, 35))

buttonS = pygame.transform.scale(pygame.image.load("art/Sprite-0003.png"), (160, 80))
###


def draw(flip, WIDTH, HEIGHT, WIN, level, jumpsLeft, frame, player_xy, playerFlipX, score):
    global dead, t, found
    FONT = pygame.font.SysFont("", 30)
    FONT1 = pygame.font.SysFont("", 100)
    FONT2 = pygame.font.SysFont("", 50)

    WIN.fill('white')

    # background #
    for x in range(30):
        for y in range(15):
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

    # death stuff #
    if dead:
        player_xy = [0, 450]
        keys = pygame.key.get_pressed()
        youdied_text = FONT1.render("You Die", True, "white")
        WIN.blit(youdied_text, (WIDTH/2 - 100, HEIGHT/2 - 100))
        button.draw_button(WIN, WIDTH/2 - 160/3, HEIGHT/2, buttonS)
        reset_text = FONT2.render("Reset", True, "black")
        WIN.blit(reset_text, (WIDTH / 2 - 50 / 3 , HEIGHT / 2 + 25))
        score_text = FONT2.render("Score: " + str(score), True, "white")
        WIN.blit(score_text, (WIDTH / 2 - 100 / 3, HEIGHT / 2 - 35))
        if button.is_button_clicked(WIDTH/2 - 160/3, HEIGHT/2, buttonS):
            t = True
            dead = False
    else:
        score_text = FONT.render("Score: " + str(score), True, "white")
        WIN.blit(score_text, (0,0))
    ###

    # text #
    if flip:
        hi_text = FONT.render("Tails", True, "white")
        WIN.blit(hi_text, (WIDTH - 60, 0))
    else:
        hi_text = FONT.render("Heads", True, "white")
        WIN.blit(hi_text, (WIDTH - 70, 0))
    ###

    # misc #
    if not jumpsLeft > 0:
        if frame < 8: #<- this animation has 4 frames, so I play it 2 times
            frame = animation(WIN, [coin, coin1, coin2, coin3], (player_xy[0], player_xy[1] - (-55 if flip else 20)), 100, False)
        else:
            animation(WIN, [coin, coin1, coin2, coin3], (player_xy[0], player_xy[1] - (40 if flip else 40), 100, True))
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

