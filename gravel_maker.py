from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

while True:
	hits = mc.events.pollBlockHits()
	for hit in hits:
		blockId = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z);
		if blockId == 247: mc.setBlock(hit.pos.x, hit.pos.y + 50, hit.pos.z, block.GRAVEL);       
	sleep(0.1)
