import unittest
from maze import Maze
from cell import Cell


class TestTests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_maze_create_cells_two(self):
        num_cols = 55
        num_rows = 20

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 55
        num_rows = 20

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze._break_entrance_and_exit()

        entrance_cell: Cell = maze._cells[0][0]
        exit_cell: Cell = maze._cells[num_cols - 1][num_rows - 1]

        self.assertEqual(entrance_cell.has_top_wall, False)
        self.assertEqual(exit_cell.has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()
