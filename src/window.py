from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver"

        self.canvas = Canvas(bg="white")
        self.canvas.pack()

        self.window_is_running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()

    def close(self):
        self.window_is_running = False

    def draw_line(self, line: Line, fill_color):
        line.draw(canvas=self.canvas, fill_color=fill_color)
