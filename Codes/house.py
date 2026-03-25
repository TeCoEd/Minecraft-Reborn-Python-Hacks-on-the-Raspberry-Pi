from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

# Get player position
x, y, z = mc.player.getPos()
x, y, z = int(x), int(y), int(z)

# House dimensions
width = 10
depth = 8
height = 5

# Clear space
mc.setBlocks(x-1, y, z-1, x+width+1, y+height+6, z+depth+1, block.AIR)

# Foundation
mc.setBlocks(
    x, y-1, z,
    x+width, y-1, z+depth,
    block.STONE
)

# Walls
mc.setBlocks(
    x, y, z,
    x+width, y+height, z+depth,
    block.WOOD_PLANKS
)

# Hollow inside
mc.setBlocks(
    x+1, y, z+1,
    x+width-1, y+height-1, z+depth-1,
    block.AIR
)

# Door opening
mc.setBlocks(
    x + width//2, y, z,
    x + width//2, y+1, z,
    block.AIR
)

# Windows
mc.setBlocks(x+2, y+2, z, x+3, y+3, z, block.GLASS)
mc.setBlocks(x+width-3, y+2, z, x+width-2, y+3, z, block.GLASS)
mc.setBlocks(x, y+2, z+2, x, y+3, z+3, block.GLASS)
mc.setBlocks(x+width, y+2, z+2, x+width, y+3, z+3, block.GLASS)

# Roof (layered slabs style)
roof_height = y + height
for i in range(4):
    mc.setBlocks(
        x-i, roof_height+i, z-i,
        x+width+i, roof_height+i, z+depth+i,
        block.WOOD
    )

# Floor
mc.setBlocks(
    x+1, y-1, z+1,
    x+width-1, y-1, z+depth-1,
    block.WOOD_PLANKS
)

# Move player inside
mc.player.setPos(x + width//2, y, z + depth//2)

mc.postToChat("🏠 Cool house built!")
