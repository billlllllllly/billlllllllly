import matplotlib.pyplot as plt
from math import sqrt
import os
import xlsxwriter
from scipy.fft import fft
import numpy as np

path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/test'
os.chdir(path)
workbook = xlsxwriter.Workbook('data.xlsx')

def length(x0, xtemp, y0, ytemp):
    temp = sqrt((xtemp-x0)**2 + (ytemp - y0)**2)
    return(temp)

def path_image(name, xcoor, ycoor):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)

    ax1.plot(xcoor, ycoor)
    xmin, xmax, ymin, ymax = ax1.axis()
    ax1.axis([xmin, xmax, ymax, ymin])

    ax2.plot(xcoor, ycoor)
    ax2.axis([-1, 1, 1.5, -0.5])

    if ymin < 0:
        fig.suptitle('ERROR OOR',color='red',fontsize=30)
    else:
        fig.suptitle('  ',fontsize=30)
    fig.tight_layout()
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/simulation2/path_image'
    os.chdir(path)
    plt.savefig(f'p{name}model.png')
    plt.close()

def writedata(name, coordinates, fftrawdataX, fftrawdataY):
    worksheet = workbook.add_worksheet(f'example{name}')
    worksheet.write('A1', 'time')
    worksheet.write('B1', 'displacement of X axis')
    worksheet.write('C1', 'displacement of Y axis')
    worksheet.write('D1', 'raw FFT of X')
    worksheet.write('E1', 'raw FFt of Y')
    worksheet.write('F1', 'FFT of X')
    worksheet.write('G1', 'FFT of Y')

    row = 1
    col = 0
    for c in coordinates:
        #print(c)
        worksheet.write(row, col, c[0])
        worksheet.write(row, col + 1, c[1])
        worksheet.write(row, col + 2, c[2])
        row += 1
    
    worksheet.write_column('D2', fftrawdataX)
    worksheet.write_column('E2', fftrawdataY)
    
    worksheet.write_dynamic_array_formula('F2:F6000', '=ABS(D1:D6000)')
    worksheet.write_dynamic_array_formula('G2:G6000', '=ABS(E1:E6000)')

def FFT_image(name, fftx, ffty):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    fre = []
    for i in range(6000):
        fre.append(i/60)
    ax1.plot(fre, fftx)
    ax2.plot(fre, ffty)
    ax1.axis([0, 10, 0, 100])
    ax2.axis([0, 10, 0, 100])
    ax1.title.set_text('FFT X')
    ax2.title.set_text('FFT Y')
    fig.suptitle(f'FFT OF {name}')
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/test'
    os.chdir(path)
    plt.savefig(f'FFT{name}model.png')
    plt.close()

def final_3dimage(idx, name):
    x,y,z = np.array(idx[0]), np.array(idx[1]), np.array(idx[2])
    '''
    xlin = np.linspace(min(x), max(x), 100)
    ylin = np.linspace(min(y), max(y), 100)
    [X,Y] = np.meshgrid(xlin, ylin)
    Z = griddata(x,y,z,X,Y,'v4')
    '''
    fig = plt.axes(projection='3d')
    fig.set_xlabel('X axis')
    fig.set_ylabel('Y axis')
    fig.set_zlabel('chaos idx')
    fig.set_zlim3d(0,50)
    #fig.set_title(f'k = {name}', size = 30)
    fig.plot_trisurf(x, y, z, cmap=plt.cm.CMRmap)
    #fig.contourf(x,y,z,zdir='z',offset=-10, camp=plt.cm.CMRmap)
    plt.tight_layout()
    plt.savefig(f'final{name}.png')
    #plt.show()
    plt.close()

def caosindex(fx, fy):
    idx = 0.
    for i in range(1, len(fx)-2, 1):
        if fx[i]>fx[i-1] and fx[i]>fx[i+1] and fx[i]<50:
            idx += 0.001
        if fx[i]>50 or fy[i]>50:
            idx += 1
    return idx

def G2(motion,t,basicvaribles):
    x_d, y_d, x, y  = motion[0], motion[1], motion[2], motion[3]
    l0, k, m, g = basicvaribles[0], basicvaribles[1], basicvaribles[2], basicvaribles[3]
    l = length(0, x, 0, y)
    x_dd = k*(l-l0)*(0-x)/l/m
    y_dd = k*(l-l0)*(0-y)/l/m + g
    return np.array([x_dd, y_dd, x_d, y_d])

