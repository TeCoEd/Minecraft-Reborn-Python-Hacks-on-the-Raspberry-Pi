from mcpi.minecraft import Minecraft
from mcpi import block
import math
import time

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

length = 120
base_height = y + 12
hill_height = 6

mc.postToChat("🎢 Generating Reborn Coaster...")

# Clear area
mc.setBlocks(x-5, y, z-5,
             x+length+5, base_height+20, z+5,
             block.AIR)

previous_y = base_height

for i in range(length):
    # Smooth rolling hills
    offset = int(math.sin(i * 0.15) * hill_height)
    current_y = base_height + offset
    
    # Base block under track
    mc.setBlock(x+i, current_y-1, z, block.STONE)
    
    # Rails (powered every 6 blocks)
    if i % 6 == 0:
        mc.setBlock(x+i, current_y, z, 27)  # Powered Rail
    else:
        mc.setBlock(x+i, current_y, z, 66)  # Regular Rail
    
    # Support pillars
    mc.setBlocks(x+i, y, z,
                 x+i, current_y-2, z,
                 block.FENCE)

    previous_y = current_y

mc.postToChat("🎉 Reborn Roller Coaster Ready!")
