from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create();
x, y, z = mc.player.getPos();

for blockId in range(255):
    mc.setBlock(x+1, y, z-blockId, 0);
    