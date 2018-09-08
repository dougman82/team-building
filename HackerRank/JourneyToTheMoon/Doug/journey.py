
import sys


def solve_naive(num_astronauts, pairs):
	
	lookup = {}
	countries = {}
	
	cur_country = 0
	astronaut_count = 0
	highest_astronaut = 0
	for pair in pairs:
		left = pair[0]
		right = pair[1]

		# Add astronauts to the lookup table, but only if we haven't already seen them
		# Count astronauts as we go to determine how many singletons we need to add later
		if left in lookup:
			# Make sure they are the same country - if not, merge them (into left's)
			if right in lookup:
				if lookup[left] != lookup[right]:
					countries[lookup[left]] += countries[lookup[right]]
					del countries[lookup[right]]
					tmp = lookup[right]
					for item in lookup:
						if lookup[item] == tmp:
							lookup[item] = lookup[left]

			# Add right to left's country
			else:
				lookup[right] = lookup[left]
				countries[lookup[left]].append(right)
				astronaut_count += 1
				highest_astronaut = max(highest_astronaut, right)
		else:
			# Add left to right's country
			if right in lookup:
				lookup[left] = lookup[right]
				countries[lookup[right]].append(left)
				astronaut_count += 1
				highest_astronaut = max(highest_astronaut, left)

			# Two new entries - put in same country
			else:
				lookup[left] = lookup[right] = cur_country
				countries[cur_country] = [left, right]
				astronaut_count += 2
				cur_country += 1
				highest_astronaut = max(highest_astronaut, max(left, right))

	# Now account for the singleton astronauts using a higher index than we've seen
	unpaired_astronauts = num_astronauts - astronaut_count
	highest_astronaut += 1
	for i in range(unpaired_astronauts):
		countries[cur_country] = [highest_astronaut + i]
		astronaut_count += 1
		cur_country += 1

	# Calculate total combinations by adding all unique multiples
	num_countries = len(countries)
	combos = 0
	keys = list(countries.keys())
	countries_scratch = dict(countries)
	for key in keys:
		source_len = len(countries_scratch[key])
		del countries_scratch[key]
		for country in countries_scratch:
			combos += source_len * len(countries_scratch[country])


	for country in countries:
		print(f"Members of country {country}: {countries[country]}")

	return combos



def solve_fast(num_astronauts, pairs):
	return "fast"


if __name__ == '__main__':

	if len(sys.argv) is not 2:
		print("Invalid number of options: " + str(len(sys.argv) - 1))
		print("Required: 1 (\"naive\", \"fast\")")
		sys.exit(1)

	option = sys.argv[1]
	if option not in ("naive", "fast"):
		print("Invalid option: " + option)
		print("Required: \"naive\", \"fast\"")
		sys.exit(2)

	input_stream = sys.stdin

	num_astronauts, num_pairs = [int(x) for x in input_stream.readline().strip().split(" ")]
	pairs = []
	for pair in range(num_pairs):
		pairs.append([int(x) for x in input_stream.readline().strip().split(" ")])

	if option == "naive":
		result = solve_naive(num_astronauts, pairs)
	elif option == "fast":
		result = solve_fast(num_astronauts, pairs)

	print(f"Valid astronaut pairs: {result}")