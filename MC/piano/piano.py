# www.stuffaboutcode.com
# Raspberry Pi, Minecraft Piano - Different blocks back different tones when hit!

# import the minecraft.py module from the minecraft directory
import mcpi.minecraft as minecraft
# import minecraft block module
import mcpi.block as block
# import time, so delays can be used
import time
# import pygame to use the mixer to play wav file
import pygame

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

print("load sounds over!")

# Connect to minecraft by creating the minecraft object
# - minecraft needs to be running and in a game
mc = minecraft.Minecraft.create()

# loop until Ctrl C
while True:
    # Get the block hit events
    hits = mc.events.pollBlockHits()
    # for each block that has been hit
    for hit in hits:
        x, y, z = hit.pos
        b = mc.getBlock(x, y, z)
        sound = None
        if b == block.STONE.id:
            sound = C4
        elif b == block.GRASS.id:
            sound = D4
        # TASK4 YOUR CODE HERE

        # TASK4 YOUR CODE OVER
        if sound:
            sound.play()
    # sleep for a short time
    time.sleep(0.1)

