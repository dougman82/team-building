import functools, itertools, unittest


# Helper function to generate small solution sets
# Too inefficient, but useful
def bonetrousle_naive(n, k, b):
    return (list(tup)[::-1] for tup in itertools.combinations(range(k, 0, -1), b) if functools.reduce(lambda x, y: x + y, tup) == n)


def bonetrousle(n, k, b):
    pass


class TestBonetrousle(unittest.TestCase):
    def test_bonetrousle_naive(self):
        actual = [[1, 3, 8], [1, 4, 7], [1, 5, 6], [2, 3, 7], [2, 4, 6], [3, 4, 5]]
        solution = list(bonetrousle_naive(12, 8, 3))
        actual.sort()
        solution.sort()
        self.assertEqual(solution, actual)
        self.assertEqual(list(bonetrousle_naive(10, 3, 3)), [])

    def test_bonetrousle(self):
        self.assertIn(bonetrousle(12, 8, 3), list(bonetrousle_naive(12, 8, 3)))


if __name__ == '__main__':
    unittest.main()
