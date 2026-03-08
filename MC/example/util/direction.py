X = 1
Z = 2


def getDirection(player):
    pos = player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z

    r = player.getRotation()
    direction = X
    if 0 <= r <= 45 or 315 <= r <= 360:
        direction = Z
    elif 45 <= r <= 135:
        direction = -X
    elif 135 <= r <= 225:
        direction = -Z
    elif 225 <= r <= 315:
        direction = X

    on_x = 0
    on_z = 0
    if direction == X:
        x += 5
        on_z = 1
    elif direction == -X:
        x -= 5
        on_z = -1
    elif direction == Z:
        z += 5
        on_x = -1
    elif direction == -Z:
        z -= 5
        on_x = 1

    return x, y, z, on_x, on_z