def RK4step(motion, t, dt, basicvaribles):
    k1 = np.array(G2(motion,t, basicvaribles))
    k2 = np.array(G2(motion+k1*dt/2, t+dt/2, basicvaribles))
    k3 = np.array(G2(motion+k2*dt/2, t+dt/2, basicvaribles))
    k4 = np.array(G2(motion+k3*dt, t+dt, basicvaribles))
    temp = (k1 + 2*k2 + 2*k3 + k4)*dt/6
    return temp

def full_image(name, xcoor, ycoor, fftx, ffty):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,4,1)
    ax2 = fig.add_subplot(1,4,2)
    ax3 = fig.add_subplot(1,4,3)
    ax4 = fig.add_subplot(1,4,4)

    ax1.plot(xcoor, ycoor)
    xmin, xmax, ymin, ymax = ax1.axis()
    ax1.axis([xmin, xmax, ymax, ymin])
    ax2.plot(xcoor, ycoor)
    ax2.axis([-1, 1, 1.5, -0.5])
    if ymin < 0:
        ax2.title.set_text('ERROR OOR',color='red',fontsize=30)
    else:
        fig.suptitle('  ',fontsize=30)
    
    fre = []
    for i in range(6000):
        fre.append(i/60)
    ax3.plot(fre, fftx)
    ax4.plot(fre, ffty)
    ax3.axis([0, 10, 0, 200])
    ax4.axis([0, 10, 0, 200])
    ax3.title.set_text('FFT X')
    ax4.title.set_text('FFT Y')
    fig.suptitle(f'release point: {name}')
    fig.tight_layout()

    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/simulation2/allinone'
    os.chdir(path)
    plt.savefig(f'model{name}.png')
    plt.close()

def simulate(inx, iny, k=27.84, m=0.5, vx=0.0, vy=0.0):
    dt = 0.0001   #s
    x = 0.01*inx #cm2m
    y = 0.01*iny #cm2m
    g = 9.8 #m/s2
    l0 = 0.15 #m
    ax = 0.0 #m/s2
    ay = 0.0 #m/s2
    t = 0.0  #s
    coordinates = []
    xcoor = []
    ycoor = []

    while t <= 60:
        l = length(0, x, 0, y)
        x += vx*dt + ax*dt*dt/2
        y += vy*dt + ay*dt*dt/2
        ax = (k*(l-l0)*(0-x)/l)/m
        ay = (k*(l-l0)*(0-y)/l + m*g)/m
        vx += ax*dt
        vy += ay*dt
        if (int(t*10000))%100 == 0:
            coordinates.append([t,x, y])
            xcoor.append(x)
            ycoor.append(y)
        t += dt

    fftrawdataX = fft(xcoor)
    fftrawdataY = fft(ycoor)
    fftx = []
    ffty = []
    
    for k in fftrawdataX:
        fftx.append(abs(k.real))
    for k in fftrawdataY:
        ffty.append(abs(k.real))
    
    name = f'({inx},{iny})'
    #writedata(name, coordinates, fftrawdataX, fftrawdataY)
    #path_image(name, xcoor, ycoor)
    FFT_image(name, fftx, ffty)
    #full_image(name, xcoor, ycoor, fftx, ffty)
    return caosindex(fftx, ffty)
    
def simulate2(inx, iny, k=27.84, m=0.5, vx=0.0, vy=0.0):
    dt = 0.0001   #s
    motion = [vx, vy, 0.01*inx, 0.01*iny]  #2SI
    basicvaribles = [0.15, k, m, 9.8]
    t = 0.0  #s
    coordinates = []
    xcoor = []
    ycoor = []

    while t <= 60:
        motion = RK4step(motion, t, dt, basicvaribles)
        if (int(t*10000))%100 == 0:
            coordinates.append([t,motion[2], motion[3]])
            xcoor.append(motion[2])
            ycoor.append(motion[3])
        t += dt
    
    fftx = fft(xcoor)
    ffty = fft(ycoor)
    

def main():
    finalcaosidx = [[],[],[]]
    margin = 20
    for i in range(margin, 100+1, margin):
        for j in range(margin, 100+1, margin):
            caosidx = simulate(inx=i, iny=j)
            finalcaosidx[0].append(i)
            finalcaosidx[1].append(j)
            finalcaosidx[2].append(caosidx)
            print('                     ', end='\r')
            print(f" ({i},{j})", end='\r')

    name = ' '
    final_3dimage(finalcaosidx, name)
    print('                      ', end='\r')
    print(f"{name} --end-- ")
    #f1(10, 50)
    #print("1")
    #workbook.close()

#print(simulate(inx=0, iny=10, k=20))
#main()

#final_3dimage([[1,2],[1,2],[1,2]])
#simulate(inx=0, iny=20, k=20)
    
