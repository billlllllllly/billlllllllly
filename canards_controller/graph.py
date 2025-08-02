import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from multiprocessing import shared_memory
from numpy import ndarray, float64

class DataDisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Display")
        self.setFixedSize(1200, 750)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Create button layout
        button_layout = QHBoxLayout()
        
        # Create Stop button
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_simulation)
        button_layout.addWidget(self.stop_button)
        
        # Create Exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit_application)
        button_layout.addWidget(self.exit_button)
        
        # Add button layout to main layout
        layout.addLayout(button_layout)

        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Val')
        self.ax.set_ylim(-15, 15)
        self.line, = self.ax.plot([], [], 'b-')
        self.line2, = self.ax.plot([], [], 'r-')

        self.time_data = []
        self.line1_val = [0.0]
        self.line2_val = [0.0]
        self.current_time = 0
        self.time_step = 1/100
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000 // 100)
        
        # connection
        self.t2gDataSource = shared_memory.SharedMemory(name='t2g')

        # Track if simulation is running
        self.simulation_running = True

    def stop_simulation(self):
        """Stop or resume the simulation"""
        if self.simulation_running:
            self.timer.stop()
            self.stop_button.setText("Resume")
            self.simulation_running = False
        else:
            self.timer.start(1000 // 100)
            self.stop_button.setText("Stop")
            self.simulation_running = True

    def exit_application(self):
        """Exit the application safely"""
        print("Exiting application...")
        self.close()

    def update_plot(self):
        self.time_data.append(self.current_time)
        self.update_val()

        window_size = 10
        # Ensure all lists are the same length
        while (self.time_data and len(self.time_data) > window_size and
               self.time_data[-1] - self.time_data[0] > window_size):
            self.time_data.pop(0)
            if self.line1_val:
                self.line1_val.pop(0)
            if self.line2_val:
                self.line2_val.pop(0)

        # Only plot if all lists are the same length
        min_len = min(len(self.time_data), len(self.line1_val), len(self.line2_val))
        self.line.set_data(self.time_data[-min_len:], self.line1_val[-min_len:])
        self.line2.set_data(self.time_data[-min_len:], self.line2_val[-min_len:])
        self.ax.set_xlim(self.current_time - window_size, self.current_time)
        self.canvas.draw()
        self.current_time += self.time_step
    
    def update_val(self):
        # update line val (append)
        data = ndarray((2,), dtype=float64, buffer=self.t2gDataSource.buf)
        self.line1_val.append(data[0])
        self.line2_val.append(data[1])
        print(data)
        

def runGraph():
    app = QApplication(sys.argv)
    window = DataDisplayWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    runGraph() 