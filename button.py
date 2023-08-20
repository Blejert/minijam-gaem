import pygame
pygame.init()

# Set up the font
font = pygame.font.SysFont('Tahoma', 50)


def draw_button(WIN, x, y, button_sprite):
    WIN.blit(button_sprite, (x, y))


# Function to check if the button is clicked
def is_button_clicked(button_x, button_y, button_sprite, clicked):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_rect = button_sprite.get_rect()
    button_rect.topleft = (button_x, button_y)
    return clicked and button_rect.collidepoint(mouse_x, mouse_y)