import unittest
from collections import namedtuple

# bad naming convention on hackerrank
def surfaceArea(A):
    running_total = 0
    max_x = len(A) - 1
    max_y = len(A[0]) - 1
    Square = namedtuple('Square', ['x', 'y'])

    for x, row in enumerate(A):
        for y, square_height in enumerate(row):
            # add 1 unit each for top and bottom
            running_total += 2

            # find surrounding squares
            square_to_the_left = Square(x, y - 1)
            square_to_the_right = Square(x, y + 1)
            square_to_the_up = Square(x + 1, y)
            square_to_the_down = Square(x - 1, y)

            if square_to_the_left.y < 0:
                running_total += square_height
            else:
                if square_height - A[square_to_the_left.x][square_to_the_left.y] > 0:
                    running_total += square_height - A[square_to_the_left.x][square_to_the_left.y]

            if square_to_the_right.y > max_y:
                running_total += square_height
            else:
                if square_height - A[square_to_the_right.x][square_to_the_right.y] > 0:
                    running_total += square_height - A[square_to_the_right.x][square_to_the_right.y]

            if square_to_the_up.x > max_x:
                running_total += square_height
            else:
                if square_height - A[square_to_the_up.x][square_to_the_up.y] > 0:
                    running_total += square_height - A[square_to_the_up.x][square_to_the_up.y]

            if square_to_the_down.x < 0:
                running_total += square_height
            else:
                if square_height - A[square_to_the_down.x][square_to_the_down.y] > 0:
                    running_total += square_height - A[square_to_the_down.x][square_to_the_down.y]

    return running_total


class TestSurfaceArea(unittest.TestCase):
    def test_surface_area_1(self):
        self.assertEqual(6, surfaceArea([[1]]))

    def test_surface_area_2(self):
        self.assertEqual(60, surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))


if __name__ == '__main__':
    unittest.main()
