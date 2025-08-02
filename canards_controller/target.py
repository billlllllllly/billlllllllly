import tkinter as tk
from multiprocessing import shared_memory
import numpy as np

class MouseTracker:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.create_line(250, 50, 250, 450, fill="black")
        self.canvas.create_line(50, 250, 450, 250, fill="black")
        self.canvas.create_rectangle(200, 200, 300, 300, outline="red")
        self.canvas.create_rectangle(150, 150, 350, 350, outline="black")

        self.canvas.pack()
        root.resizable(False, False)

        self.mouse_x = None
        self.mouse_y = None
        self.is_inside_canvas = False

        self.canvas.bind("<Enter>", self.on_enter)
        self.canvas.bind("<Leave>", self.on_leave)
        self.canvas.bind("<Motion>", self.on_motion)

        self.t2tMemory = shared_memory.SharedMemory(create=True, size=16, name='t2t')
        self.t2tData = np.ndarray((2,), dtype=np.float64, buffer=self.t2tMemory.buf)

        self.poll_mouse()

    def on_enter(self, event):
        self.is_inside_canvas = True

    def on_leave(self, event):
        self.is_inside_canvas = False

    def on_motion(self, event):
        self.mouse_x, self.mouse_y = event.x, event.y

    def poll_mouse(self):
        if (
            self.is_inside_canvas and self.mouse_x is not None
            and 150 <= self.mouse_x <= 350
            and 150 <= self.mouse_y <= 350
        ):
            x = self.mouse_x - 250
            y = (self.mouse_y - 250)*-1
            self.t2tData[0] = x
            self.t2tData[1] = y
            print("send: ", self.t2tData)
        self.root.after(10, self.poll_mouse)

root = tk.Tk()
tracker = MouseTracker(root)
root.mainloop()
    