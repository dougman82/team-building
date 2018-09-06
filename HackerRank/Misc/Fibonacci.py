# Author: Samuel Vange
import unittest
import timeit


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_dp(n):
    return fib_dp_helper(n, {})


def fib_dp_helper(n, memo):
    if n <= 2:
        return 1

    if memo.get(n - 1):
        fib_n1 = memo[n - 1]
    else:
        fib_n1 = fib_dp_helper(n - 1, memo)
        memo[n - 1] = fib_n1

    if memo.get(n - 2):
        fib_n2 = memo[n - 2]
    else:
        fib_n2 = fib_dp_helper(n - 2, memo)
        memo[n - 2] = fib_n2

    return fib_n1 + fib_n2


class TestFib(unittest.TestCase):
    def test_fib_dp(self):
        start = timeit.timeit()
        self.assertEqual(fib_dp(29), 514229)
        end = timeit.timeit()
        print end - start

    def test_fib(self):
        start = timeit.timeit()
        self.assertEqual(fib(29), 514229)
        end = timeit.timeit()
        print end - start


if __name__ == '__main__':
    unittest.main()