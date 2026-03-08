import random
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
player = mc.player

while True:
    x = random.randint(-5000, 5000)
    y = random.randint(0, 50)
    z = random.randint(-5000, 5000)
    mc.setBlock(x, y, z, 0)
    mc.setBlock(x, y+1, z, 0)
    player.setPos(x, y, z)
    time.sleep(5)
