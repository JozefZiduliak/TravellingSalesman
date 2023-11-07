import time

from cities import Map

# ! Create generator of permutations
# Implementovat mutaciu
# Also save the information about which generation it is

if __name__ == '__main__':

    # Map size x, Map size Y, Number of Cities, Minimal distance between cities
    #map = Map(200, 200, 40,20)
    #map.start_evolution()
    #map.draw_generations()

    # Creating testing sciprt that will test the algorithm on different maps
    #  5 times on number of cities 20,30 and 40

    number_of_cities = [20,30,40]

    for i in range(10):
            #print(f"Number of cities: {number_of_cities[i]}")
            print(f"Number of iteration: {i}")
            # Measure time
            start_time = time.time()

            map = Map(200, 200, 40,20)
            map.start_evolution()

            end_time = time.time()
            duration = end_time - start_time

            print(f"Duration of iteration {i}: {duration:.2f} seconds")

