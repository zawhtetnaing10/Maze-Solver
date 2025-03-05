from line import Line
from tkinter import Canvas
from point import Point
from window import Window
from constants import CELL_COLOR
from constants import BACKGROUND_COLOR


class Cell:
    def __init__(self, x1, x2, y1, y2, win: Window = None,  has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self, fill_color):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        left_wall = Line(top_left, bottom_left)
        top_wall = Line(top_left, top_right)
        right_wall = Line(top_right, bottom_right)
        bottom_wall = Line(bottom_left, bottom_right)

        if self.has_left_wall and self._win is not None:
            left_wall.draw(canvas=self._win.canvas, fill_color=fill_color)
        elif not self.has_left_wall and self._win is not None:
            left_wall.draw(canvas=self._win.canvas,
                           fill_color=BACKGROUND_COLOR)

        if self.has_top_wall and self._win is not None:
            top_wall.draw(canvas=self._win.canvas, fill_color=fill_color)
        elif not self.has_top_wall and self._win is not None:
            top_wall.draw(canvas=self._win.canvas, fill_color=BACKGROUND_COLOR)

        if self.has_bottom_wall and self._win is not None:
            bottom_wall.draw(canvas=self._win.canvas, fill_color=fill_color)
        elif not self.has_bottom_wall and self._win is not None:
            bottom_wall.draw(canvas=self._win.canvas,
                             fill_color=BACKGROUND_COLOR)

        if self.has_right_wall and self._win is not None:
            right_wall.draw(canvas=self._win.canvas, fill_color=fill_color)
        elif not self.has_right_wall and self._win is not None:
            right_wall.draw(canvas=self._win.canvas,
                            fill_color=BACKGROUND_COLOR)

    def draw_move(self, to_cell, undo=False):
        center_x = self._x1 + (self._x2 - self._x1) / 2
        center_y = self._y1 + (self._y2 - self._y1) / 2
        center = Point(center_x, center_y)

        to_cell_center_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2
        to_cell_center_y = to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2
        to_cell_center = Point(to_cell_center_x, to_cell_center_y)

        color = "gray" if undo else "red"

        line = Line(center, to_cell_center)
        if self._win is not None:
            line.draw(canvas=self._win.canvas, fill_color=color)
