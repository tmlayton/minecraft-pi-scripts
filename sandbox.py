from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block

mc = Minecraft.create();

while True:
    hits = mc.events.pollBlockHits();
    for hit in hits:
        x = hit.pos.x;
        y = hit.pos.y;
        z = hit.pos.z;
        
        hitBlock = mc.getBlockWithData(x, y, z)
        
        if hitBlock.id == block.FURNACE_INACTIVE:
            mc.setBlock(x,y,z,62,1);
                  
        if hitBlock.id == block.FURNACE_ACTIVE:
            mc.setBlock(x,y,z,61,2);
    sleep(0.1)
