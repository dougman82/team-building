import unittest


def pylons(k, arr):

    # using variables to index for in-IDE variable name completion
    can_host_plant = 'can_host_plant'
    has_electricity = 'has_electricity'
    index = 'index'
    plant_built = 'plant_built'

    # Create a dictionary of information for each city:
    # can_host_plant: if the city was a 1 in the original array, this is true
    # has_electricity: if the city has a power plant k - 1 cities away or less, this is true
    # index: the original index of the plant, for convenience
    # plant_built: true if a plant has been built at this city
    cities = [{can_host_plant: True if int(val) == 1 else False, has_electricity: False, index: idx, plant_built: False} for idx, val in enumerate(arr)]
    for city in cities:
        # Only worry about cities with no electricity yet
        if not city[has_electricity]:
            # This is our range of cities we want to check for power plant availability
            best_city_index = city[index] + (k - 1)
            worst_city_index = city[index] - (k - 1)

            # Make sure we stay within the array
            if worst_city_index < 0:
                worst_city_index = 0
            if best_city_index > len(arr) - 1:
                best_city_index = len(arr) - 1

            # Find the best city to build the plant at, and build it
            # don't forget to mark all cities k - 1 cities away as powered
            for candidate_plant_city in cities[worst_city_index:best_city_index + 1][::-1]:
                # The first city in our range is the best candidate
                if candidate_plant_city[can_host_plant]:
                    candidate_plant_city[plant_built] = True

                    # Provide power to cities k - 1 cities away
                    first_city_index = candidate_plant_city[index] - (k - 1)
                    last_city_index = candidate_plant_city[index] + (k - 1)

                    # Make sure we stay within the array
                    if first_city_index < 0:
                        first_city_index = 0
                    if last_city_index > len(cities) - 1:
                        last_city_index = len(cities) - 1

                    for _city in cities[first_city_index:last_city_index + 1][::-1]:
                        _city[has_electricity] = True
                    break
            # Yeah! for/else construct!
            else:
                # If we got here, it's because no candidate cities could host a power plant
                # this city can't be powered
                return -1
    # Double for/else construct!
    else:
        # how many cities ended up with power plants?
        return len([city for city in cities if city[plant_built]])


class TestPylons(unittest.TestCase):
    def test_pylons(self):
        self.assertEqual(2, pylons(2, [0, 1, 1, 1, 1, 0]))


if __name__ == '__main__':
    unittest.main()
