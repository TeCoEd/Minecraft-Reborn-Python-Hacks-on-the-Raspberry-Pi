from mcpi.minecraft import Minecraft
from mcpi import block
import random
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()

size = 25   # MASSIVE size (increase for insanity)

print("Building MEGA Egyptian Pyramid...")

# ------------------------
# Build Outer Pyramid (Hollow)
# ------------------------
for level in range(size):
    width = size - level
    
    for x in range(-width, width + 1):
        for z in range(-width, width + 1):
            
            # Only build walls (hollow inside)
            if (abs(x) == width or abs(z) == width):
                mc.setBlock(pos.x + x,
                            pos.y + level,
                            pos.z + z,
                            block.SANDSTONE.id)

print("Outer shell complete!")

# ------------------------
# Create Entrance Tunnel
# ------------------------
for y in range(3):
    for z in range(-3, 1):
        for x in range(-2, 3):
            mc.setBlock(pos.x + x,
                        pos.y + y,
                        pos.z - size + z,
                        block.AIR.id)

print("Entrance created!")

# ------------------------
# TNT Floor Trap Room
# ------------------------
trap_y = pos.y + 1

for x in range(-5, 6):
    for z in range(-5, 6):
        mc.setBlock(pos.x + x,
                    trap_y,
                    pos.z + z,
                    block.TNT.id)

print("TNT trap installed 😈")

# ------------------------
# Hidden Lava Trap
# ------------------------
for x in range(-2, 3):
    for z in range(-2, 3):
        mc.setBlock(pos.x + x,
                    pos.y + 6,
                    pos.z + z,
                    block.LAVA.id)

print("Lava trap added 🔥")

# ------------------------
# Treasure Room at Top
# ------------------------
treasure_y = pos.y + size - 3

for x in range(-2, 3):
    for z in range(-2, 3):
        mc.setBlock(pos.x + x,
                    treasure_y,
                    pos.z + z,
                    block.GOLD_BLOCK.id)

mc.setBlock(pos.x, treasure_y + 1, pos.z, block.DIAMOND_BLOCK.id)

print("Treasure chamber complete 💎")

print("MEGA PYRAMID FINISHED.")
