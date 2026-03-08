from mcpi import minecraft
from mcpi import block
from mcpi.vec3 import Vec3
import time

RED = 14
GREEN = 13

# Input the IP Address in create() if your game is running on another device
mc = minecraft.Minecraft.create()
player = mc.player


def stop():
    # LESSON3: YOUR CODE HERE

    # LESSON3: YOUR CODE HERE OVER
    return False


x, y, z = player.getTilePos()
z = z + 1

start_x = x
start_z = z

dx = 1
dz = 0

while True:
    if stop():
        continue
    # POINT A
    if x == start_x and z == start_z:
        dx = 1
        dz = 0
    # POINT B
    elif x == start_x + 10 and z == start_z:
        # LESSON2: YOUR CODE HERE

        # LESSON2: YOUR CODE HERE OVER
        pass
    # POINT C
    elif x == start_x + 10 and z == start_z + 10:
        dx = -1
        dz = 0
    # POINT D
    elif x == start_x and z == start_z + 10:
        # LESSON2: YOUR CODE HERE

        # LESSON2: YOUR CODE HERE OVER
        pass
    mc.setBlock(x, y, z, block.AIR)
    # LESSON2: YOUR CODE HERE

    # LESSON2: YOUR CODE HERE OVER
    mc.setBlock(x, y, z, block.WOOL.id, 10)
    mc.setBlock(x, y - 1, z, block.WOOL.id, 2)

    # sleep a short time
    time.sleep(0.5)
