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
        hitBlock = mc.getBlock(x,y,z)
        below = mc.getBlock(x,y-1,z)
        
        if hitBlock == 155:            
            if below == block.WATER.id:
                mc.setBlock(x,y,z,0)
                mc.setBlock(x,y-1,z,155);
            else:
                mc.setBlock(x,y+1,z,155);
                mc.setBlock(x,y,z,block.WATER)
            
    sleep(0.1)