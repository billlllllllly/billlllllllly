import PIL
from PIL import Image, ImageSequence
import cv2
from math import *
import os, shutil

def length(x0, xtemp, y0, ytemp):
    temp = sqrt((xtemp-x0)**2 + (ytemp - y0)**2)
    #print(temp)
    return(temp)

def f1(inx, iny):
    zoominrate = 1
    k = float(27.84) #N/m
    m = float(0.5) #kg
    dt = 0.0001   #s
    x0, y0 = 100, 25
    x = inx #cm
    y = iny #cm
    xtemp = float(x + x0)
    ytemp = float(y + y0)
    g = 9.8 #m/s2
    l0 = 15.8 #cm
    vx = 0.0 #m/s
    ax = 0.0 #m/s2
    vy = 0.0 #m/s
    ay = 0.0 #m/s2
    t = 0.0  #s
    sizex, sizey = 200, 200

    p1 = PIL.Image.new(mode="RGB", size=(sizex, sizey), color = (250, 250, 250))
    p2 = p1.load()



    while t <= 60:
        l = length(x0, xtemp, y0, ytemp)
        xtemp  += vx*dt + ax*dt*dt/2
        ytemp  += vy*dt + ay*dt*dt/2
        ax = (k*(l - l0)/100*(x0-xtemp)/l)/m
        ay = (k*(l - l0)/100*(y0-ytemp)/l + m*g)/m
        vx += ax*dt
        vy += ay*dt
        #print(f"[{l}, {ax}, {ay}]")
    
        if floor(xtemp)<sizex and floor(ytemp)<sizey and floor(xtemp)>0 and floor(ytemp)>0:
            p2[floor(xtemp), floor(ytemp)] = (0, 0, 0)
        t += dt

    #marking initial
    x += x0
    y += y0

    i = x - 1
    while i <= x+1:
        j = y - 1
        while j <= y+1:
            if i<sizex and i>0 and j<sizey and j>0:
                p2[i, j] = (200, 0, 0)
            j+=1
        i+=1
            
    x -= x0
    y -= y0


    #p1.show()
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/模擬'
    os.chdir(path)
    p1.save(f"p({x}, {y})model.png")


#main

i = 95
while i <= 100:
    j = 5
    while j <= 100:
        f1(i, j)
        print(f"({i},{j})")
        j += 5
    i += 5
print(" --end-- ")


#f1(40, 30)
