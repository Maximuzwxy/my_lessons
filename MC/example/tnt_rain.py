import mcpi.minecraft as minecraft
import mcpi.entity as entity
mc = minecraft.Minecraft.create()
player = mc.player
x, y, z = player.getTilePos()
origin_x, origin_z = x, z
y += 30

import random

while True:
    x = random.randint(origin_x-30,origin_x+30)
    z = random.randint(origin_z-30,origin_z+30)
    mc.spawnEntity(x, y, z, entity.PRIMED_TNT)