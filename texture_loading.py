import pygame

spritesheet = pygame.image.load("minijam-gaem/Coin_Flip_Sheet.png")

texture_rect = pygame.Rect(40, 0, 8, 16)
player = pygame.Surface(texture_rect.size)
player.blit(spritesheet, (0, 0), texture_rect)
player = pygame.transform.scale(player, (50, 100))