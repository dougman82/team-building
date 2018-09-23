import functools, itertools, unittest


# Helper function to generate small solution sets
# Too inefficient, but useful
def bonetrousle_naive(n, k, b):
    return (list(tup)[::-1] for tup in itertools.combinations(range(k, 0, -1), b) if functools.reduce(lambda x, y: x + y, tup) == n)


def bonetrousle(n, k, b):
    # A solution is only possible if n is between the smallest and largest possible solutions
    max_possible = sum(range(k - (b - 1), k + 1))
    min_possible = sum(range(1, b + 1))
    if not min_possible <= n <= max_possible:
        return [-1]

    # Start with the smallest possible solution
    solution = list(range(1, b + 1))

    # We'll divide our target number to distribute over our solution
    min_to_add = (n - min_possible) // b
    solution = list(map(lambda x: x + min_to_add, solution))

    # Distribute remainder
    remainder = (n - min_possible) % b
    solution = [num + 1 if index < remainder else num for index, num in enumerate(solution[::-1])][::-1] # too many slices, cleanup
    return solution


class TestBonetrousle(unittest.TestCase):
    def skip_test_bonetrousle_naive(self):
        actual = [[1, 3, 8], [1, 4, 7], [2, 3, 7], [1, 5, 6], [2, 4, 6], [3, 4, 5]]
        solutions = list(bonetrousle_naive(12, 8, 3)) or [[-1]]

        self.assertEqual(solutions, actual)
        self.assertEqual(list(bonetrousle_naive(10, 3, 3)), [])

    def test_bonetrousle(self):
        self.assertIn(bonetrousle(12, 8, 3), list(bonetrousle_naive(12, 8, 3)) or [[-1]])
        self.assertIn(bonetrousle(10, 3, 3), list(bonetrousle_naive(10, 3, 3)) or [[-1]])


if __name__ == '__main__':
    unittest.main()
