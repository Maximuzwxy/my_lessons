from mcpi import minecraft
from mcpi import block

# Connect to minecraft by creating the minecraft object
# - minecraft needs to be running and in a game
# Input the IP Address in create() if your game is running on another device
mc = minecraft.Minecraft.create()
# Get player object
player = mc.player

# YOUR CODE HERE
player.getTilePos()