from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

# Player position
x, y, z = mc.player.getPos()
x, y, z = int(x), int(y), int(z)

# Castle settings
size = 30
wall_height = 8
tower_radius = 3
tower_height = 12
gate_height = 5

# Clear area
mc.setBlocks(x-5, y, z-5, x+size+5, y+25, z+size+5, block.AIR)

# Ground
mc.setBlocks(x, y-1, z, x+size, y-1, z+size, block.STONE)

# Walls
mc.setBlocks(x, y, z, x+size, y+wall_height, z, block.STONE)
mc.setBlocks(x, y, z+size, x+size, y+wall_height, z+size, block.STONE)
mc.setBlocks(x, y, z, x, y+wall_height, z+size, block.STONE)
mc.setBlocks(x+size, y, z, x+size, y+wall_height, z+size, block.STONE)

# Hollow interior
mc.setBlocks(x+1, y, z+1, x+size-1, y+wall_height-1, z+size-1, block.AIR)

# Towers
def build_tower(cx, cz):
    mc.setBlocks(cx-tower_radius, y, cz-tower_radius,
                 cx+tower_radius, y+tower_height, cz+tower_radius,
                 block.STONE)
    mc.setBlocks(cx-(tower_radius-1), y, cz-(tower_radius-1),
                 cx+(tower_radius-1), y+tower_height-1, cz+(tower_radius-1),
                 block.AIR)

build_tower(x, z)
build_tower(x+size, z)
build_tower(x, z+size)
build_tower(x+size, z+size)

# Gate position
gate_x = x + size // 2
gate_z = z

# Gate frame
mc.setBlocks(gate_x-2, y, gate_z,
             gate_x+2, y+gate_height+1, gate_z,
             block.STONE)

# Gate door (starts CLOSED)
def draw_gate(bottom_y):
    mc.setBlocks(gate_x-1, bottom_y, gate_z,
                 gate_x+1, bottom_y+gate_height-1, gate_z,
                 block.IRON_BLOCK)

# Clear gate space
mc.setBlocks(gate_x-1, y, gate_z,
             gate_x+1, y+gate_height, gate_z,
             block.AIR)

# Close gate
draw_gate(y)

time.sleep(1)

# Animate gate UP
for i in range(gate_height + 1):
    mc.setBlocks(gate_x-1, y, gate_z,
                 gate_x+1, y+gate_height+1, gate_z,
                 block.AIR)
    draw_gate(y + i)
    time.sleep(0.4)

time.sleep(2)

# Animate gate DOWN
for i in reversed(range(gate_height + 1)):
    mc.setBlocks(gate_x-1, y, gate_z,
                 gate_x+1, y+gate_height+1, gate_z,
                 block.AIR)
    draw_gate(y + i)
    time.sleep(0.4)

# Move player inside
mc.player.setPos(x + size//2, y+1, z + 3)
mc.postToChat("⚙️ Gate cycle complete!")
