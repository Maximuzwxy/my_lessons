from mcpi import minecraft
from mcpi import block
import time

# Input the IP Address in create() if your game is running on another device
mc = minecraft.Minecraft.create()
player = mc.player

x, y, z = player.getTilePos()
x = x + 1
mc.setBlock(x, y, z, block.WOOL.id, 10)

for i in range(10):
    # sleep a short time
    time.sleep(0.5)
    mc.setBlock(x, y, z, block.AIR.id)
    # YOUR CODE HERE

    mc.setBlock(x, y, z, block.WOOL.id, 10)
