from PyQt5.QtWidgets import QApplication
from graph import DataDisplayWindow
from controller import PID
from physics_model import Ball
import sys

class DDW2(DataDisplayWindow):
    def __init__(self):
        super().__init__()
        self.controller = PID(kp=28, ki=1, kd=25,
                              time_step=self.time_step, maxForce=50,
                              targetMode=1)
        self.model_obj = Ball(time_step = self.time_step)
    
    def update_val(self):
        self.controller.update_target(time = self.time_data[-1])
        # Update the model
        self.controller.update_current(self.model_obj.position)
        force = self.controller.calculate_output()
        
        self.model_obj.update_acceleration(force)
        self.model_obj.update()
        
        # Update the plot data
        self.line1_val.append(self.controller.target)
        self.line2_val.append(self.model_obj.position)

    def exit_application(self):
        # Exit the application safely
        print("Exiting application...")
        self.close()


def main():
    app = QApplication(sys.argv)
    window = DDW2()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
