import random
import time

from mcpi import minecraft
from mcpi import block
from mcpi import entity

mc = minecraft.Minecraft.create('192.168.66.207')

time.sleep(3)

x,y,z = mc.player.getTilePos()


