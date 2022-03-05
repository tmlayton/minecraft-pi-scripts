from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create();

x, y, z = mc.player.getPos();

for j in range(5):
    for k in range(5):
        baseX = 20 * j
        baseZ = 20 * k
        y1 = mc.getHeight(x+1+baseX, z+1+baseZ);
        y2 = mc.getHeight(x+10+baseX, z+10+baseZ);
        y = min(y1, y2);
        mc.setBlocks(x+1+baseX, y, z+1+baseZ, x+10+baseX, y+51, z+10+baseZ, block.CLAY);
        for i in range(13):
            windows = (i * 4) + 1 
            mc.setBlocks(x+1+baseX, windows, z+1+baseZ, x+10+baseX, windows+1, z+10+baseZ, block.GLASS);

        mc.setBlocks(x+2+baseX, y+1, z+2+baseZ, x+9+baseX, y+50, z+9+baseZ, block.AIR);
