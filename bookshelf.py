from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create();
bookshelves = {};

def isBookshelf(x, y, z):
    blocks = []
    hitBlock = mc.getBlock(x, y, z);
    blocks.append(hitBlock);
    
    # make this work in the z direction too
    blocks.append(mc.getBlock(x-1, y, z));
    blocks.append(mc.getBlock(x+1, y, z));
    blocks.append(mc.getBlock(x, y-1, z));
    blocks.append(mc.getBlock(x, y+1, z));
    return len(set(blocks)) == 1 and hitBlock == block.BOOKSHELF.id;

while True:
    hits = mc.events.pollBlockHits();
    for hit in hits:
        x = hit.pos.x;
        y = hit.pos.y;
        z = hit.pos.z;
            
        if isBookshelf(x, y, z) == True:
            
            bookshelfKey = f'{x}{y}{z}';
            key2 = f'{x-2}{y}{z}';
            isOpen = bookshelves.get(bookshelfKey);
            value2 = bookshelves.get(key2);
            
            if isOpen == None and value2 != None:
                isOpen = value2;
                bookshelfKey = key2;
            
            if isOpen == False or isOpen == None:
                # make this work in the z direction too
                mc.setBlocks(x,y+1,z, x-1,y-1,z, block.AIR);
                mc.setBlocks(x+2,y+1,z, x+3,y-1,z, block.BOOKSHELF);
                bookshelves[bookshelfKey] = True;
            else:
                # make this work in the z direction too
                mc.setBlocks(x,y+1,z, x+1,y-1,z, block.AIR);
                mc.setBlocks(x-2,y+1,z, x-3,y-1,z, block.BOOKSHELF);
                bookshelves[bookshelfKey] = False;
                
    sleep(0.1)