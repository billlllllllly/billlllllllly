class PID:
    def __init__(self, kp=0.15, ki=0.000007, kd=0.15,
                target=0, timeStep=1/100, maxOutput=40):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target = target
        self.current = 0
        self.previousError = 0
        self.integralError = 0
        self.timeStep = timeStep
        self.maxOutput = maxOutput

    def error(self):
        return self.target - self.current
    
    def calculate_output(self):
        e = self.error()
        # kp
        p = self.kp * e
        # ki
        if(e*self.previousError < 0):
            self.integralError = 0
        self.integralError += (e+self.previousError) * self.timeStep / 2
        i = self.ki * self.integralError
        # kd
        derivative = (e - self.previousError) / self.timeStep
        self.previousError = e
        d = self.kd * derivative
        output = p+i+d
        if(self.maxOutput):
            if output > self.maxOutput:
                output = self.maxOutput
            elif output < -1*self.maxOutput:
                output = -1*self.maxOutput
        return output
    
    def update_target(self, val):
        self.target = val

    def update_current(self, val):
        pass