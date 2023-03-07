import PIL
from PIL import Image
from math import *

zoominrate = 1
k = float(0) #N/m
m = float(1) #kg
dt = 0.1   #s
x0, y0 = 100, 25
x = float(150)#cm
y = float(125)#cm
g = 9.8 #m/s2
l0 = 0.10 #m
vx = -20.0 #m/s
ax = 0.0 #m/s2
vy = 20.0 #m/s
ay = 0.0 #m/s2
t = 0.0  #s

p1 = PIL.Image.new(mode="RGB", size=(200, 400), color = (250, 250, 250))
p2 = p1.load()

def length(x, y):
    return(sqrt((x-x0)**2 + (y - y0)**2))

while t <= 10:
    l = length(x, y)
    x  += vx*dt + ax*dt*dt/2
    y  += vy*dt + ay*dt*dt/2
    ax += (k*(l - l0)/100*(50-x)/l)/m
    ay += (k*(l - l0)/100*(0-y)/l + m*g)/m
    vx += ax*dt
    vy += ay*dt
    
    if floor(x)<200 and floor(y)<200 and floor(x)>0 and floor(y)>0:
        p2[floor(x), floor(y)] = (0, 0, 0)
    t += dt


p1.show()
