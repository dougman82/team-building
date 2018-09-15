
import sys

# Look for stretches of zeroes longer than 
def is_possible(invalid_gap, cities):
	#print(f"Checking for gaps of width {invalid_gap}")
	invalid_sequence = [0] * invalid_gap
	for i in range(len(cities) - invalid_gap + 1):
		if cities[i] == 0:
			if cities[i:i + invalid_gap] == invalid_sequence:
				return False
	return True


# Hop through the list (distribution - 1) cities at a time looking to place power plants
# If suitable spot is not found, hop forward and scan backward as needed
def solve(distribution, cities):

	# First check if solution exists
	smallest_invalid_gap = (2 * distribution) - 1
	if not is_possible(smallest_invalid_gap, cities):
		return -1
	else:
		return 1




if __name__ == '__main__':

	input_stream = sys.stdin

	num_cities, distribution = [int(x) for x in input_stream.readline().strip().split(" ")]
	cities = [int(x) for x in input_stream.readline().strip().split(" ")]

	print(solve(distribution, cities))