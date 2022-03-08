from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()
x, y, z = mc.player.getPos();

mc.setBlocks(x+1,y,z+1, x+10, y+10, z+10, block.WOOL.id, 1);