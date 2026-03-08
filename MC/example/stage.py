import mcpi.minecraft as minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player
pos = player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for i in range(100):
    for j in range(100):
        mc.setBlock(x+i, y, z+j, block.GOLD_BLOCK)