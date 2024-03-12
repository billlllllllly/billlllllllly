import random
import time
from math import floor

def show_progress(progress, cc=1, spinner = 0):
    p = floor(progress*20)
    if p <= 8:
        print('[', end='')
        for i in range(p):
            print('#', end='')
        for i in range(8-p):
            print('-', end='')

        print('\033[%dm%03d' % (random.randint(91, 96) if cc == 1 else 93, (progress*100)), end='%\033[0m')
        print('--------]', end='')
    else:
        print('[########', end='')
        print('\033[%dm%03d' % (random.randint(91, 96) if cc == 1 else 93, (progress*100)), end='%\033[0m')
        i=0
        while i in range(p-12):
            print('#', end='')
            i+=1
        while i in range(8):
            print('-', end='')
            i+=1
        print(']', end='')

    if spinner == 1:
        s = int(progress*100) % 9
        if s <= 3:
            print('  /', end = '')
        elif s <= 5:
            print('  -', end = '')
        else:
            print('  \\', end = '')

    if progress == 1:
        print("\r[########100%########]    \033[93mDONE!\033[0m  \n ")
    else:
        print('', end = '\r')
    return

def test(cc):
    for i in range(100+1):
        time.sleep(0.03)
        show_progress(progress=(i/100), cc=cc, spinner=1)




#print('y' if 1>2 else "n")