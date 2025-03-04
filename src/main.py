from window import Window
from line import Line
from point import Point


def main():
    win = Window(800, 600)

    p1 = Point(20, 20)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    win.draw_line(line=line, fill_color="white")

    win.wait_for_close()


main()
