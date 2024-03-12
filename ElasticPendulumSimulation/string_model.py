import matplotlib.pyplot as plt
from math import sqrt
import os
import xlsxwriter
from scipy.fft import fft
import numpy as np
import csv
from tools import show_progress

path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/temp'
os.chdir(path)
workbook = xlsxwriter.Workbook('data.xlsx')

def length(x0=0, xtemp=0, y0=0, ytemp=0):
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
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/temp'
    plt.savefig(os.path.join(path, f'p{name}model.png'))
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

def writedata2(motion_initial, R):
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/datasetforregression'
    with open(os.path.join(path, "EPSdata.csv"), 'w', newline='') as file:
        writer = csv.writer(file)
        x,y,x_d,y_d,k,m = motion_initial[0], motion_initial[1], motion_initial[2], motion_initial[3], motion_initial[4], motion_initial[5]
        K = m*(x_d**2 + y_d**2)/2
        U = k*(length(xtemp=x,ytemp=y)**2)/2
        E = K+U
        writer.writerow([x, y, x_d, y_d, k, m, K, U, E, R])
    return

def FFT_image(name, fftx, ffty):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    fre = []
    for i in range(len(fftx)):
        fre.append(i/60)

    ax1.plot(fre, fftx)
    ax2.plot(fre, ffty)
    ax1.axis([0, 10, 0, 1000])
    ax2.axis([0, 10, 0, 1000])
    ax1.title.set_text('FFT X')
    ax2.title.set_text('FFT Y')
    fig.suptitle(f'FFT OF {name}')
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/temp'
    plt.savefig(os.path.join(path, f'FFT{name}model.png'))
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
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/temp'
    plt.savefig(os.path.join(path, f'final{name}.png'))
    plt.close()

def chaosindex(fx, fy):
    idx = 0.
    for i in range(1, len(fx)-2, 1):
        if fx[i]>fx[i-1] and fx[i]>fx[i+1] and fx[i]<50:
            idx += 0.001
        if fx[i]>50 or fy[i]>50:
            idx += 1
    return idx

def G2(motion,t,basicvaribles):
    x, y, x_d, y_d  = motion[0], motion[1], motion[2], motion[3]
    l0, k, m, g = basicvaribles[0], basicvaribles[1], basicvaribles[2], basicvaribles[3]
    l = length(0, x, 0, y)
    try:
        x_dd = k*(l-l0)*(0-x)/l/m
    except:
        x_dd = 0
    try:
        y_dd = k*(l-l0)*(0-y)/l/m + g
    except:
        y_dd = 0
    return np.array([x_d, y_d, x_dd, y_dd])

def RK4step(motion, t, dt, basicvaribles):
    k1 = np.array(G2(motion, t, basicvaribles))
    k2 = np.array(G2(motion+k1*dt/2, t+dt/2, basicvaribles))
    k3 = np.array(G2(motion+k2*dt/2, t+dt/2, basicvaribles))
    k4 = np.array(G2(motion+k3*dt, t+dt, basicvaribles))
    temp = motion + (k1 + 2*k2 + 2*k3 + k4)*dt/6
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
        t += dt
        show_progress(progress=(int(t)/60))

    fftx = [abs(i) for i in fft([coor[1] for coor in coordinates])]
    ffty = [abs(i) for i in fft([coor[2] for coor in coordinates])]
    
    name = f'({inx},{iny})'
    #writedata(name, coordinates, fftrawdataX, fftrawdataY)
    #path_image(name, [coor[1] for coor in coordinates], [coor[2] for coor in coordinates])
    FFT_image(name, fftx, ffty)
    #full_image(name, xcoor, ycoor, fftx, ffty)
    return chaosindex(fftx, ffty)
    
def simulate2(inx, iny, k=27.84, m=0.5, vx=0.0, vy=0.0):
    dt = 0.0005   #s
    motion = [0.01*inx, 0.01*iny, vx, vy]  #2SI
    motion_initial = [0.01*inx, 0.01*iny, vx, vy, k, m]
    basicvaribles = [0.15, k, m, 9.8]
    t = 0  #s
    coordinates = []

    while t < 20.000:
        motion = RK4step(motion, t, dt, basicvaribles)
        coordinates.append([t,motion[0], motion[1]])
        t += dt
        show_progress(progress=(int(t)/60))
    #coordinates.pop(0)

    fftx = [abs(i) for i in fft([coor[1] for coor in coordinates])]
    ffty = [abs(i) for i in fft([coor[2] for coor in coordinates])]

    name = f"({inx},{iny})_s2"

    R = chaosindex(fftx, ffty)
    writedata2(motion_initial, R)
    #writedata(name, coordinates, fftx, ffty)
    #path_image(name, [coor[1] for coor in coordinates], [coor[2] for coor in coordinates])
    #FFT_image(name, fftx, ffty)
    #full_image(name, xcoor, ycoor, fftx, ffty)  

def main():
    finalcaosidx = [[],[],[]]
    margin = 20
    for i in range(margin, 100+1, margin):
        for j in range(margin, 100+1, margin):
            caosidx = simulate2(inx=i, iny=j)
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

#main()
#print(simulate(inx=0, iny=10, k=20))
#main()
#final_3dimage([[1,2],[1,2],[1,2]])
#simulate(inx=0, iny=20, k=20)
simulate2(0, 5)
    
