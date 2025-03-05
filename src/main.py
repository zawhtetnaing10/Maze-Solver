from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 5, 5, 15, 15, win, seed=42)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()

    win.wait_for_close()


main()
