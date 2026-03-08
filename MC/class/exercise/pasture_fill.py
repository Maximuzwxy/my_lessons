import time

import mcpi.minecraft as minecraft
from mcpi import block, entity

mc = minecraft.Minecraft.create('192.168.66.207')
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
        print(e)
        entity_id, type_id, type_name, ex, ey, ez = e
        if (area_x1 <= ex <= area_x2 and area_y1 <= ey <= area_y2 and area_z1 <= ez <= area_z2
                and type_name in target_types):
            print('aaa')
            try:
                mc.removeEntity(entity_id)
            except Exception as err:
                print(f"移除实体{entity_id}失败: {err}")
clear_entities()

# # Task1: build a platform
# # clear the space
# def clear_space():
#     time.sleep(1)
#     mc.setBlocks()
#     time.sleep(1)
# clear_space()
#
# # 搭建 50 X 50 的平台
# def build_platform():
#     time.sleep(1)
#     mc.setBlocks()
# build_platform()
#
# cow_x, cow_y, cow_z =
# sheep_x, sheep_y, sheep_z =
# chicken_x, chicken_y, chicken_z =
# horse_x, horse_y, horse_z =
#
# def build_fence():
#     time.sleep(1)
#     # fence-cow
#     for i in range():
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         time.sleep(0.1)
#
#     # fence-sheep
#     for i in range():
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         time.sleep(0.1)
#
#     # fence-chicken
#     for i in range():
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         time.sleep(0.1)
#
#     # fence-horse
#     for i in range():
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         time.sleep(0.1)
#
# build_fence()
#
# # build red stone
# def build_red_stone():
#     time.sleep(1)
#     for i in range():
#         mc.setBlock()
#         mc.setBlock()
#         time.sleep(0.1)
#
#     for i in range():
#         mc.setBlock()
#         mc.setBlock()
#         time.sleep(0.1)
#
# build_red_stone()
#
# # build railway
# def build_railway():
#     time.sleep(1)
#     # clear the railway
#     for i in range():
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#         mc.setBlock()
#
#     time.sleep(1)
#
#     for i in range():
#         time.sleep(0.1)
#         if i == 0 or i == 49 or i == 24 or i == 25:
#             mc.setBlock()
#             mc.setBlock()
#         else:
#             mc.setBlock()
#             mc.setBlock()
#
#     for i in range():
#         time.sleep(0.1)
#         if i == 0 or i == 49 or i == 24 or i == 25:
#             mc.setBlock()
#             mc.setBlock()
#         else:
#             mc.setBlock()
#             mc.setBlock()
#
# build_railway()
#
# def build_doors():
#     time.sleep(1)
#     # cow door
#     # build the left pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the right pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the door
#     mc.setBlock()
#
#     #######################################
#
#     # sheep door
#     # build the left pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the right pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the door
#     mc.setBlock()
#
#     #######################################
#
#     # chicken door
#     # build the left pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the right pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the door
#     mc.setBlock()
#
#     #######################################
#
#     # horse door
#     # build the left pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the right pillar
#     mc.setBlock()
#     mc.setBlock()
#
#     # build the door
#     mc.setBlock()
#
# build_doors()
#
# # spawn animals
# def spawn_animals():
#     time.sleep(1)
#     for i in range():
#         mc.spawnEntity(, entity.COW)
#         mc.spawnEntity(, entity.SHEEP)
#         mc.spawnEntity(, entity.CHICKEN)
#         mc.spawnEntity(, entity.HORSE)
#
#         time.sleep(0.1)
#     mc.spawnEntity(x + 20, y + 1, z + 24, entity.MINECART)
#
# spawn_animals()









