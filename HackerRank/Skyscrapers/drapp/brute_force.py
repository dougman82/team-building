# #!/bin/python3

import sys, time


# This solution will simply iterate through all skyscrapers to 
# find all valid paths.

def solve(arr):
	valid_paths = 0
	length = len(arr)

	# Do the double iteration dance!!!
	for i in range(length):
		for j in range(length):

			# Ignore the case where both pointers point to same skyscraper
			# Ensure both skyscrapers are same height
			if (i != j) and (arr[i] == arr[j]):

				min_idx = min(i, j)
				max_idx = max(i, j)
				valid = True
				for k in range(min_idx + 1, max_idx):
					if arr[k] > arr[i]:
						valid = False
						break
				if valid:
					valid_paths += 1

	return valid_paths


if __name__ == '__main__':

	input_stream = sys.stdin

	arr_count = input_stream.readline()
	arr = list(map(int, input_stream.readline().rstrip().split()))

	result = 0
	delta_time = 0
	iterations = 100
	for i in range(iterations):
		time_start = time.clock()
		result = solve(arr)
		time_end = time.clock()
		delta_time += time_end - time_start
	print("Average time: " + str(delta_time / iterations))

	print(result)