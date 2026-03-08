import mcpi.minecraft as minecraft
from util import number
import time

mc = minecraft.Minecraft.create()
player = mc.player
x,y,z = player.getTilePos()

i = 0
while True:
    number.show(mc, i, x+3, y, z)
    time.sleep(1)
    i += 1