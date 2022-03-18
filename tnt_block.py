from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()
x,y,z = mc.player.getPos()

mc.setBlocks(x, y+1, z, x+51, y+2, z+28, block.AIR);