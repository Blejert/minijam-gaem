import pygame
import random
from collisions import nextto_down, nextto_up, nextto_left, nextto_right

pygame.font.init()

WIDTH, HEIGHT = 1275, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Python Game")

# BG = pygame.transform.scale(pygame.image.load("bg.PNG"), (WIDTH, HEIGHT))


# variables #
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 5
player_xy = [0, 0]
player_y_vel = 0
jumpsLeft = 0
flip = False
playerFlipX = False
###


FONT = pygame.font.SysFont("", 30)

test = False

# art #
player = pygame.transform.scale(pygame.image.load("art/tile002.png"), (35, 70))
player_flippedX = pygame.transform.flip(player, True, False)
player_flippedY = pygame.transform.flip(player, False, True)
player_flippedYX = pygame.transform.flip(player, True, True)
###


def draw(player):
    # WIN.blit(BG, (0, 0))
    WIN.fill('white')

    # hi_text = FONT.render("HI", True, "white")
    # WIN.blit(hi_text, (10, 10))

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
