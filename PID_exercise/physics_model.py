class Ball:
    def __init__(self, position=0, velocity=0, acceleration=0, mass=1, time_step=1/100):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.time_step = time_step

    def update_acceleration(self, force):
        self.acceleration = force/self.mass

    def update(self):
        # update velocity
        self.velocity += self.acceleration * self.time_step
        # update position
        self.position += (self.velocity*self.time_step + 0.5*self.acceleration*self.time_step**2)
