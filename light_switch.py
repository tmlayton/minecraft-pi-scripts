from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block

turningOn = False;
turningOff = False;
lightState = False;
mc = Minecraft.create();
lights = [];

while True:
    if turningOn:
        turningOn = False;
        turningOff = False;
        for light in lights:
            mc.setBlock(light['x'], light['y'], light['z'], block.GLOWSTONE_BLOCK);
            
    elif turningOff:
        turningOn = False;
        turningOff = False;
        for light in lights:
            x, y, z = light;
            mc.setBlock(light['x'], light['y'], light['z'], block.WOOL_BLACK);
    
    hits = mc.events.pollBlockHits();
    for hit in hits:
        x, y, z = hit.pos;
        key = {'x': x, 'y': y, 'z': z};
        blockWithData = mc.getBlockWithData(x, y, z);
                
        if (blockWithData == block.WOOL_BLACK or blockWithData == block.GLOWSTONE_BLOCK) and key not in lights:
            lights.append(key);
            mc.postToChat(f'Light {key}');
                
        elif blockWithData.id == 247:
            if lightState:
                lightState = False;
                turningOff = True;
            else:
                lightState = True;
                turningOn = True;
    sleep(0.1)