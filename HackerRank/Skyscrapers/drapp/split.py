# #!/bin/python3

import sys, time


# This solution will iterate down from the max height and then split the remaining
# problem space, divide and conquer. Complexity O(?)

def solve(arr):
	valid_paths = 0
	length = len(arr)
	max_height = max(arr)
	num_max_height = arr.count(max_height)
	#print(num_max_height)

	# Calculate number of paths on the highest skyscrapers
	if num_max_height > 1:
		valid_paths = num_max_height * (num_max_height - 1)
		###print (str(valid_paths) + " valid paths for tallest in " + str(arr))
	
	# Return immediately if there is nothing else to split
	if num_max_height == length:
		return valid_paths

	# Split the remaining skyscrapers
	tallest_indices = [i for i, x in enumerate(arr) if x == max_height]
	#print("tallest_indices: " + str(tallest_indices))
	for i in range(len(tallest_indices)):
		cur = tallest_indices[i]

		# To the left of the left-most tall skyscraper			
		if i == 0:
			# Instead of "cur < 0"
			# This ignores the case where only one building remains to the left
			if cur > 1:
				valid_paths += solve(arr[0:cur])

		# To the right of the right-most tall skyscraper
		if i == (len(tallest_indices) - 1):
			# Instead of "cur < (len(arr) - 1)"
			# This ignores the case where only one building remains to the right
			if cur < (length - 2):
				valid_paths += solve(arr[cur + 1:])

		
		# In between the current and next tall skyscrapers
		else:
			# Ignore stretches of 1 (or 0) buildings in between
			nxt = tallest_indices[i + 1]
			gap = nxt - cur - 1
			###print("cur, nxt, gap: [" + str(cur) + ", " + str(nxt) + ", " + str(gap) + "]")
			if gap >= 2:
				valid_paths += solve(arr[cur + 1:nxt])

	return valid_paths


if __name__ == '__main__':

	input_stream = sys.stdin

	arr_count = input_stream.readline().strip()
	arr = list(map(int, input_stream.readline().strip().split()))

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