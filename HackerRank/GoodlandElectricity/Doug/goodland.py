
import sys

# Look for stretches of zeroes of length:
#   1. (length invalid_end_gap) at the beginning/end of the array
#   2. (invalid_middle_gap) in the interior of the array
def is_possible(invalid_end_gap, invalid_middle_gap, cities):

	invalid_end_sequence = [0] * invalid_end_gap
	if cities[:invalid_end_gap] == invalid_end_sequence or cities[(0 - invalid_end_gap):] == invalid_end_sequence:
		return False

	invalid_middle_sequence = [0] * invalid_middle_gap
	for i in range(len(cities) - invalid_middle_gap + 1):
		if cities[i] == 0 and cities[i:i + invalid_middle_gap] == invalid_middle_sequence:
				return False
	return True


# Hop through the list (2 * distribution - 1) cities at a time looking to place power plants
# If suitable spot is not found, scan backward as needed
def solve(distribution, cities):

	# First check if solution exists, return -1 if none
	invalid_end_gap = distribution
	invalid_middle_gap = (2 * distribution) - 1
	if not is_possible(invalid_end_gap, invalid_middle_gap, cities):
		return -1
	
	# If distribution == 1, then every city must hold a power plant
	if distribution == 1:
		return len(cities)

	# Main logic loop
	scan_index = distribution - 1
	hop_width = (2 * distribution) - 1
	last_powerplant = -1
	num_powerplants = 0
	while scan_index < (len(cities)):
		if cities[scan_index] == 1:
			num_powerplants += 1
			last_powerplant = scan_index
		else:
			while cities[scan_index] != 1:
				scan_index -= 1
			if scan_index != last_powerplant:
				num_powerplants += 1
				last_powerplan = scan_index
			else:
				break
		
		print(f"Placing powerplant at index { scan_index }")
		scan_index += hop_width

	return num_powerplants




if __name__ == '__main__':

	input_stream = sys.stdin

	num_cities, distribution = [int(x) for x in input_stream.readline().strip().split(" ")]
	cities = [int(x) for x in input_stream.readline().strip().split(" ")]

	print(f"Solution: {solve(distribution, cities)}")