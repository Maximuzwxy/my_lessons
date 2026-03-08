from mcpi import minecraft
from mcpi import block

# Connect to minecraft by creating the minecraft object
# - minecraft needs to be running and in a game
mc = minecraft.Minecraft.create()
player = mc.player

x, y, z = player.getTilePos()

mc.setBlock(x + 1, y, z, block.STONE)
mc.setBlock(x + 2, y, z, block.GRASS)
mc.setBlock(x + 3, y, z, block.WOOD)
# TASK2: YOUR CODE HERE
