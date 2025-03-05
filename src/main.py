from window import Window
from line import Line
from point import Point
from cell import Cell


def main():
    win = Window(800, 600)

    cell_1 = Cell(20, 40, 20, 40, win=win, has_left_wall=False,
                  has_right_wall=False, has_top_wall=True, has_bottom_wall=True)

    cell_2 = Cell(50, 100, 50, 100, win=win, has_left_wall=True,
                  has_right_wall=True, has_top_wall=True, has_bottom_wall=True)

    cell_1.draw(fill_color="white")
    cell_2.draw(fill_color="purple")

    cell_1.draw_move(to_cell=cell_2, undo=True)

    win.wait_for_close()


main()
