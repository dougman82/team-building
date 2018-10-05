import unittest
from collections import namedtuple

# bad naming convention on hackerrank
def surfaceArea(A):
    running_total = 0
    Square = namedtuple('Square', ['x', 'y'])

    for x, row in enumerate(A):
        for y, square_height in enumerate(row):
            # add 1 unit each for top and bottom
            running_total += 2
            this_square = Square(x, y)

            # find surrounding squares with
            # FUNCTION OVERKILL!!!!
            def north_adjacent(square):
                max_x = len(A) - 1
                if square.x + 1> max_x:
                    return None
                else:
                    return Square(square.x + 1, square.y)

            def east_adjacent(square):
                max_y = len(A[0]) - 1
                if square.y + 1 > max_y:
                    return None
                else:
                    return Square(square.x, square.y + 1)

            def south_adjacent(square):
                if square.x - 1 < 0:
                    return None
                else:
                    return Square(square.x - 1, square.y)

            def west_adjacent(square):
                if square.y - 1 < 0:
                    return None
                else:
                    return Square(square.x, square.y - 1)

            def num_visible_squares(square, adjacent_square):
                if square_height(square) - square_height(adjacent_square) > 0:
                    return square_height(square) - square_height(adjacent_square)
                else:
                    return 0

            def square_height(square):
                if square:
                    return A[square.x][square.y]
                else:
                    return 0

            running_total += num_visible_squares(this_square, west_adjacent(this_square))

            running_total += num_visible_squares(this_square, east_adjacent(this_square))

            running_total += num_visible_squares(this_square, north_adjacent(this_square))

            running_total += num_visible_squares(this_square, south_adjacent(this_square))

    return running_total


class TestSurfaceArea(unittest.TestCase):
    def test_surface_area_1(self):
        self.assertEqual(6, surfaceArea([[1]]))

    def test_surface_area_2(self):
        self.assertEqual(60, surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))


if __name__ == '__main__':
    unittest.main()
