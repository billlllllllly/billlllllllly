from math import floor

#fitness func
def method1(p):
    fitness = 0
    for j in range(len(p)):
        if j % 2 == 0:
            fitness += p[j]
        else:
            fitness -= p[j]
    return fitness

def method3():
    return

def method2(p):
    fitness = sum(p)
    return fitness

#tools
def normolization(r):
    r_normolized = []
    for i in r:
        if max(r) != min(r):
            i_normolized = (i - min(r)) / (max(r) - min(r))
        else:
            i_normolized = 1
        r_normolized.append(i_normolized)
    return r_normolized

def show_progress(progress):
    p = floor(progress*20)
    if p <= 8:
        print('[', end='')
        for i in range(p):
            print('#', end='')
        for i in range(8-p):
            print('-', end='')
        print('\033[93m%03d' % (progress*100), end='%\033[0m')
        print('--------]', end='')
    else:
        print('[########', end='')
        print('\033[93m%03d' % (progress*100), end='%\033[0m')
        i=0
        while i in range(p-12):
            print('#', end='')
            i+=1
        while i in range(8):
            print('-', end='')
            i+=1
        print(']', end='')

    if progress == 1:
        print("\033[93m    DONE!  \033[0m \n ")
    else:
        print('', end = '\r')
    return