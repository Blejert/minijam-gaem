import pygame
import random
import levels
from Draw import draw
from collisions import nextto_down, nextto_up, nextto_left, nextto_right, nexttolevel_right
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Jump")

level = levels.level1

# variables #
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 5
player_xy = [0, 450]
player_y_vel = 0
jumpsLeft = 0
flip = False
playerFlipX = False
frame = 0
dead = False
score = 0
play = False
###

# MusicAndSounds/Sounds #
pygame.mixer.music.load('MusicAndSounds/Min_Jam_Fae_Dark.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
###

def selectlevel():
    global play, player_xy, level, flip

    # level stuff #
    if not play:
        number = random.randint(1, 3)
        if number == 1:
            if not level == levels.level:
                level = levels.level
                play = True
            else:
                selectlevel()
        elif number == 2:
            if not level == levels.level1:
                level = levels.level1
                play = True
            else:
                selectlevel()
        else:
            if not level == levels.level2:
                level = levels.level2
                play = True
            else:
                selectlevel()

    ###
    if nexttolevel_right(player_xy):
        play = False
        flip = False
        player_xy = [0, 450]


def main():
    # stupid global stuff #
    global player_y_vel, flip, jumpsLeft, jumped, playerFlipX, dead
    ###

    run = True

    clock = pygame.time.Clock()

    while run:

        selectlevel()

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Player Movement #
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not nextto_right(player_xy, level):
            player_xy[0] += 5
            playerFlipX = False
        if keys[pygame.K_a] and not nextto_left(player_xy, level):
            player_xy[0] -= 5
            playerFlipX = True
        ###

        # jump #
        if not flip:
            if nextto_down(player_xy, level):
                jumpsLeft = 2
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if nextto_down(player_xy, level):
                    player_y_vel = -10
                    jumpsLeft -= 1
                    jumped = True
                if not jumped and jumpsLeft == 1:
                    jumpsLeft = 0
                    jumped = True
                    if random.randint(0, 2) == 1:
                        player_y_vel = -10
                    else:
                        player_y_vel = 10
                        flip = True
            else:
                jumped = False
        else:
            if nextto_up(player_xy, level):
                jumpsLeft = 2
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if nextto_up(player_xy, level):
                    player_y_vel = 10
                    jumpsLeft -= 1
                    jumped = True
                if not jumped and jumpsLeft == 1:
                    jumpsLeft = 0
                    jumped = True
                    if random.randint(0, 2) == 1:
                        player_y_vel = 10
                    else:
                        player_y_vel = -10
                        flip = False
            else:
                jumped = False
        ###

        # gravity #
        if not flip:
            if not nextto_down(player_xy, level):
                player_y_vel += 0.3
        else:
            if not nextto_up(player_xy, level):
                player_y_vel -= 0.3
        ###

        # bumping into the roof #
        if nextto_down((player_xy[0], player_xy[1] - (20 if flip else 0)), level) and player_y_vel > 0:
            player_y_vel = 0
        if nextto_up((player_xy[0], player_xy[1] + (20 if not flip else 0)), level) and player_y_vel < 0:
            player_y_vel = 0

        # velocity I think #
        for _ in range(round(player_y_vel)):
            if player_y_vel > 0 and not nextto_down((player_xy[0], player_xy[1] - (20 if flip else 0)), level):
                player_xy[1] += 1
        for _ in range(-round(player_y_vel)):
            if player_y_vel < 0 and not nextto_up((player_xy[0], player_xy[1] + (20 if not flip else 0)), level):
                player_xy[1] -= 1
        ###

        draw(flip, WIDTH, HEIGHT, WIN, level, jumpsLeft, frame, player_xy, playerFlipX, dead)

    pygame.quit()


if __name__ == "__main__":
    main()
