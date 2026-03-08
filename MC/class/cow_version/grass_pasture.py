import time

from mcpi.vec3 import Vec3
import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player

# 获取玩家所在的位置
pos = player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# # 搭建 50 X 50 的平台
mc.setBlocks(x, y, z, x+49, y, z+49, block.GRASS)

pos_cow = Vec3(x, y, z)
pos_sheep = Vec3(x+26, y, z)
pos_chicken = Vec3(x, y, z+26)
pos_horse = Vec3(x+26, y, z+26)


# 划分区域 cow - pink,sheep - yellow, chicken - orange, horse - grey
pink = 6
yellow = 4
orange = 1
grey = 7

# fence
x1 = pos_cow.x
y1 = pos_cow.y
z1 = pos_cow.z
for i in range(23):
    mc.setBlock(x1 + i, y1 + 1, z1, block.FENCE)
    mc.setBlock(x1 + 23, y1 + 1, z1 + i, block.FENCE)
    mc.setBlock(x1 + 23 - i, y1 + 1, z1 + 23, block.FENCE)
    mc.setBlock(x1, y1 + 1, z1 + 23 - i, block.FENCE)


x2 = pos_sheep.x
y2 = pos_sheep.y
z2 = pos_sheep.z
for i in range(23):
    mc.setBlock(x2 + i, y2 + 1, z2, block.FENCE)
    mc.setBlock(x2 + 23, y2 + 1, z2 + i, block.FENCE)
    mc.setBlock(x2 + 23 - i, y2 + 1, z2 + 23, block.FENCE)
    mc.setBlock(x2, y2 + 1, z2 + 23 - i, block.FENCE)


x3 = pos_chicken.x
y3 = pos_chicken.y
z3 = pos_chicken.z
for i in range(23):
    mc.setBlock(x3 + i, y3 + 1, z3, block.FENCE)
    mc.setBlock(x3 + 23, y3 + 1, z3 + i, block.FENCE)
    mc.setBlock(x3 + 23 - i, y3 + 1, z3 + 23, block.FENCE)
    mc.setBlock(x3, y3 + 1, z3 + 23 - i, block.FENCE)


x4 = pos_horse.x
y4 = pos_horse.y
z4 = pos_horse.z
for i in range(23):
    mc.setBlock(x4 + i, y4 + 1, z4, block.FENCE)
    mc.setBlock(x4 + 23, y4 + 1, z4 + i, block.FENCE)
    mc.setBlock(x4 + 23 - i, y4 + 1, z4 + 23, block.FENCE)
    mc.setBlock(x4, y4 + 1, z4 + 23 - i, block.FENCE)

time.sleep(10)

# animals
from mcpi import entity

for i in range(0, 50):
    mc.spawnEntity(x1+12,y1+1,z1+12,entity.COW)
for i in range(0, 50):
    mc.spawnEntity(x2+12,y2+1,z2+12,entity.SHEEP)
for i in range(0, 50):
    mc.spawnEntity(x3+12,y3+1,z3+12,entity.CHICKEN)
for i in range(0, 50):
    mc.spawnEntity(x4+12,y4+1,z4+12,entity.HORSE)

# door
# cow
mc.setBlock(x1+23, y1+1, z1, block.WOOD)
mc.setBlock(x1+23, y1+2, z1, block.WOOD)

mc.setBlock(x1+23,y1+2,z1+1,block.DOOR_WOOD.id, 11)
mc.setBlock(x1+23,y1+1,z1+1,block.DOOR_WOOD.id, 2)

mc.setBlock(x1+23, y1+1, z1+2, block.WOOD)
mc.setBlock(x1+23, y1+2, z1+2, block.WOOD)

# sheep
mc.setBlock(x2+23, y2+1, z2+23, block.WOOD)
mc.setBlock(x2+23, y2+2, z2+23, block.WOOD)

mc.setBlock(x2+22,y2+2,z2+23,block.DOOR_WOOD.id, 9)
mc.setBlock(x2+22,y2+1,z2+23,block.DOOR_WOOD.id, 3)

mc.setBlock(x2+21, y2+1, z2+23, block.WOOD)
mc.setBlock(x2+21, y2+2, z2+23, block.WOOD)

# chicken
mc.setBlock(x3, y3+1, z3, block.WOOD)
mc.setBlock(x3, y3+2, z3, block.WOOD)

mc.setBlock(x3+1,y3+2,z3,block.DOOR_WOOD.id, 8)
mc.setBlock(x3+1,y3+1,z3,block.DOOR_WOOD.id, 1)

mc.setBlock(x3+2, y3+1, z3, block.WOOD)
mc.setBlock(x3+2, y3+2, z3, block.WOOD)

# horse
mc.setBlock(x4, y4+1, z4+23, block.WOOD)
mc.setBlock(x4, y4+2, z4+23, block.WOOD)

mc.setBlock(x4,y4+2,z4+22,block.DOOR_WOOD.id, 10)
mc.setBlock(x4,y4+1,z4+22,block.DOOR_WOOD.id, 0)

mc.setBlock(x4, y4+1, z4+21, block.WOOD)
mc.setBlock(x4, y4+2, z4+21, block.WOOD)
