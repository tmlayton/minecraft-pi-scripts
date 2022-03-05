from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create();

def transform(fromId, toId):
    while True:
        hits = mc.events.pollBlockHits();
        for hit in hits:
            x = hit.pos.x;
            y = hit.pos.y;
            z = hit.pos.z;
            
            if mc.getBlock(x, y, z) == fromId:
                mc.setBlock(x, y, z, toId);
                        
        sleep(0.1)