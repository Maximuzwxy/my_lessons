import mcpi.minecraft as minecraft
from mcpi import block
import time

# mc = minecraft.Minecraft.create('192.168.66.207', 4711)
mc = minecraft.Minecraft.create()
player = mc.player
x,y,z = player.getTilePos()
player.setPos(x,y+100,z)
while True:
    pos = player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y, z, block.FLOWER_YELLOW)
    time.sleep(1)