from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

# Player position
x, y, z = mc.player.getPos()
x, y, z = int(x), int(y), int(z)

# Castle size
size = 30
wall_height = 8
tower_radius = 3
tower_height = 12

# Clear area
mc.setBlocks(x-5, y, z-5, x+size+5, y+20, z+size+5, block.AIR)

# Ground
mc.setBlocks(x, y-1, z, x+size, y-1, z+size, block.STONE)

# Outer walls
mc.setBlocks(x, y, z, x+size, y+wall_height, z, block.STONE)
mc.setBlocks(x, y, z+size, x+size, y+wall_height, z+size, block.STONE)
mc.setBlocks(x, y, z, x, y+wall_height, z+size, block.STONE)
mc.setBlocks(x+size, y, z, x+size, y+wall_height, z+size, block.STONE)

# Hollow inside
mc.setBlocks(x+1, y, z+1, x+size-1, y+wall_height-1, z+size-1, block.AIR)

# Gate
gate_x = x + size//2
mc.setBlocks(gate_x-1, y, z, gate_x+1, y+3, z, block.AIR)

# Battlements
for i in range(0, size+1, 2):
    mc.setBlock(x+i, y+wall_height+1, z, block.STONE)
    mc.setBlock(x+i, y+wall_height+1, z+size, block.STONE)
    mc.setBlock(x, y+wall_height+1, z+i, block.STONE)
    mc.setBlock(x+size, y+wall_height+1, z+i, block.STONE)

# Towers (4 corners)
def build_tower(cx, cz):
    mc.setBlocks(
        cx-tower_radius, y, cz-tower_radius,
        cx+tower_radius, y+tower_height, cz+tower_radius,
        block.STONE
    )
    mc.setBlocks(
        cx-(tower_radius-1), y, cz-(tower_radius-1),
        cx+(tower_radius-1), y+tower_height-1, cz+(tower_radius-1),
        block.AIR
    )

build_tower(x, z)
build_tower(x+size, z)
build_tower(x, z+size)
build_tower(x+size, z+size)

# Move player inside
mc.player.setPos(x + size//2, y+1, z + size//2)
mc.postToChat("🏰 Castle complete! Welcome, my liege.")
