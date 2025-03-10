from cell import Cell
from window import Window
from constants import CELL_COLOR
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window = None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._cells = []

        if seed is not None:
            random.seed(seed)

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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            # left
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))

            # right
            if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i + 1, j))

            # top
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))

            # bottom
            if j+1 < self.num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))

            if not to_visit:
                self._draw_cell(i, j)
                return

            coord_to_visit = random.choice(to_visit)
            to_visit_i, to_visit_j = coord_to_visit

            # left
            if to_visit_i == i - 1 and to_visit_j == j:
                self._cells[to_visit_i][to_visit_j].has_right_wall = False
                self._cells[i][j].has_left_wall = False

            # right
            if to_visit_i == i + 1 and to_visit_j == j:
                self._cells[to_visit_i][to_visit_j].has_left_wall = False
                self._cells[i][j].has_right_wall = False

            # top
            if to_visit_i == i and to_visit_j == j-1:
                self._cells[to_visit_i][to_visit_j].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False

            # bottom
            if to_visit_i == i and to_visit_j == j+1:
                self._cells[to_visit_i][to_visit_j].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False

            self._break_walls_r(to_visit_i, to_visit_j)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        neighbouring_cells = {}

        # left
        if i - 1 >= 0 and not self._cells[i-1][j].visited:
            neighbouring_cells["l"] = (i-1, j)

        # right
        if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
            neighbouring_cells["r"] = (i + 1, j)

        # top
        if j - 1 >= 0 and not self._cells[i][j-1].visited:
            neighbouring_cells["t"] = (i, j-1)

        # bottom
        if j+1 < self.num_rows and not self._cells[i][j+1].visited:
            neighbouring_cells["b"] = (i, j+1)

        for key in neighbouring_cells:
            current_cell = self._cells[i][j]
            to_cell_i, to_cell_j = neighbouring_cells[key]
            to_cell = self._cells[to_cell_i][to_cell_j]

            if key == "l":
                if not current_cell.has_left_wall and not to_cell.has_right_wall:
                    current_cell.draw_move(to_cell)
                    if self.solve_r(to_cell_i, to_cell_j):
                        return True
                    else:
                        current_cell.draw_move(to_cell, undo=True)

            if key == "r":
                if not current_cell.has_right_wall and not to_cell.has_left_wall:
                    current_cell.draw_move(to_cell)
                    if self.solve_r(to_cell_i, to_cell_j):
                        return True
                    else:
                        current_cell.draw_move(to_cell, undo=True)

            if key == "t":
                if not current_cell.has_top_wall and not to_cell.has_bottom_wall:
                    current_cell.draw_move(to_cell)
                    if self.solve_r(to_cell_i, to_cell_j):
                        return True
                    else:
                        current_cell.draw_move(to_cell, undo=True)

            if key == "b":
                if not current_cell.has_bottom_wall and not to_cell.has_top_wall:
                    current_cell.draw_move(to_cell)
                    if self.solve_r(to_cell_i, to_cell_j):
                        return True
                    else:
                        current_cell.draw_move(to_cell, undo=True)

        return False
