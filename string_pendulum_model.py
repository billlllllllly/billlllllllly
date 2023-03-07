import PIL
from PIL import Image
from math import *

zoominrate = 1
k = float(100) #N/m
m = float(1) #kg
dt = 0.001   #s
x0, y0 = 100, 25
x = float(100+40)#cm
y = float(0+30)#cm
g = 9.8 #m/s2
l0 = 20 #cm
vx = 0.0 #m/s
ax = 0.0 #m/s2
vy = 0.0 #m/s
ay = 0.0 #m/s2
t = 0.0  #s
sizex, sizey = 200, 200


p1 = PIL.Image.new(mode="RGB", size=(sizex, sizey), color = (250, 250, 250))
p2 = p1.load()

def length(x, y):
    temp = sqrt((x-x0)**2 + (y - y0)**2)
    #print(temp)
    return(temp)

p2[x-1, y-1] = (200, 0, 0)
p2[x-1, y] = (200, 0, 0)
p2[x-1, y+1] = (200, 0, 0)
p2[x, y-1] = (200, 0, 0)
p2[x, y] = (200, 0, 0)
p2[x, y+1] = (200, 0, 0)
p2[x+1, y-1] = (200, 0, 0)
p2[x+1, y] = (200, 0, 0)
p2[x+1, y+1] = (200, 0, 0)

while t <= 50:
    l = length(x, y)
    x  += vx*dt + ax*dt*dt/2
    y  += vy*dt + ay*dt*dt/2
    ax = (k*(l - l0)/100*(50-x)/l)/m
    ay = (k*(l - l0)/100*(0-y)/l + m*g)/m
    vx += ax*dt
    vy += ay*dt
    #print(f"[{0}{1}]", ax, ay)
    
    if floor(x)<sizex and floor(y)<sizey and floor(x)>0 and floor(y)>0:
        p2[floor(x), floor(y)] = (0, 0, 0)
    t += dt


p1.show()
