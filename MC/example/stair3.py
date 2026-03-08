import mcpi.minecraft as minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player
pos = player.getTilePos()

x,y,z = pos
for i in range(10):
    for j in range(i):
        for k in range(10):
            mc.setBlock(x+k, y+j, z+i, block.GOLD_BLOCK)