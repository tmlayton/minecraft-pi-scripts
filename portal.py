from mcpi import minecraft
from mcpi import block
from time import sleep

mc = minecraft.Minecraft.create();

while True:
    x, y, z = mc.player.getPos();
        
    playerLeft = mc.getBlock(x-1, y, z);
    playerRight = mc.getBlock(x+1, y, z);
        
    if playerLeft == block.OBSIDIAN.id or playerRight == block.OBSIDIAN.id:
        mc.player.setPos(94.5, -30, 52.5);

    sleep(0.1)
