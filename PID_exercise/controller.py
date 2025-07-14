from physics_model import *
from math import sin
from file_manager import locker

class PID:
    def __init__(self, kp=0.05, ki=0.05, kd=0.05,
                target=0, time_step=1/100, maxForce=0,
                targetMode=1):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target = target
        self.current = 0
        self.previous_error = 0
        self.integral_error = 0
        self.time_step = time_step
        self.maxForce = maxForce
        self.targetMode = targetMode

    def error(self):
        return self.target - self.current
    
    def calculate_output(self):
        e = self.error()
        # kp
        p = self.kp * e
        # ki
        self.integral_error += e * self.time_step
        i = self.ki * self.integral_error
        # kd
        derivative = (e - self.previous_error) / self.time_step
        self.previous_error = e
        d = self.kd * derivative
        output = p+i+d
        if(self.maxForce):
            if output > self.maxForce:
                output = self.maxForce
            elif output < -1*self.maxForce:
                output = -1*self.maxForce
        return output
    
    def update_target(self, time=0):
        match self.targetMode:
            case 1:
                if (int)(time/4)%2 == 1:
                    self.target = 7.5
                else:
                    self.target = -7.5
            case 2:
                self.target = 7.5*sin(time)
            case 3:
                LOG = "target.log"
                with locker(LOG, "r") as f:
                    line = f.readlines()[0]
                    try:
                        self.target = float(line)
                    except:
                        pass

    def update_current(self, value):
        self.current = value

