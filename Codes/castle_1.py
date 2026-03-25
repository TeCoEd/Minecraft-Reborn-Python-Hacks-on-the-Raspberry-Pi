from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

# Main castle body
mc.setBlocks(x, y, z, x+20, y+10, z+20, block.STONE)

# Hollow inside
mc.setBlocks(x+1, y+1, z+1, x+19, y+9, z+19, block.AIR)

# Towers
for dx, dz in [(0,0), (20,0), (0,20), (20,20)]:
    mc.setBlocks(x+dx, y, z+dz, x+dx+4, y+15, z+dz+4, block.BRICK_BLOCK)

# Windows
for i in range(2, 19, 4):
    mc.setBlocks(x+i, y+4, z, x+i+1, y+6, z, block.GLASS)

mc.postToChat("🏰 Castle Complete!")
