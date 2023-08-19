# functions check if on a given direction the player is right next to something like the ground or the edge of the screen
# don't try to understand how it works, just ask me if it breaks
# I somehow understood it

import math
from Draw import die


def nextto_down(player_xy, level):
    if player_xy[1] + 70 + 1 > 600:
        return True
    if (player_xy[1] + 70) % 40 == 0:
        if level[math.floor((player_xy[1] + 70) / 40)][math.floor(( player_xy[0] + 17 ) / 40)] == 3:
            die()
    if (player_xy[1] + 70) % 40 == 0:
        if level[math.floor((player_xy[1] + 70) / 40)][math.floor(player_xy[0] / 40)] != 0 or level[math.floor((player_xy[1] + 70) / 40)][math.floor((player_xy[0] + 34) / 40)] != 0:
            return True

    return False


def nextto_up(player_xy, level):
    if player_xy[1] - 1 < 0:
        return True
    if (player_xy[0] - 40) % 40 == 0:
        if level[math.floor((player_xy[1] - 40) / 40)][math.floor((player_xy[0] + 17 ) / 40)] == 4:
            die()
    if (player_xy[1] - 40) % 40 == 0:
        if level[math.floor((player_xy[1] - 40) / 40)][math.floor(player_xy[0] / 40)] != 0 or level[math.floor((player_xy[1] - 40) / 40)][math.floor((player_xy[0] + 34) / 40)] != 0:
            return True
    return False


def nextto_left(player_xy, level):
    if player_xy[0] - 1 < 0:
        return True
    if ( player_xy[0] - 40 ) % 40 == 0:
        if level[math.floor(player_xy[1] / 40)][math.floor((player_xy[0] - 40) / 40)] != 0 or level[math.floor((player_xy[1] + 35) / 40)][math.floor((player_xy[0] - 40) / 40)] != 0 or level[math.floor((player_xy[1] + 69) / 40)][math.floor((player_xy[0] - 40) / 40)] != 0:
            return True
    return False


def nextto_right(player_xy, level):
    if player_xy[0] + 35 + 1 > 1200:
        return True
    if ( player_xy[0] + 35 ) % 40 == 0:
        if level[math.floor(player_xy[1] / 40)][math.floor((player_xy[0] + 35) / 40)] != 0 or level[math.floor((player_xy[1] + 35) / 40)][math.floor((player_xy[0] + 35) / 40)] != 0 or level[math.floor((player_xy[1] + 69) / 40)][math.floor((player_xy[0] + 35) / 40)] != 0:
            return True
    return False


def nexttolevel_right(player_xy):
    if player_xy[0] + 35 + 1 > 1200:
        return True
    return False

