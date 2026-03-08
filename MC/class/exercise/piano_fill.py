import time
import pygame

from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player

time.sleep(3)
x, y, z = player.getTilePos()

# Initialise pygame and the mixer
pygame.init()
pygame.mixer.init()

# load WAVS files
C4 = pygame.mixer.Sound("notes/c4.wav")
D4 = pygame.mixer.Sound("notes/d4.wav")
E4 = pygame.mixer.Sound("notes/e4.wav")
F4 = pygame.mixer.Sound("notes/f4.wav")
G4 = pygame.mixer.Sound("notes/g4.wav")
A4 = pygame.mixer.Sound("notes/a4.wav")
B4 = pygame.mixer.Sound("notes/b4.wav")

mc.postToChat("load sounds over!")


# Task1: generate piano keys
# keys = [block.STONE.id, block.GRASS.id, block.WOOD.id, block.DIRT.id, block.SAND.id, block.GRAVEL.id, block.BRICK_BLOCK.id]
keys = [1, 2, 17, 3, 12, 13, 45]
# code



# Task2: keep tracking hit events
# while True:
#     # code
#
#     for h in hits:
#         # code
#
#         mc.postToChat(f'hit the position: {x} {y} {z}')
#         mc.postToChat(f'hit the block: {b}')
#     time.sleep(0.1)

# Task3: Turn stone(any block) into gold
# copy task2

# Task4: Different block, Different Sound
# while True:
#     # Get the block hit events
#     hits = mc.events.pollBlockHits()
#     # for each block that has been hit C4~G4 A4 B4
#     for hit in hits:
#         x, y, z = hit.pos
#         b = mc.getBlock(x, y, z)
#         sound = None
#         if b == block.STONE.id:
#             sound =
#         elif b == block.GRASS.id:
#             sound =
#         elif b == block.WOOD.id:
#             sound =
#         elif b == block.DIRT.id:
#             sound =
#         elif b == block.SAND.id:
#             sound =
#         elif b == block.GRAVEL.id:
#             sound =
#         elif b == block.BRICK_BLOCK.id:
#             sound =
#
#         if sound:
#             # code
#
#     # sleep for a short time
#     time.sleep(0.1)






