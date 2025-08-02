from pyfirmata import Arduino
from PID import PID
from math import sqrt
from time import time
from sys import exit
import numpy as np
from multiprocessing import shared_memory
from numpy import ndarray, float64

# general setup
# input from target.py
t2tDataSource = shared_memory.SharedMemory(name='t2t')
# output to graph.py
t2gMemory = shared_memory.SharedMemory(create=True, size=16, name='t2g')
t2gData = np.ndarray((2,), dtype=np.float64, buffer=t2gMemory.buf)

# arduino setup
# b = Arduino('COM4')


# controller setup
x_controller = PID()
y_controller = PID()
r_controller = PID()
countdown = False
countdownTime = time()

def rotation_control_check():
    # return 
    return 0

def rotation_control():
    # read in imu data
    # fin control
    pass

def target_control():
    global countdown
    global countdownTime
    try:
        target = ndarray((2,), dtype=float64, buffer=t2tDataSource.buf)
    except:
        pass
    if(not countdown):
        if(sqrt(target[0]**2 + target[1]**2) > 120):
            print("countdown set")
            countdownTime = time()
            countdown = True
    else:
        if(sqrt(target[0]**2 + target[1]**2) < 120):
            countdown = False
            print("countdown reset")
    x_controller.update_target(target[0])
    y_controller.update_target(target[1])
    output_x = x_controller.calculate_output()
    otuput_y = y_controller.calculate_output()
    t2gData[0] = output_x
    t2gData[1] = otuput_y

def to_servo_target():
    pass

def rundown():
    if(countdown):
        if(time() - countdownTime > 5):
            exit("terminated, target lost for over 5 sec")

# main loop
while(1):
    #update and calculate
    rundown()
    if(rotation_control_check()):
        rotation_control()
    else:
        target_control()
    # sleep(0.01)