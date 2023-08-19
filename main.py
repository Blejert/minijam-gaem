import pygame
import math
pygame.font.init()
from animation import animation


def draw(flip, WIDTH, HEIGHT, WIN, level, jumpsLeft, frame, player_xy, playerFlipX):
    FONT = pygame.font.SysFont("", 30)

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
                WIN.blit(grass, (x * 40, y * 40))
            elif level[y][x] == 2:
                WIN.blit(dirt, (x * 40, y * 40))

    # text #
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
