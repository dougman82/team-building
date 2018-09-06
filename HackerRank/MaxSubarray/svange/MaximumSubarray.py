import unittest


def maximum_subarray(arr):
    memo = {}
    return maximum_subarray_helper(arr, memo)


def maximum_subarray_helper(arr, memo):
    if memo[arr[:-1]]:
        sub_problem_solution = memo[arr[:-1]]
    else:
        sub_problem_solution = maximum_subarray_helper(arr[:-1], memo)

    





class TestMaximumSubarray(unittest.TestCase):
    def test_problem_1(self):
        self.assertEqual(maximum_subarray([1, 2, 3, 4]), (10, 10))

    def test_problem_2(self):
        self.assertEqual(maximum_subarray([2, -1, 2, 3, 4, -5]), (10, 11))


if __name__ == '__main__':
    unittest.main()
