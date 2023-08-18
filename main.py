def main():
    import pygame
    import random
    from collisions import nextto_down, nextto_up, nextto_left, nextto_right
    import texture_loading as tl

    screen = pygame.display.set_mode((1000,800))

    clock = pygame.time.Clock()

    player = tl.player
    player_xy = [0, 0]
    player_y_vel = 0

    jumpsLeft = 0
    flip = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(pygame.Color(0,0,0))
        screen.blit(player, (player_xy[0], player_xy[1]))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not nextto_right(player_xy):
            player_xy[0] += 5
        if keys[pygame.K_a] and not nextto_left(player_xy):
            player_xy[0] -= 5

        if not flip:
            if nextto_down(player_xy):
                jumpsLeft = 2
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if not jumped and not nextto_up(player_xy):
                    if jumpsLeft > 0:
                        if jumpsLeft == 1:
                            if random.randint(0, 2) == 1:
                                player_y_vel = -10
                                jumpsLeft -= 1
                                jumped = True
                            else:
                                player_y_vel = 10
                                flip = True
                                jumpsLeft -= 1
                                jumped = True
                        else:
                            player_y_vel = -10
                            jumpsLeft -= 1
                            jumped = True
            else:
                jumped = False
        elif flip:
            if nextto_up(player_xy):
                jumpsLeft = 2
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if not jumped and not nextto_down(player_xy):
                    if jumpsLeft > 0:
                        if jumpsLeft == 1:
                            if random.randint(0, 2) == 1:
                                player_y_vel = 10
                                jumpsLeft -= 1
                                jumped = True
                            else:
                                player_y_vel = -10
                                flip = False
                                jumpsLeft -= 1
                                jumped = True
                        else:
                            player_y_vel = 10
                            jumpsLeft -= 1
                            jumped = True
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
            elif player_y_vel > 0:
                player_y_vel = 0

        print(jumpsLeft)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()