from cell import Cell
from window import Window
from constants import CELL_COLOR
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(x1=0, x2=0, y1=0, y2=0, win=self.win))
            self._cells.append(column)

        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        current_cell: Cell = self._cells[i][j]

        cell_x1 = self.x1 + (i * self.cell_size_x)
        cell_x2 = cell_x1 + self.cell_size_x

        cell_y1 = self.y1 + (j * self.cell_size_y)
        cell_y2 = cell_y1 + self.cell_size_y

        current_cell._x1 = cell_x1
        current_cell._x2 = cell_x2
        current_cell._y1 = cell_y1
        current_cell._y2 = cell_y2

        current_cell.draw(fill_color=CELL_COLOR)

        self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell: Cell = self._cells[0][0]
        exit_cell: Cell = self._cells[self.num_cols - 1][self.num_rows - 1]

        entrance_cell.has_top_wall = False
        self._cells[0][0] = entrance_cell
        self._draw_cell(0, 0)

        exit_cell.has_bottom_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1] = exit_cell
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
