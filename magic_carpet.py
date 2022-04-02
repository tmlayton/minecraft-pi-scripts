from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    if mc.getBlock(x,y-1,z) == block.WOOL_BLACK.id:
        h = mc.getHeight(x-10,z)
        mc.player.setPos(x-10,h,z)

    sleep(0.1)
