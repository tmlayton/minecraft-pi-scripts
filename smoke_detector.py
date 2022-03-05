from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block
import pygame

pygame.init();
pygame.mixer.init();
alarm = pygame.mixer.Sound("audio/alarm.wav");
ready = pygame.mixer.Sound("audio/ready.wav");
test = pygame.mixer.Sound("audio/test.wav");
alarmBool = False;
readyBool = False;
testingBool = False;
smokeDetectors = {};
timer = 0;
testBlock = [];
torchActivated = False;
mc = Minecraft.create();

def safe_index(l, value):
  try:
    return l.index(value)
  except ValueError:
    return None;

def anySmokeDetected():
    active = [];
    for sd in smokeDetectors.values():
        if smokeDetected(*sd):
            active.append(sd);
    
    return active;
    
def smokeDetected(x, y, z):
    return searchBlocks(x-2, y-1, z-2, x+2, y-3, z+2, block.TORCH.id);

def searchBlocks(x1, y1, z1, x2, y2, z2, blockId):
    xhigh = max(x1, x2)
    xlow = min(x1, x2)
    yhigh = max(y1, y2)
    ylow = min(y1, y2)
    zhigh = max(z1, z2)
    zlow = min(z1, z2)
 
    for x in range(xhigh - xlow + 1):
        for y in range(yhigh - ylow + 1):
            for z in range(zhigh - zlow + 1):
                currentBlock = mc.getBlock(xlow + x, ylow + y, zlow + z);
                if blockId == currentBlock:
                    print('Fire found');
                    return True;
    return False;

while True:
    timer = timer + 1;
    active = [];
    
    if readyBool == False and testingBool == False:
        active = anySmokeDetected();
    
    if len(active) > 0: 
        for sd in active:
            mc.setBlock(*sd, block.WOOL_RED);
        
        ready.stop();
        test.stop();
        readyBool = False;
        testingBool = False;
        
        if alarmBool == False:
            alarmBool = True;
            alarm.play(-1);
    else:
        if alarmBool == True:
            alarmBool = False;
            alarm.stop();
            
    for sd in smokeDetectors.values():
        if safe_index(active, sd) == None and mc.getBlockWithData(*sd) == block.WOOL_RED:
            mc.setBlock(*sd, block.WOOL_WHITE);
        
    hits = mc.events.pollBlockHits();
    for hit in hits:
        x = hit.pos.x;
        y = hit.pos.y;
        z = hit.pos.z;
        blockWithData = mc.getBlockWithData(x,y,z)
        
        if blockWithData == block.WOOL_WHITE or blockWithData == block.WOOL_CYAN or blockWithData == block.WOOL_LIME:
            key = f'{x}{y}{z}';
            isSd = smokeDetectors.get(key);
            if isSd == None:
                print('smoke detector registered', x, y, z);
                smokeDetectors[key] = [x, y, z];
            elif readyBool == False and testingBool == False and alarmBool == False:
                print('ready')
                timer = 0;
                readyBool = True;
                ready.play();
                testBlock = [x, y, z]
                mc.setBlock(x, y, z, block.WOOL_CYAN);
            elif testingBool == False and alarmBool == False:
                print('testing')
                timer = 0;
                readyBool = False;
                testingBool = True;
                ready.stop();
                test.play();
                testBlock = [x, y, z]
                mc.setBlock(x, y, z, block.WOOL_LIME);
            elif alarmBool == False:
                print('cancel')
                ready.stop();
                test.stop();
                readyBool = False;
                testingBool = False;
                mc.setBlock(x, y, z, block.WOOL_WHITE);
       
    if testingBool == True and timer % 5 == 0:
        if mc.getBlockWithData(*testBlock) == block.WOOL_LIME:
            mc.setBlock(*testBlock, block.WOOL_GREEN)
        else:
            mc.setBlock(*testBlock, block.WOOL_LIME)
    
    if readyBool == True and timer % 5 == 0:
        if mc.getBlockWithData(*testBlock) == block.WOOL_CYAN:
            mc.setBlock(*testBlock, block.WOOL_BLUE)
        else:
            mc.setBlock(*testBlock, block.WOOL_CYAN)
            
    if (timer > 375 and alarmBool == False):
        ready.stop();
        test.stop();
        readyBool = False;
        testingBool = False;
        mc.setBlock(*testBlock, block.WOOL_WHITE);
    sleep(0.1)