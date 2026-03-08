import mcpi.minecraft as minecraft
from mcpi import entity
mc = minecraft.Minecraft.create()
player = mc.player

x, y, z = player.getTilePos()

mc.spawnEntity(x+1, y, z, entity.CHICKEN)
# YOU CODE HERE
mc.spawnEntity(x-1, y, z, entity.SHEEP)
mc.spawnEntity(x, y, z+1, entity.COW)
mc.spawnEntity(x, y, z-1, entity.HORSE)
