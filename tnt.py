from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        blockId = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
        if blockId == block.TNT:
            mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.TNT.id, 1)
            mc.postToChat("TNT activated")
    sleep(0.1)
