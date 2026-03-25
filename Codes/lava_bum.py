from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

print("Sneak lava mode activated!")

last_sneak_state = False

while True:
    # Get player entity ID
    player_id = mc.getPlayerEntityId()
    
    # Get current position
    pos = mc.player.getTilePos()
    
    # Check if player is sneaking (Shift key)
    sneak_state = mc.entity.getSneaking(player_id)
    
    # If player JUST started sneaking
    if sneak_state and not last_sneak_state:
        # Place lava block behind/under player
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.LAVA.id)
    
    last_sneak_state = sneak_state
    
    time.sleep(0.1)
