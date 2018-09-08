import itertools
import unittest
from typing import List
from collections import defaultdict
from collections import deque


def journey_to_the_moon(n: int, astronaut: List[List[int]]):
    # Construct the graph
    # Create an adj list
    adj_list = []
    for i in range(n):
        # Each astronaut needs an empty list of neighbors
        # Use a set to eliminate duplicate entries
        adj_list.append(set())

    for pair in astronaut:
        # Each astronaut in each incoming astronaut pair is a neighbor of the other in that pair
        a1, a2 = tuple(pair)
        adj_list[a1].add(a2)
        adj_list[a2].add(a1)

    # Make the sets lists for ease of programming
    adj_list = list(map(lambda x: list(x), adj_list))

    # Get a table of connected components using BFS on each unvisited node
    connected_components = {}
    component = 0
    for node, neighbors in enumerate(adj_list):
        q = deque()
        visited = set()
        q.append(node)
        while q:
            current = q.popleft()
            if current in visited:
                continue
            visited.add(current)
            connected_components[current] = component
            q.extend(adj_list[current])
        component += 1

    # Invert the list so we have a table of the form:
    # cc1: count1
    # cc2: count2
    # ...
    connected_components = connected_components.items()
    cc_table = defaultdict(lambda: 0)
    for astro, cc in connected_components:
        cc_table[cc] += 1
    combos = itertools.combinations(cc_table.keys(), 2)

    # Calculate result
    # Find each pair of connected components and add the product of their counts to the total solution count
    solution = 0
    for c in combos:
        solution += cc_table[c[0]] * cc_table[c[1]]
    return solution


class TestJourneyToTheMoon(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(journey_to_the_moon(5, [[0, 1], [3, 2], [3, 4]]), 6)


if __name__ == '__main__':
    unittest.main()
