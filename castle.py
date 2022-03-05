import datetime,time,math

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

mc.setBlocks(-100,0,-100,100,100,100,block.AIR)

def drawTower(tx,ty,tz):
        #create a castle
        mc.setBlocks(tx,ty,tz,tx+10,ty+15,tz+10,block.STONE)
        #create crennelations
        for x in range(0,12):
                for z in range(0,12):
                        if x % 2 == 0 and z % 2 == 0:
                                mc.setBlock(tx+x,ty+16,tz+z,block.STONE)
        mc.setBlocks(tx+1,ty+15,tz+1,tx+9,ty+16,tz+9,block.AIR)
        mc.setBlocks(tx+2,ty+14,tz+2,tx+8,ty+16,tz+8,block.AIR)


def drawWall(x,y,z,length,plane):
        if plane == "x":
                mc.setBlocks(x,y,z,x+length,y+10,z,block.STONE)
                for i in range(length+2):
                        if i % 2 == 0:
                                mc.setBlock(x+i,y+10,z,block.AIR)

        if plane == "z":
                mc.setBlocks(x,y,z,x,y+10,z+length,block.STONE)
                for i in range(length+2):
                        if i % 2 == 0:
                                mc.setBlock(x,y+10,z+i,block.AIR)

drawWall(0,0,0,50,"x")
time.sleep(1)
drawWall(0,0,0,50,"z")
time.sleep(1)
drawWall(0,0,50,50,"x")
time.sleep(1)
drawWall(50,0,0,50,"z")
time.sleep(1)

drawTower(0,0,0)
time.sleep(1)
drawTower(0,0,50)
time.sleep(1)
drawTower(50,0,0)
time.sleep(1)
drawTower(50,0,50)