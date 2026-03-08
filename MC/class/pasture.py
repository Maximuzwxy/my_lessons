import time

import mcpi.minecraft as minecraft
from mcpi import block, entity

mc = minecraft.Minecraft.create()
# mc = minecraft.Minecraft.create('192.168.66.207')
player = mc.player
time.sleep(3)

# pasture position
x, y, z = -530, 25, 50

def clear_entities():
    # 清除指定区域内的牛羊鸡马
    entities = mc.getEntities()
    # 区域范围
    area_x1, area_y1, area_z1 = x, 89, z
    area_x2, area_y2, area_z2 = x + 60, 91, z + 60
    target_types = ['COW', 'SHEEP', 'CHICKEN', 'HORSE']
    for e in entities:
        entity_id, type_id, type_name, ex, ey, ez = e
        if (area_x1 <= ex <= area_x2 and area_y1 <= ey <= area_y2 and area_z1 <= ez <= area_z2
                and type_name in target_types):
            try:
                mc.removeEntity(entity_id)
            except Exception as err:
                print('Error: ', err)
clear_entities()

# Task1: build a platform
# clear the space
def clear_space():
    time.sleep(1)
    mc.setBlocks(x, y, z, x + 49, y + 3, z + 49, 0)
    time.sleep(1)
clear_space()

# 搭建 50 X 50 的平台
def build_platform():
    time.sleep(1)
    mc.setBlocks(x, y, z, x+49, y, z+49, 2)
build_platform()

cow_x, cow_y, cow_z = x, y + 1, z
sheep_x, sheep_y, sheep_z = x + 26, y + 1, z
chicken_x, chicken_y, chicken_z = x, y + 1, z + 26
horse_x, horse_y, horse_z = x + 26, y + 1, z + 26

def build_fence():
    time.sleep(1)
    # fence-cow
    for i in range(23):
        mc.setBlock(cow_x + i, cow_y, cow_z, 85)
        mc.setBlock(cow_x + 23, cow_y, cow_z + i, 85)
        mc.setBlock(cow_x + 23 - i, cow_y, cow_z + 23, 85)
        mc.setBlock(cow_x, cow_y, cow_z + 23 - i, 85)
        time.sleep(0.1)

    # fence-sheep
    for i in range(23):
        mc.setBlock(sheep_x + i, sheep_y, sheep_z, 85)
        mc.setBlock(sheep_x + 23, sheep_y, sheep_z + i, 85)
        mc.setBlock(sheep_x + 23 - i, sheep_y, sheep_z + 23, 85)
        mc.setBlock(sheep_x, sheep_y, sheep_z + 23 - i, 85)
        time.sleep(0.1)

    # fence-chicken
    for i in range(23):
        mc.setBlock(chicken_x + i, chicken_y, chicken_z, 85)
        mc.setBlock(chicken_x + 23, chicken_y, chicken_z + i, 85)
        mc.setBlock(chicken_x + 23 - i, chicken_y, chicken_z + 23, 85)
        mc.setBlock(chicken_x, chicken_y, chicken_z + 23 - i, 85)
        time.sleep(0.1)

    # fence-horse
    for i in range(23):
        mc.setBlock(horse_x + i, horse_y, horse_z, 85)
        mc.setBlock(horse_x + 23, horse_y, horse_z + i, 85)
        mc.setBlock(horse_x + 23 - i, horse_y, horse_z + 23, 85)
        mc.setBlock(horse_x, horse_y, horse_z + 23 - i, 85)
        time.sleep(0.1)

build_fence()

# build red stone
def build_red_stone():
    time.sleep(1)
    for i in range(50):
        mc.setBlock(x + 24, y, z + i, 152)
        mc.setBlock(x + 25, y, z + i, 152)
        time.sleep(0.1)

    for i in range(50):
        mc.setBlock(x + i, y, z + 24, 152)
        mc.setBlock(x + i, y, z + 25, 152)
        time.sleep(0.1)

build_red_stone()

