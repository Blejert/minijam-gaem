# functions check if on a given direction the player is right next to something like the ground or the edge of the screen
# will get massive changes and will have to get the terrain data to check if the player is next to the ground

def nextto_down(player_xy):
    if player_xy[1] + 100 + 1 > 800:
        return True
    return False

def nextto_up(player_xy):
    return False

def nextto_left(player_xy):
    if player_xy[0] - 1 < 0:
        return True
    return False

def nextto_right(player_xy):
    if player_xy[0] + 50 + 1 > 1000:
        return True
    return False