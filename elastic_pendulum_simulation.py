import matplotlib.pyplot as plt
from math import sqrt
import os
import xlsxwriter
from scipy.fft import fft

path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/simulation2'
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
    ax1.axis([0, 10, 0, 200])
    ax2.axis([0, 10, 0, 200])
    ax1.title.set_text('FFT X')
    ax2.title.set_text('FFT Y')
    fig.suptitle(f'FFT OF {name}')
    path = 'C:/Users/sunfar/Desktop/billy/for竹中/物探二/simulation2/FFT_image'
    os.chdir(path)
    plt.savefig(f'FFT{name}model.png')
    plt.close()


def f1(inx, iny):
    k = float(27.84) #N/m
    m = float(0.5) #kg
    dt = 0.0001   #s
    x0, y0 = 0,0
    x = 0.01*inx #cm2m
    y = 0.01*iny #cm
    xtemp = float(x + x0)
    ytemp = float(y + y0)
    g = 9.8 #m/s2
    l0 = 0.158 #m
    vx = 0.0 #m/s
    ax = 0.0 #m/s2
    vy = 0.0 #m/s
    ay = 0.0 #m/s2
    t = 0.0  #s
    coordinates = []
    xcoor = []
    ycoor = []

    while t <= 60:
        l = length(x0, xtemp, y0, ytemp)
        xtemp += vx*dt + ax*dt*dt/2
        ytemp += vy*dt + ay*dt*dt/2
        ax = (k*(l-l0)*(x0-xtemp)/l)/m
        ay = (k*(l-l0)*(y0-ytemp)/l + m*g)/m
        vx += ax*dt
        vy += ay*dt
        if (int(t*10000))%100 == 0:
            coordinates.append([t,xtemp, ytemp])
            xcoor.append(xtemp)
            ycoor.append(ytemp)
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
    path_image(name, xcoor, ycoor)
    FFT_image(name, fftx, ffty)



#main

for i in range(5, 100+1, 5):
    for j in range(5, 100+1, 5):
        f1(i, j)
        print('                     ', end='\r')
        print(f" ({i},{j})", end='\r')
#loop end

print('                      ', end='\r')
print(" --end-- ")

#f1(10, 50)
#print("1")

workbook.close()