# build railway
def build_railway():
    time.sleep(1)
    # clear first
    # for i in range(50):
    #     mc.setBlock(x + i, y + 1, z + 24, 0)
    #     mc.setBlock(x + i, y + 1, z + 25, 0)
    #     mc.setBlock(x + 24, y + 1, z + i, 0)
    #     mc.setBlock(x + 25, y + 1, z + i, 0)
    #
    # time.sleep(1)

    for i in range(50):
        time.sleep(0.1)
        if i == 0 or i == 49 or i == 24 or i == 25:
            mc.setBlock(x + i, y + 1, z + 24, 66, 2)
            mc.setBlock(x + i, y + 1, z + 25, 66, 5)
        else:
            mc.setBlock(x + i, y + 1, z + 24, 27, 1)
            mc.setBlock(x + i, y + 1, z + 25, 27, 1)

    for i in range(50):
        time.sleep(0.1)
        if i == 0 or i == 49 or i == 24 or i == 25:
            mc.setBlock(x + 24, y + 1, z + i, 66, 3)
            mc.setBlock(x + 25, y + 1, z + i, 66, 4)
        else:
            mc.setBlock(x + 24, y + 1, z + i, 27, 0)
            mc.setBlock(x + 25, y + 1, z + i, 27, 0)

build_railway()

def build_doors():
    time.sleep(1)
    # cow door
    # build the left pillar
    mc.setBlock(cow_x + 23, cow_y, cow_z + 21, 17)
    mc.setBlock(cow_x + 23, cow_y + 1, cow_z + 21, 17)

    # build the right pillar
    mc.setBlock(cow_x + 23, cow_y, cow_z + 23, 17)
    mc.setBlock(cow_x + 23, cow_y + 1, cow_z + 23, 17)

    # build the door
    mc.setBlock(cow_x + 23, cow_y, cow_z + 22, block.FENCE_GATE.id, 1)

    #######################################

    # sheep door
    # build the left pillar
    mc.setBlock(sheep_x, sheep_y, sheep_z + 21, 17)
    mc.setBlock(sheep_x, sheep_y + 1, sheep_z + 21, 17)

    # build the right pillar
    mc.setBlock(sheep_x, sheep_y, sheep_z + 23, 17)
    mc.setBlock(sheep_x, sheep_y + 1, sheep_z + 23, 17)

    # build the door
    mc.setBlock(sheep_x, sheep_y, sheep_z + 22, block.FENCE_GATE.id, 1)

    #######################################

    # chicken door
    # build the left pillar
    mc.setBlock(chicken_x + 23, chicken_y, chicken_z, 17)
    mc.setBlock(chicken_x + 23, chicken_y + 1, chicken_z, 17)

    # build the right pillar
    mc.setBlock(chicken_x + 23, chicken_y, chicken_z + 2, 17)
    mc.setBlock(chicken_x + 23, chicken_y + 1, chicken_z + 2, 17)

    # build the door
    mc.setBlock(chicken_x + 23, chicken_y, chicken_z + 1, block.FENCE_GATE.id, 1)

    #######################################

    # horse door
    # build the left pillar
    mc.setBlock(horse_x, horse_y, horse_z, 17)
    mc.setBlock(horse_x, horse_y + 1, horse_z, 17)

    # build the right pillar
    mc.setBlock(horse_x, horse_y, horse_z + 2, 17)
    mc.setBlock(horse_x, horse_y + 1, horse_z + 2, 17)

    # build the door
    mc.setBlock(horse_x, horse_y, horse_z + 1, block.FENCE_GATE.id, 1)

build_doors()

# spawn animals
def spawn_animals():
    time.sleep(1)
    for i in range(50):
        mc.spawnEntity(cow_x + 12, cow_y, cow_z + 12, entity.COW)
        mc.spawnEntity(sheep_x + 12, sheep_y, sheep_z + 12, entity.SHEEP)
        mc.spawnEntity(chicken_x + 12, chicken_y, chicken_z + 12, entity.CHICKEN)
        mc.spawnEntity(horse_x + 12, horse_y, horse_z + 12, entity.HORSE)

        time.sleep(0.1)
    mc.spawnEntity(x + 20, y + 1, z + 24, entity.MINECART)

spawn_animals()









