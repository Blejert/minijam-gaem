import pygame
import random
import math
from collisions import nextto_down, nextto_up, nextto_left, nextto_right
from animation import animation
pygame.font.init()
pygame.mixer.init()

pygame.font.init()

WIDTH, HEIGHT = 1275, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Jump")


# variables #
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 5
player_xy = [0, 0]
player_y_vel = 0
jumpsLeft = 0
flip = False
playerFlipX = False
frame = 0
###

FONT = pygame.font.SysFont("", 30)

# art #
player = pygame.transform.scale(pygame.image.load("art/tile002.png"), (35, 70))
player_flippedX = pygame.transform.flip(player, True, False)
player_flippedY = pygame.transform.flip(player, False, True)
player_flippedYX = pygame.transform.flip(player, True, True)

background = pygame.transform.scale(pygame.image.load("art/tile019.png"), (35, 35))
grass = pygame.transform.scale(pygame.image.load("art/tile016.png"), (35, 35))

coin = pygame.transform.scale(pygame.image.load("tile000.png"), (35, 35))
coin1 = pygame.transform.scale(pygame.image.load("tile001.png"), (35, 35))
coin2 = pygame.transform.scale(pygame.image.load("tile002.png"), (35, 35))
coin3 = pygame.transform.scale(pygame.image.load("tile003.png"), (35, 35))
###

# MusicAndSounds/Sounds #
pygame.mixer.music.load('MusicAndSounds/Min_Jam_Fae_Dark.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
###



def draw(player):
    global next_frame_time, current_frame, frame, playCoin
    WIN.fill('white')

    # background #
    for x in range(math.ceil(WIDTH / 35)):
        for y in range(math.ceil(HEIGHT / 35)):
            WIN.blit(background, (x * 35, y * 35))
    ###

    # text #
    s = [coin, coin1, coin2, coin3]
    xy = (0, 0)
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


def main():
    # stupid global stuff #
    global player_y_vel
    global flip
    global jumpsLeft
    global jumped
    global playerFlipX
    ###

    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Player Movement #
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not nextto_right(player_xy):
            player_xy[0] += 5
            playerFlipX = False
        if keys[pygame.K_a] and not nextto_left(player_xy):
            player_xy[0] -= 5
            playerFlipX = True
        ###

        # jump #
        if not flip:
            if nextto_down(player_xy):
                jumpsLeft = 2
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if nextto_down(player_xy):
                    player_y_vel = -10
                    jumpsLeft -= 1
                    jumped = True
                if not jumped and jumpsLeft == 1 and not nextto_up(player_xy):
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
            if nextto_up(player_xy):
                jumpsLeft = 2
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if nextto_up(player_xy):
                    player_y_vel = 10
                    jumpsLeft -= 1
                    jumped = True
                if not jumped and jumpsLeft == 1 and not nextto_down(player_xy):
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
            if not nextto_down(player_xy):
                player_y_vel += 0.3
            elif player_y_vel > 0:
                player_y_vel = 0
        else:
            if not nextto_up(player_xy):
                player_y_vel -= 0.3
            elif player_y_vel < 0:
                player_y_vel = 0
        ###

        # velocity I think #
        for _ in range(round(player_y_vel)):
            if player_y_vel > 0 and not nextto_down(player_xy):
                player_xy[1] += 1
        for _ in range(-round(player_y_vel)):
            if player_y_vel < 0 and not nextto_up(player_xy):
                player_xy[1] -= 1
        ###

        draw(player)

    pygame.quit()


if __name__ == "__main__":
    main()


    pygame.quit()


if __name__ == "__main__":
    main()
