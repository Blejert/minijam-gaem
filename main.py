def main():
    import pygame
    import random
    from collisions import nextto_down, nextto_up, nextto_left, nextto_right

    WIDTH, HEIGHT = 1275, 675
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # art
    player = pygame.transform.scale(pygame.image.load("art/tile002.png"), (35, 70))
    player_flippedX = pygame.transform.flip(player, True, False)
    player_flippedY = pygame.transform.flip(player, False, True)
    player_flippedYX = pygame.transform.flip(player, True, True)

    clock = pygame.time.Clock()

    player_xy = [0, 0]
    player_y_vel = 0

    # veriables
    jumpsLeft = 0
    flip = False
    playerFlipX = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(pygame.Color(0,0,200))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not nextto_right(player_xy):
            player_xy[0] += 5
            playerFlipX = False
        if keys[pygame.K_a] and not nextto_left(player_xy):
            player_xy[0] -= 5
            playerFlipX = True

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

        for _ in range(round(player_y_vel)):
            if player_y_vel > 0 and not nextto_down(player_xy):
                player_xy[1] += 1
        for _ in range(-round(player_y_vel)):
            if player_y_vel < 0 and not nextto_up(player_xy):
                player_xy[1] -= 1

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

        if not playerFlipX:
            if flip:
                screen.blit(player_flippedY, (player_xy[0], player_xy[1]))
            else:
                screen.blit(player, (player_xy[0], player_xy[1]))
        else:
            if flip:
                screen.blit(player_flippedYX, (player_xy[0], player_xy[1]))
            else:
                screen.blit(player_flippedX, (player_xy[0], player_xy[1]))

        print(jumpsLeft)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()