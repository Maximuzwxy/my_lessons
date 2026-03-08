from mcpi import minecraft
from mcpi import block

# Input the IP Address in create() if your game is running on another device
mc = minecraft.Minecraft.create()
player = mc.player

x, y, z = player.getTilePos()
x = x + 1

# A
mc.setBlock(x, y, z, block.WOOL.id, 10)
# B
mc.setBlock(x, y + 1, z, block.WOOL.id, 10)
# LIGHT
# YOUR CODE HERE

# YOUR CODE HERE OVER
print(x, y + 2, z)
