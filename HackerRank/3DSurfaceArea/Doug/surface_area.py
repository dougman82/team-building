import sys


def surfaceArea(A):
	
	height = len(A)
	width = len(A[0])
	
	# Look at all 6 sides
	
	# Top and bottom always == H x W
	surface_area = 2 * height * width
	
	# For East, West, North, South, start at edge, add difference in height since last (start 0)
	# Right and Left sides
	for row in A:
		
		# Left
		prev_height = 0
		for column in row:
			if prev_height < column:
				surface_area += column - prev_height
			prev_height = column
		
		
		# Right
		prev_height = 0
		for column in row[::-1]:
			if prev_height < column:
				surface_area += column - prev_height
			prev_height = column

		
	# North and South
	for i in range(width):
		
		# North
		prev_height = 0
		for j in range(height):
			cur_height = A[j][i]
			print(cur_height)
			if prev_height < cur_height:
				surface_area += cur_height - prev_height
			prev_height = cur_height
				
		# South
		prev_height = 0
		for j in list(reversed(range(height))):
			cur_height = A[j][i]
			if prev_height < cur_height:
				surface_area += cur_height - prev_height
			prev_height = cur_height

	return surface_area


if __name__ == '__main__':

	input_stream = sys.stdin

	height, width = [int(x) for x in input_stream.readline().strip().split(" ")]
	A = []
	for _ in range(height):
		A.append(list(map(int, input_stream.readline().strip().split())))
	
	print(surfaceArea(A))