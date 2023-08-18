def main():
    import pygame
    from collisions import nextto_down, nextto_up, nextto_left, nextto_right
    import texture_loading as tl

    screen = pygame.display.set_mode((1000,800))

    clock = pygame.time.Clock()

    player = tl.player
    player_xy = [0, 0]
    player_y_vel = 0

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
        if ( keys[pygame.K_w] or keys[pygame.K_SPACE] ) and nextto_down(player_xy) and not nextto_up(player_xy):
            player_y_vel = -10

        for _ in range(round(player_y_vel)):
            if player_y_vel > 0 and not nextto_down(player_xy):
                player_xy[1] += 1
        for _ in range(-round(player_y_vel)):
            if player_y_vel < 0 and not nextto_up(player_xy):
                player_xy[1] -= 1

        if not nextto_down(player_xy):
            player_y_vel += 0.3
        elif player_y_vel > 0:
            player_y_vel = 0

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
