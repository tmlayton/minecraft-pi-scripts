from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

while True:
	hits = mc.events.pollBlockHits()
	for hit in hits:
		block = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z);
		block.data = (block.data + 1) & 0xf;
		mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.id, block.data)
		mc.postToChat("Block data is now " + str(block.data))
	sleep(0.1)
