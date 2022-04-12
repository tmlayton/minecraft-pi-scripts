from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block

mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        x = hit.pos.x
        y = hit.pos.y
        z = hit.pos.z
        hitBlock = mc.getBlock(x, y, z)
        below = mc.getBlock(x, y - 1, z)

        if hitBlock == block.SNOW_BLOCK.id:
            if below == block.WATER_STATIONARY.id:
                mc.setBlock(x, y, z, block.AIR.id)
                mc.setBlock(x, y - 1, z, block.SNOW_BLOCK.id)
            else:
                mc.setBlock(x, y + 1, z, block.SNOW_BLOCK.id)
                mc.setBlock(x, y, z, block.WATER.id)

    sleep(0.1)
