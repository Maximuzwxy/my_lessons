import mcpi.minecraft as minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player
pos = player.getTilePos()

x,y,z = pos
for i in range(100):
    for j in range(i):
        mc.setBlock(x,y+j,z+i,block.GOLD_BLOCK)