import pygame

next_frame_time = 0
current_frame = 0
animation_count = 0  # Initialize a counter for the number of repetitions


def animation(WIN, s, xy, time, reset):
    global next_frame_time, current_frame, animation_count
    if not reset:
        current_time = pygame.time.get_ticks()

        if current_time > next_frame_time:
            current_frame = (current_frame + 1) % len(s)
            next_frame_time = current_time + time
            animation_count += 1

        WIN.blit(s[current_frame], xy)
        return animation_count
    else:
        animation_count = 0

