import pygame
import random
import math
import button
import levels
import levels1
import Draw
from collisions import nextto_down, nextto_up, nextto_left, nextto_right, nexttolevel_right
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Jump")

level = levels.level1
level_list = [levels.level, levels.level1, levels.level2, levels.level3]
level_list1 = [levels1.level, levels1.level1, levels1.level2, levels1.level3]

# variables #
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 5
player_xy = [0, 450]
player_y_vel = 0
jumpsLeft = 0
flip = False
already_pressed = False
playerFlipX = False
frame = 0
score = -1
play = False
test = False
start = False
has_jumped = False
gavePoint = False
credits = False
tutorial = False
###

# MusicAndSounds/Sounds #
pygame.mixer.music.load('MusicAndSounds/Min_Jam_Fae_Dark.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

Jump_Sound = pygame.mixer.Sound("MusicAndSounds/jump.wav")
Jump_Sound.set_volume(0.5)

Click_Sound = pygame.mixer.Sound("MusicAndSounds/click.wav")
Click_Sound.set_volume(0.5)

Gravity_Sound = pygame.mixer.Sound("MusicAndSounds/gravity.wav")
Gravity_Sound.set_volume(0.5)
###

buttonS = pygame.transform.scale(pygame.image.load("art/Sprite-0003.png"), (160, 80))
buttonS1 = pygame.transform.scale(pygame.image.load("art/Sprite-0003.png"), (80, 40))
background = pygame.transform.scale(pygame.image.load("art/tiles/tile019.png"), (40, 40))

FONT = pygame.font.SysFont("", 30)
FONT1 = pygame.font.SysFont("", 100)
FONT2 = pygame.font.SysFont("", 50)

def drawstart(WIN):
    pygame.display.update()
    global start, credits, tutorial
    # background #
    for x in range(math.ceil(WIDTH / 40)):
        for y in range(math.ceil(HEIGHT / 40)):
            WIN.blit(background, (x * 40, y * 40))
    ###

    print(pygame.mouse.get_pressed()[0])
    clicked = pygame.mouse.get_pressed()[0] and not already_pressed

    if not credits and not tutorial:
        start_text = FONT1.render("Coin Jump", True, "white")
        WIN.blit(start_text, (WIDTH / 2 - 180, HEIGHT / 2 - 150 + 20))

        button.draw_button(WIN, WIDTH / 2 - 160 / 2, HEIGHT / 2 - 10, buttonS)
        start_text = FONT2.render("Play", True, "black")
        WIN.blit(start_text, (WIDTH / 2 - 80 + 40, HEIGHT / 2 - 10 + 20))
        if button.is_button_clicked(WIDTH / 2 - 160 / 2, HEIGHT / 2 - 40, buttonS, clicked):
            Click_Sound.play()
            start = True

        button.draw_button(WIN, WIDTH / 2 - 160 / 2, HEIGHT / 2 + 80, buttonS)
        credits_text = FONT2.render("Credits", True, "black")
        WIN.blit(credits_text, (WIDTH / 2 - 60, HEIGHT / 2 + 100))
        if button.is_button_clicked(WIDTH / 2 - 160 / 2, HEIGHT / 2 + 80, buttonS, clicked):
            Click_Sound.play()
            credits = True

        button.draw_button(WIN, WIDTH / 2 - 160 / 2, HEIGHT / 2 + 170, buttonS1)
        quit_text = FONT.render("quit", True, "black")
        WIN.blit(quit_text, (WIDTH / 2 - 60, HEIGHT / 2 + 180))
        if button.is_button_clicked(WIDTH / 2 - 160 / 2, HEIGHT / 2 + 170, buttonS1, clicked):
            Click_Sound.play()
            pygame.quit()
            quit()

        button.draw_button(WIN, WIDTH / 2 - 00 / 2, HEIGHT / 2 + 170, buttonS1)
        t_text = FONT.render("tutorial", True, "black")
        WIN.blit(t_text, (WIDTH / 2 + 5, HEIGHT / 2 + 180))
        if button.is_button_clicked(WIDTH / 2 - 00 / 2, HEIGHT / 2 + 170, buttonS1, clicked):
            Click_Sound.play()
            tutorial = True
    elif credits:
        text = FONT.render("Programming By: Theboredkid and Blejert", True, "white")
        WIN.blit(text, (WIDTH / 3, HEIGHT / 2))
        text2 = FONT.render("Music By: Zig zag", True, "white")
        WIN.blit(text2, (WIDTH / 2 - 125, HEIGHT / 2 + 25))
        text1 = FONT.render("Art By: Spelunky", True, "white")
        WIN.blit(text1, (WIDTH / 2 - 97, HEIGHT / 2 + 50))

        button.draw_button(WIN, WIDTH / 2 - 80 / 2, HEIGHT / 2 + 170, buttonS1)
        quit_text = FONT.render("return", True, "black")
        WIN.blit(quit_text, (WIDTH / 2 - 30, HEIGHT / 2 + 180))
        if button.is_button_clicked(WIDTH / 2 - 80 / 2, HEIGHT / 2 + 170, buttonS1, clicked):
            Click_Sound.play()
            credits = False
    else:
        text = FONT.render("When you double jump theres a 50/50 chance that gravity flips", True, "white")
        WIN.blit(text, (WIDTH / 5, HEIGHT / 2))

        button.draw_button(WIN, WIDTH / 2 - 80 / 2, HEIGHT / 2 + 170, buttonS1)
        quit_text = FONT.render("return", True, "black")
        WIN.blit(quit_text, (WIDTH / 2 - 30, HEIGHT / 2 + 180))
        if button.is_button_clicked(WIDTH / 2 - 80 / 2, HEIGHT / 2 + 170, buttonS1, clicked):
            Click_Sound.play()
            tutorial = False



def resetscore():
    global score
    score = 0


def selectlevel():
    global play, player_xy, level, flip, score, gavePoint
    # level stuff #
    if not play:
        if not Draw.dead:
            if not gavePoint:
                score += 1
                gavePoint = True
        print("hi")
        if score < 10:
            chosen_level = level_list[random.randint(0, 3)]
        else:
            chosen_level = level_list1[random.randint(0, 2)]
        if not level == chosen_level:
            level = chosen_level
            play = True
            selectlevel()
    else:
        gavePoint = False

    ###
    if nexttolevel_right(player_xy):
        play = False
        flip = False
        player_xy = [0, 450]


def main():
    # stupid global stuff #
    global player_y_vel, flip, jumpsLeft, jumped, playerFlipX, player_xy, play, score, already_pressed
    ###

    run = True

    while run:


        if start:
            selectlevel()

            if not Draw.dead:
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
                        if not has_jumped and not jumpsLeft <= 0:
                            Jump_Sound.play()
                            has_jumped = True
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
                                Gravity_Sound.play()
                                flip = True
                    else:
                        has_jumped = False
                        jumped = False
                else:
                    if nextto_up(player_xy, level):
                        jumpsLeft = 2
                    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                        if not has_jumped and not jumpsLeft <= 0:
                            Jump_Sound.play()
                            has_jumped = True
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
                                Gravity_Sound.play()
                                flip = False
                    else:
                        has_jumped = False
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

            if Draw.dead:
                pygame.mouse.set_visible(True)
                player_xy = [0, 450]
                if not test:
                    play = False
                    test = True
                    flip = False
            else:
                pygame.mouse.set_visible(False)
                test = False

            if Draw.t:
                score = 0
                Draw.t = False

            Draw.draw(flip, WIDTH, HEIGHT, WIN, level, jumpsLeft, frame, player_xy, playerFlipX, score, pygame.mouse.get_pressed()[0] and not already_pressed)
        else:
            pygame.mouse.set_visible(True)
            drawstart(WIN)

        already_pressed = pygame.mouse.get_pressed()[0]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
