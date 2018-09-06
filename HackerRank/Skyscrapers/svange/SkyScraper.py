import functools
import unittest
from collections import defaultdict


# This is a cool recursive solution, but has a running time of n * k
# for n = the size of the buildings array
# and k = the number of different building heights.
def solve(arr):
    if len(arr) <= 1:
        return 0

    tallest = max(arr)
    num_tallest = arr.count(tallest)

    tallest_paths = num_tallest * (num_tallest - 1)

    splits = [i for i, x in enumerate(arr) if x == tallest]

    sub_problems = []
    current = 0
    for split in splits:
        sub_problems.append(arr[current:split])
        current = split + 1
    if current == len(arr) + 1:
        sub_problems.append(arr[current::])

    sub_problem_answers = map(solve, sub_problems)
    sum_sub_problem_answers = functools.reduce(lambda x, y: x + y, sub_problem_answers)

    return int(tallest_paths + sum_sub_problem_answers)


# This solution uses a stack and a hash table to reduce the running time to 2n
# for n = the size of the building array
def solve_stack(arr):
    if len(arr) <= 1:
        return 0
    stack = []

    num_paths = 0

    for next_building in arr:
        # Special case where nothing is on the stack
        if len(stack) == 0:
            stack.append(next_building)
            continue

        # If the next building is taller than the last building, pop things off the stack until the building
        # at the top of the stack is taller than the next building
        # While doing this, use a hash table to count how many occurences of any building height seen
        # for a building k seen n times, add n * (n - 1) to the total number of paths
        if next_building > stack[-1]:
            # Default dictionary where each value is initialized to 0
            seen = defaultdict(lambda: 0)
            while next_building > stack[-1]:
                seen[stack.pop()] += 1
                if len(stack) == 0:
                    break
            for building in seen.keys():
                if seen[building] > 1:
                    num_paths += seen[building] * (seen[building] - 1)
            stack.append(next_building)
        # If the next building is smaller than or equal in height to the next building, push it onto the stack.
        else:
            stack.append(next_building)

    # Clean up any remaining stack
    if stack:
        seen = defaultdict(lambda: 0)
        while stack:
            seen[stack.pop()] += 1
        for building in seen.keys():
            if seen[building] > 1:
                num_paths += seen[building] * (seen[building] - 1)
    return num_paths



class TestSolution(unittest.TestCase):
    def skip_test_solve(self):
        self.assertEqual(solve([1, 2, 3]), 0)
        self.assertEqual(solve([3, 2, 1]), 0)
        self.assertEqual(solve([1, 1, 1, 2, 2]), 8)
        self.assertEqual(solve([3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3]), 14)

    def test_solve_stack(self):
        self.assertEqual(solve_stack([1, 2, 3]), 0)
        self.assertEqual(solve_stack([3, 2, 1]), 0)
        self.assertEqual(solve_stack([1, 1, 1, 2, 2]), 8)
        self.assertEqual(solve_stack([3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3]), 14)


if __name__ == '__main__':
    unittest.main()
