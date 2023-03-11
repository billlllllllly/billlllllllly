import PIL
from PIL import Image, ImageSequence
import cv2
from math import *


zoominrate = 1
k = float(27.84) #N/m
m = float(0.5) #kg
dt = 0.0001   #s
x0, y0 = 100, 25
x = 10 #cm
y = 50 #cm
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

def length(x, y):
    temp = sqrt((xtemp-x0)**2 + (ytemp - y0)**2)
    #print(temp)
    return(temp)

while t <= 2:
    l = length(xtemp, ytemp)
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

#marking 
x += x0
y += y0
p2[x-1, y-1] = (200, 0, 0)
p2[x-1, y] = (200, 0, 0)
p2[x-1, y+1] = (200, 0, 0)
p2[x, y-1] = (200, 0, 0)
p2[x, y] = (200, 0, 0)
p2[x, y+1] = (200, 0, 0)
p2[x+1, y-1] = (200, 0, 0)
p2[x+1, y] = (200, 0, 0)
p2[x+1, y+1] = (200, 0, 0)
x -= x0
y -= y0


p1.show()
#p1.save(f"p({x}, {y})model.png")
