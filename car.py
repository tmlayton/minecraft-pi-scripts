from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

going = False
carX = 0
carY = 0
carZ = 0
moves = 0
position = "bottom"

while True:
    if going == True:
        if position == "bottom":
            carY = carY + 1
            mc.setBlock(carX, carY, carZ, block.GOLD_BLOCK)
            mc.setBlock(carX, carY - 1, carZ, block.AIR)
            mc.player.setPos(carX + 0.5, carY + 1, carZ + 0.5)
        else:
            carY = carY - 1
            mc.setBlock(carX, carY, carZ, block.GOLD_BLOCK)
            mc.setBlock(carX, carY + 1, carZ, block.AIR)
            mc.player.setPos(carX + 0.5, carY + 1, carZ + 0.5)

        moves = moves + 1

        if moves >= 35:
            going = False
            moves = 0
            if position == "bottom":
                position = "top"
            else:
                position = "bottom"

    hits = mc.events.pollBlockHits()
    for hit in hits:
        blockId = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
        if blockId == block.GOLD_BLOCK.id:
            going = True
            carX = hit.pos.x
            carY = hit.pos.y
            carZ = hit.pos.z

    sleep(0.1)
