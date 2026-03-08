import mcpi.minecraft as minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player
pos = player.getTilePos()

x,y,z = pos
for i in range(100):
    mc.setBlock(x,y+i,z+i,block.GOLD_BLOCK)