import mcpi.minecraft as minecraft
import mcpi.entity as entity

mc = minecraft.Minecraft.create()
player = mc.player

x,y,z = player.getTilePos()

for i in range(2):
    mc.spawnEntity(x, y+i, z, entity.COW)